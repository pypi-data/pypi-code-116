"""Jobs functionality - consolidates and replaces legacy "custom scripts" and "reports" features."""
from collections import OrderedDict
import inspect
import json
import logging
import os
import pkgutil
import sys
import shutil
import traceback
import warnings


from cacheops import cached
from db_file_storage.form_widgets import DBClearableFileInput
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import RegexValidator
from django.db import transaction
from django.db.models import Model
from django.db.models.query import QuerySet
from django.forms import ValidationError
from django.utils import timezone
from django.utils.functional import classproperty
import netaddr
import yaml


from .choices import JobResultStatusChoices, LogLevelChoices
from .context_managers import change_logging
from .datasources.git import ensure_git_repository
from .forms import JobForm
from .models import FileProxy, GitRepository, ScheduledJob
from .registry import registry

from nautobot.core.celery import nautobot_task
from nautobot.ipam.formfields import IPAddressFormField, IPNetworkFormField
from nautobot.ipam.validators import (
    MaxPrefixLengthValidator,
    MinPrefixLengthValidator,
    prefix_validator,
)
from nautobot.utilities.exceptions import AbortTransaction
from nautobot.utilities.forms import (
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
)


User = get_user_model()


__all__ = [
    "Job",
    "BooleanVar",
    "ChoiceVar",
    "FileVar",
    "IntegerVar",
    "IPAddressVar",
    "IPAddressWithMaskVar",
    "IPNetworkVar",
    "MultiChoiceVar",
    "MultiObjectVar",
    "ObjectVar",
    "StringVar",
    "TextVar",
]

logger = logging.getLogger("nautobot.jobs")


class BaseJob:
    """Base model for jobs (reports, scripts).

    Users can subclass this directly if they want to provide their own base class for implementing multiple jobs
    with shared functionality; if no such sharing is required, use Job class instead.

    For backward compatibility with NetBox, this class has several APIs that can be implemented by the user:

    1. run(self, data, commit) - First method called when invoking a Job, can handle setup and parameter storage.
    2. test_*(self) - Any method matching this pattern will be called next
    3. post_run(self) - Last method called, will be called even in case of an exception during the above methods
    """

    class Meta:
        """
        Metaclass attributes - subclasses can define any or all of the following attributes:

        - name (str)
        - description (str)
        - commit_default (bool)
        - field_order (list)
        - read_only (bool)
        - approval_required (bool)
        """

        pass

    def __init__(self):
        self.logger = logging.getLogger(f"nautobot.jobs.{self.__class__.__name__}")

        self.request = None
        self.active_test = "main"
        self.failed = False
        self._job_result = None

        # Grab some info about the job
        self.source = inspect.getsource(self.__class__)

        # Compile test methods and initialize results skeleton
        self.test_methods = []

        for method_name in dir(self):
            if method_name.startswith("test_") and callable(getattr(self, method_name)):
                self.test_methods.append(method_name)

    def __str__(self):
        return self.name

    @classproperty
    def file_path(cls):
        return inspect.getfile(cls)

    @classproperty
    def class_path(cls):
        """
        Unique identifier of a specific Job class, in the form <source_grouping>/<module_name>/<ClassName>.

        Examples:
        local/my_script/MyScript
        plugins/my_plugin.jobs/MyPluginJob
        git.my-repository/myjob/MyJob
        """
        # TODO: it'd be nice if this were derived more automatically instead of needing this logic
        if cls in registry["plugin_jobs"]:
            source_grouping = "plugins"
        elif cls.file_path.startswith(settings.JOBS_ROOT):
            source_grouping = "local"
        elif cls.file_path.startswith(settings.GIT_ROOT):
            # $GIT_ROOT/<repo_slug>/jobs/job.py -> <repo_slug>
            source_grouping = ".".join(
                [
                    "git",
                    os.path.basename(os.path.dirname(os.path.dirname(cls.file_path))),
                ]
            )
        else:
            raise RuntimeError(
                f"Unknown/unexpected job file_path {cls.file_path}, should be one of "
                + ", ".join([settings.JOBS_ROOT, settings.GIT_ROOT])
            )

        return "/".join([source_grouping, cls.__module__, cls.__name__])

    @classproperty
    def class_path_dotted(cls):
        """
        Dotted class_path, suitable for use in things like Python logger names.
        """
        return cls.class_path.replace("/", ".")

    @classproperty
    def class_path_js_escaped(cls):
        """
        Escape various characters so that the class_path can be used as a jQuery selector.
        """
        return cls.class_path.replace("/", r"\/").replace(".", r"\.")

    @classproperty
    def name(cls):
        return getattr(cls.Meta, "name", cls.__name__)

    @classproperty
    def description(cls):
        return getattr(cls.Meta, "description", "")

    @classproperty
    def read_only(cls):
        return getattr(cls.Meta, "read_only", False)

    @classproperty
    def approval_required(cls):
        return getattr(cls.Meta, "approval_required", False)

    @classmethod
    def _get_vars(cls):
        vars = OrderedDict()
        for name, attr in cls.__dict__.items():
            if name not in vars and issubclass(attr.__class__, ScriptVariable):
                vars[name] = attr

        return vars

    @classmethod
    def _get_file_vars(cls):
        """Return an ordered dict of FileVar fields."""
        vars = cls._get_vars()
        file_vars = OrderedDict()
        for name, attr in vars.items():
            if isinstance(attr, FileVar):
                file_vars[name] = attr

        return file_vars

    @property
    def job_result(self):
        return self._job_result

    @job_result.setter
    def job_result(self, value):
        # Initialize job_result data format for our usage
        value.data = OrderedDict()

        self._job_result = value

    @property
    def results(self):
        """
        The results generated by this job.
        ** If you need the logs, you will need to filter on JobLogEntry **
            Ex.
            from nautobot.extras.models import JogLogEntry

            JobLogEntry.objects.filter(job_result=self.job_result, <other criteria>)

        {
            "output": "...",
        }
        """
        return self.job_result.data if self.job_result else None

    def as_form(self, data=None, files=None, initial=None, approval_view=False):
        """
        Return a Django form suitable for populating the context data required to run this Job.

        `approval_view` will disable all fields from modification and is used to display the form
        during a approval review workflow.
        """
        fields = {name: var.as_field() for name, var in self._get_vars().items()}
        FormClass = type("JobForm", (JobForm,), fields)

        form = FormClass(data, files, initial=initial)

        if self.read_only:
            # Hide the commit field for read only jobs
            form.fields["_commit"].widget = forms.HiddenInput()
            form.fields["_commit"].initial = False
        else:
            # Set initial "commit" checkbox state based on the Meta parameter
            form.fields["_commit"].initial = getattr(self.Meta, "commit_default", True)

        field_order = getattr(self.Meta, "field_order", None)

        if field_order:
            form.order_fields(field_order)

        if approval_view:
            # Set `disabled=True` on all fields
            for _, field in form.fields.items():
                field.disabled = True

            # Alter the commit help text to avoid confusion concerning approval dry-runs
            form.fields["_commit"].help_text = "Commit changes to the database"

        return form

    @staticmethod
    def serialize_data(data):
        """
        This method parses input data (from JobForm usually) and returns a dict which is safe to serialize

        Here we convert the QuerySet of a MultiObjectVar to a list of the pk's and the model instance
        of an ObjectVar into the pk value.

        These are converted back during job execution.
        """

        return_data = {}
        for field_name, value in data.items():
            # MultiObjectVar
            if isinstance(value, QuerySet):
                return_data[field_name] = list(value.values_list("pk", flat=True))
            # ObjectVar
            elif isinstance(value, Model):
                return_data[field_name] = value.pk
            # FileVar (Save each FileVar as a FileProxy)
            elif isinstance(value, InMemoryUploadedFile):
                return_data[field_name] = BaseJob.save_file(value)
            # IPAddressVar, IPAddressWithMaskVar, IPNetworkVar
            elif isinstance(value, netaddr.ip.BaseIP):
                return_data[field_name] = str(value)
            # Everything else...
            else:
                return_data[field_name] = value

        return return_data

    @classmethod
    def deserialize_data(cls, data):
        """
        Given data input for a job execution, deserialize it by resolving object references using defined variables.

        This converts a list of pk's back into a QuerySet for MultiObjectVar instances and single pk values into
        model instances for ObjectVar.

        Note that when resolving querysets or model instances by their PK, we do not catch DoesNotExist
        exceptions here, we leave it up the caller to handle those cases. The normal job execution code
        path would consider this a failure of the job execution, as described in `nautobot.extras.jobs.run_job`.
        """
        vars = cls._get_vars()
        return_data = {}

        if not isinstance(data, dict):
            raise TypeError("Data should be a dictionary.")

        for field_name, value in data.items():
            # If a field isn't a var, skip it (e.g. `_commit`).
            try:
                var = vars[field_name]
            except KeyError:
                continue

            if value is None:
                if var.field_attrs.get("required"):
                    raise ValidationError(f"{field_name} is a required field")
                else:
                    return_data[field_name] = value
                    continue

            if isinstance(var, MultiObjectVar):
                queryset = var.field_attrs["queryset"].filter(pk__in=value)
                if queryset.count() < len(value):
                    # Not all objects found
                    not_found_pk_list = value - list(queryset.values_list("pk", flat=True))
                    raise queryset.model.DoesNotExist(
                        f"Failed to find requested objects for var {field_name}: [{', '.join(not_found_pk_list)}]"
                    )
                return_data[field_name] = var.field_attrs["queryset"].filter(pk__in=value)

            elif isinstance(var, ObjectVar):
                if isinstance(value, dict):
                    return_data[field_name] = var.field_attrs["queryset"].get(**value)
                else:
                    return_data[field_name] = var.field_attrs["queryset"].get(pk=value)
            elif isinstance(var, FileVar):
                return_data[field_name] = cls.load_file(value)
            # IPAddressVar is a netaddr.IPAddress object
            elif isinstance(var, IPAddressVar):
                return_data[field_name] = netaddr.IPAddress(value)
            # IPAddressWithMaskVar, IPNetworkVar are netaddr.IPNetwork objects
            elif isinstance(var, (IPAddressWithMaskVar, IPNetworkVar)):
                return_data[field_name] = netaddr.IPNetwork(value)
            else:
                return_data[field_name] = value

        return return_data

    def validate_data(self, data):
        vars = self._get_vars()

        if not isinstance(data, dict):
            raise ValidationError("Job data needs to be a dict")

        for k, v in data.items():
            if k not in vars:
                raise ValidationError({k: "Job data contained an unknown property"})

        # defer validation to the form object
        f = self.as_form(data=self.deserialize_data(data))
        if not f.is_valid():
            raise ValidationError(f.errors)

    @staticmethod
    def load_file(pk):
        """Load a file proxy stored in the database by primary key.

        Args:
            pk (uuid): Primary key of the `FileProxy` to retrieve

        Returns:
            File-like object
        """
        fp = FileProxy.objects.get(pk=pk)
        return fp.file

    @staticmethod
    def save_file(uploaded_file):
        """
        Save an uploaded file to the database as a file proxy and return the
        primary key.

        Args:
            uploaded_file (file): File handle of file to save to database

        Returns:
            uuid
        """
        fp = FileProxy.objects.create(name=uploaded_file.name, file=uploaded_file)
        return fp.pk

    @staticmethod
    def delete_files(*files_to_delete):
        """Given an unpacked list of primary keys for `FileProxy` objects, delete them.

        Args:
            files_to_delete (*args): List of primary keys to delete

        Returns:
            int (number of objects deleted)
        """
        files = FileProxy.objects.filter(pk__in=files_to_delete)
        num = 0
        for fp in files:
            fp.delete()  # Call delete() on each, so `FileAttachment` is reaped
            num += 1
        logger.debug(f"Deleted {num} file proxies")
        return num

    def run(self, data, commit):
        """
        Method invoked when this Job is run, before any "test_*" methods.
        """
        pass

    def post_run(self):
        """
        Method invoked after "run()" and all "test_*" methods.
        """
        pass

    # Logging

    def _log(self, obj, message, level_choice=LogLevelChoices.LOG_DEFAULT):
        """
        Log a message. Do not call this method directly; use one of the log_* wrappers below.
        """
        self.job_result.log(
            message,
            obj=obj,
            level_choice=level_choice,
            grouping=self.active_test,
            logger=self.logger,
        )

    def log(self, message):
        """
        Log a generic message which is not associated with a particular object.
        """
        self._log(None, message, level_choice=LogLevelChoices.LOG_DEFAULT)

    def log_debug(self, message):
        """
        Log a debug message which is not associated with a particular object.
        """
        self._log(None, message, level_choice=LogLevelChoices.LOG_DEFAULT)

    def log_success(self, obj=None, message=None):
        """
        Record a successful test against an object. Logging a message is optional.
        If the object provided is a string, treat it as a message. This is a carryover of Netbox Report API
        """
        if isinstance(obj, str) and message is None:
            self._log(obj=None, message=obj, level_choice=LogLevelChoices.LOG_SUCCESS)
        else:
            self._log(obj, message, level_choice=LogLevelChoices.LOG_SUCCESS)

    def log_info(self, obj=None, message=None):
        """
        Log an informational message.
        If the object provided is a string, treat it as a message. This is a carryover of Netbox Report API
        """
        if isinstance(obj, str) and message is None:
            self._log(obj=None, message=obj, level_choice=LogLevelChoices.LOG_INFO)
        else:
            self._log(obj, message, level_choice=LogLevelChoices.LOG_INFO)

    def log_warning(self, obj=None, message=None):
        """
        Log a warning.
        If the object provided is a string, treat it as a message. This is a carryover of Netbox Report API
        """
        if isinstance(obj, str) and message is None:
            self._log(obj=None, message=obj, level_choice=LogLevelChoices.LOG_WARNING)
        else:
            self._log(obj, message, level_choice=LogLevelChoices.LOG_WARNING)

    def log_failure(self, obj=None, message=None):
        """
        Log a failure. Calling this method will automatically mark the overall job as failed.
        If the object provided is a string, treat it as a message. This is a carryover of Netbox Report API
        """
        if isinstance(obj, str) and message is None:
            self._log(obj=None, message=obj, level_choice=LogLevelChoices.LOG_FAILURE)
        else:
            self._log(obj, message, level_choice=LogLevelChoices.LOG_FAILURE)
        self.failed = True

    # Convenience functions

    def load_yaml(self, filename):
        """
        Return data from a YAML file
        """
        file_path = os.path.join(os.path.dirname(self.file_path), filename)
        with open(file_path, "r") as datafile:
            data = yaml.safe_load(datafile)

        return data

    def load_json(self, filename):
        """
        Return data from a JSON file
        """
        file_path = os.path.join(os.path.dirname(self.file_path), filename)
        with open(file_path, "r") as datafile:
            data = json.load(datafile)

        return data


class Job(BaseJob):
    """
    Classes which inherit from this model will appear in the list of available jobs.
    """


#
# Script variables
#


class ScriptVariable:
    """
    Base model for script variables
    """

    form_field = forms.CharField

    def __init__(self, label="", description="", default=None, required=True, widget=None):

        # Initialize field attributes
        if not hasattr(self, "field_attrs"):
            self.field_attrs = {}
        if label:
            self.field_attrs["label"] = label
        if description:
            self.field_attrs["help_text"] = description
        if default:
            self.field_attrs["initial"] = default
        if widget:
            self.field_attrs["widget"] = widget
        self.field_attrs["required"] = required

    def as_field(self):
        """
        Render the variable as a Django form field.
        """
        form_field = self.form_field(**self.field_attrs)
        if not isinstance(form_field.widget, forms.CheckboxInput):
            if form_field.widget.attrs and "class" in form_field.widget.attrs.keys():
                form_field.widget.attrs["class"] += " form-control"
            else:
                form_field.widget.attrs["class"] = "form-control"

        return form_field


class StringVar(ScriptVariable):
    """
    Character string representation. Can enforce minimum/maximum length and/or regex validation.
    """

    def __init__(self, min_length=None, max_length=None, regex=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Optional minimum/maximum lengths
        if min_length:
            self.field_attrs["min_length"] = min_length
        if max_length:
            self.field_attrs["max_length"] = max_length

        # Optional regular expression validation
        if regex:
            self.field_attrs["validators"] = [
                RegexValidator(
                    regex=regex,
                    message="Invalid value. Must match regex: {}".format(regex),
                    code="invalid",
                )
            ]


class TextVar(ScriptVariable):
    """
    Free-form text data. Renders as a <textarea>.
    """

    form_field = forms.CharField

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.field_attrs["widget"] = forms.Textarea


class IntegerVar(ScriptVariable):
    """
    Integer representation. Can enforce minimum/maximum values.
    """

    form_field = forms.IntegerField

    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Optional minimum/maximum values
        if min_value:
            self.field_attrs["min_value"] = min_value
        if max_value:
            self.field_attrs["max_value"] = max_value


class BooleanVar(ScriptVariable):
    """
    Boolean representation (true/false). Renders as a checkbox.
    """

    form_field = forms.BooleanField

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Boolean fields cannot be required
        self.field_attrs["required"] = False


class ChoiceVar(ScriptVariable):
    """
    Select one of several predefined static choices, passed as a list of two-tuples. Example:

        color = ChoiceVar(
            choices=(
                ('#ff0000', 'Red'),
                ('#00ff00', 'Green'),
                ('#0000ff', 'Blue')
            )
        )
    """

    form_field = forms.ChoiceField

    def __init__(self, choices, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set field choices
        self.field_attrs["choices"] = choices


class MultiChoiceVar(ChoiceVar):
    """
    Like ChoiceVar, but allows for the selection of multiple choices.
    """

    form_field = forms.MultipleChoiceField


class ObjectVar(ScriptVariable):
    """
    A single object within Nautobot.

    :param model: The Nautobot model being referenced
    :param display_field: The attribute of the returned object to display in the selection list (default: 'name')
    :param query_params: A dictionary of additional query parameters to attach when making REST API requests (optional)
    :param null_option: The label to use as a "null" selection option (optional)
    """

    form_field = DynamicModelChoiceField

    def __init__(
        self,
        model=None,
        queryset=None,
        display_field="display",
        query_params=None,
        null_option=None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        # Set the form field's queryset. Support backward compatibility for the "queryset" argument for now.
        if model is not None:
            self.field_attrs["queryset"] = model.objects.all()
        elif queryset is not None:
            warnings.warn(
                f'{self}: Specifying a queryset for ObjectVar is no longer supported. Please use "model" instead.'
            )
            self.field_attrs["queryset"] = queryset
        else:
            raise TypeError("ObjectVar must specify a model")

        self.field_attrs.update(
            {
                "display_field": display_field,
                "query_params": query_params,
                "null_option": null_option,
            }
        )


class MultiObjectVar(ObjectVar):
    """
    Like ObjectVar, but can represent one or more objects.
    """

    form_field = DynamicModelMultipleChoiceField


class DatabaseFileField(forms.FileField):
    """Specialized `FileField` for use with `DatabaseFileStorage` storage backend."""

    widget = DBClearableFileInput


class FileVar(ScriptVariable):
    """
    An uploaded file.
    """

    form_field = DatabaseFileField


class IPAddressVar(ScriptVariable):
    """
    An IPv4 or IPv6 address without a mask.
    """

    form_field = IPAddressFormField


class IPAddressWithMaskVar(ScriptVariable):
    """
    An IPv4 or IPv6 address with a mask.
    """

    form_field = IPNetworkFormField


class IPNetworkVar(ScriptVariable):
    """
    An IPv4 or IPv6 prefix.
    """

    form_field = IPNetworkFormField

    def __init__(self, min_prefix_length=None, max_prefix_length=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set prefix validator and optional minimum/maximum prefix lengths
        self.field_attrs["validators"] = [prefix_validator]
        if min_prefix_length is not None:
            self.field_attrs["validators"].append(MinPrefixLengthValidator(min_prefix_length))
        if max_prefix_length is not None:
            self.field_attrs["validators"].append(MaxPrefixLengthValidator(max_prefix_length))


def is_job(obj):
    """
    Returns True if the given object is a Job subclass.
    """
    from .scripts import Script, BaseScript
    from .reports import Report

    try:
        return issubclass(obj, Job) and obj not in [Job, Script, BaseScript, Report]
    except TypeError:
        return False


def is_variable(obj):
    """
    Returns True if the object is a ScriptVariable instance.
    """
    return isinstance(obj, ScriptVariable)


def get_jobs():
    """
    Compile a dictionary of all jobs available across all modules in the jobs path(s).

    Returns an OrderedDict:

    {
        "local": {
            <module_name>: {
                "name": <human-readable module name>,
                "jobs": {
                   <class_name>: <job_class>,
                   <class_name>: <job_class>,
                   ...
                },
            },
            <module_name>: { ... },
            ...
        },
        "git.<repository-slug>": {
            <module_name>: { ... },
        },
        ...
        "plugins": {
            <module_name>: { ... },
        }
    }
    """
    jobs = OrderedDict()

    paths = _get_job_source_paths()

    # Iterate over all groupings (local, git.<slug1>, git.<slug2>, etc.)
    for grouping, path_list in paths.items():
        # Iterate over all modules (Python files) found in any of the directory paths identified for the given grouping
        for importer, module_name, _ in pkgutil.iter_modules(path_list):
            try:
                # Remove cached module to ensure consistency with filesystem
                if module_name in sys.modules:
                    del sys.modules[module_name]

                # Dynamically import this module to make its contents (job(s)) available to Python
                module = importer.find_module(module_name).load_module(module_name)
            except Exception as exc:
                logger.error(f"Unable to load job {module_name}: {exc}")
                continue

            # For each module, we construct a dict {"name": module_name, "jobs": {"job_name": job_class, ...}}
            human_readable_name = module.name if hasattr(module, "name") else module_name
            module_jobs = {"name": human_readable_name, "jobs": OrderedDict()}
            # Get all Job subclasses (which includes Script and Report subclasses as well) in this module,
            # and add them to the dict
            for name, cls in inspect.getmembers(module, is_job):
                module_jobs["jobs"][name] = cls

            # If there were any Job subclasses found, add the module_jobs dict to the overall jobs dict
            # (otherwise skip it since there aren't any jobs in this module to report)
            if module_jobs["jobs"]:
                jobs.setdefault(grouping, {})[module_name] = module_jobs

    # Add jobs from plugins (which were already imported at startup)
    for cls in registry["plugin_jobs"]:
        module = inspect.getmodule(cls)
        human_readable_name = module.name if hasattr(module, "name") else module.__name__
        jobs.setdefault("plugins", {}).setdefault(module.__name__, {"name": human_readable_name, "jobs": OrderedDict()})
        jobs["plugins"][module.__name__]["jobs"][cls.__name__] = cls

    return jobs


def _get_job_source_paths():
    """
    Helper function to get_jobs().

    Constructs a dict of {"grouping": [filesystem_path, ...]}.
    Current groupings are "local", "git.<repository_slug>".
    Plugin jobs aren't loaded dynamically from a source_path and so are not included in this function
    """
    paths = {}
    # Locally installed jobs
    if settings.JOBS_ROOT and os.path.exists(settings.JOBS_ROOT):
        paths.setdefault("local", []).append(settings.JOBS_ROOT)

    # Jobs derived from Git repositories
    if settings.GIT_ROOT and os.path.isdir(settings.GIT_ROOT):
        for repository_record in GitRepository.objects.all():
            if "extras.job" not in repository_record.provided_contents:
                # This repository isn't marked as containing jobs that we should use.
                continue

            try:
                # In the case where we have multiple Nautobot instances, or multiple RQ worker instances,
                # they are not required to share a common filesystem; therefore, we may need to refresh our local clone
                # of the Git repository to ensure that it is in sync with the latest repository clone from any instance.
                ensure_git_repository(
                    repository_record,
                    head=repository_record.current_head,
                    logger=logger,
                )
            except Exception as exc:
                logger.error(f"Error during local clone of Git repository {repository_record}: {exc}")
                continue

            jobs_path = os.path.join(repository_record.filesystem_path, "jobs")
            if os.path.isdir(jobs_path):
                paths[f"git.{repository_record.slug}"] = [jobs_path]
            else:
                logger.warning(f"Git repository {repository_record} is configured to provide jobs, but none are found!")

        # TODO: when a Git repo is deleted or its slug is changed, we update the local filesystem
        # (see extras/signals.py, extras/models/datasources.py), but as noted above, there may be multiple filesystems
        # involved, so not all local clones of deleted Git repositories may have been deleted yet.
        # For now, if we encounter a "leftover" Git repo here, we delete it now.
        for git_slug in os.listdir(settings.GIT_ROOT):
            git_path = os.path.join(settings.GIT_ROOT, git_slug)
            if not os.path.isdir(git_path):
                logger.warning(
                    f"Found non-directory {git_slug} in {settings.GIT_ROOT}. Only Git repositories should exist here."
                )
            elif not os.path.isdir(os.path.join(git_path, ".git")):
                logger.warning(f"Directory {git_slug} in {settings.GIT_ROOT} does not appear to be a Git repository.")
            elif not GitRepository.objects.filter(slug=git_slug):
                logger.warning(f"Deleting unmanaged (leftover?) repository at {git_path}")
                shutil.rmtree(git_path)

    return paths


@cached(timeout=60)
def get_job_classpaths():
    """
    Get a list of all known Job class_path strings.

    This is used as a cacheable, light-weight alternative to calling get_jobs() or get_job()
    when all that's needed is to verify whether a given job exists.
    """
    jobs_dict = get_jobs()
    result = set()
    for grouping_name, modules_dict in jobs_dict.items():
        for module_name in modules_dict:
            for class_name in modules_dict[module_name]["jobs"]:
                result.add(f"{grouping_name}/{module_name}/{class_name}")
    return result


def get_job(class_path):
    """
    Retrieve a specific job class by its class_path.

    Note that this is built atop get_jobs() and so is not a particularly light-weight API;
    if all you need to do is to verify whether a given class_path exists, use get_job_classpaths() instead.

    Returns None if not found.
    """
    try:
        grouping_name, module_name, class_name = class_path.split("/", 2)
    except ValueError:
        logger.error(f'Invalid class_path value "{class_path}"')
        return None

    jobs = get_jobs()
    return jobs.get(grouping_name, {}).get(module_name, {}).get("jobs", {}).get(class_name, None)


@nautobot_task
def run_job(data, request, job_result_pk, commit=True, *args, **kwargs):
    """
    Helper function to call the "run()", "test_*()", and "post_run" methods on a Job.

    This function is responsible for setting up the job execution, handing the DB tranaction
    and rollback conditions, plus post execution cleanup and saving the JobResult record.
    """
    from nautobot.extras.models import JobResult  # avoid circular import

    # Getting the correct job result can fail if the stored data cannot be serialized.
    # Catching `TypeError: the JSON object must be str, bytes or bytearray, not int`
    try:
        job_result = JobResult.objects.get(pk=job_result_pk)
    except TypeError as e:
        logger.error(f"Unable to serialize data for job {job_result_pk}")
        logger.error(e)
        return False

    job_class = get_job(job_result.name)
    if not job_class:
        job_result.log(
            f'Unable to locate job "{job_result.name}" to run it!',
            level_choice=LogLevelChoices.LOG_FAILURE,
            grouping="initialization",
            logger=logger,
        )
        job_result.status = JobResultStatusChoices.STATUS_ERRORED
        job_result.completed = timezone.now()
        job_result.save()
        return False

    try:
        job = job_class()
        job.active_test = "initialization"
        job.job_result = job_result
    except Exception as error:
        logger.error("Error initializing job object.")
        logger.error(error)
        stacktrace = traceback.format_exc()
        job_result.log_failure(f"Error initializing job:\n```\n{stacktrace}\n```")
        job_result.set_status(JobResultStatusChoices.STATUS_ERRORED)
        job_result.completed = timezone.now()
        job_result.save()
        return False

    try:
        # Capture the file IDs for any FileProxy objects created so we can cleanup later.
        file_ids = None
        file_fields = list(job._get_file_vars())
        file_ids = [data[f] for f in file_fields]

        # Attempt to resolve serialized data back into original form by creating querysets or model instances
        # If we fail to find any objects, we consider this a job execution error, and fail.
        # This might happen when a job sits on the queue for a while (i.e. scheduled) and data has changed
        # or it might be bad input from an API request, or manual execution.

        data = job_class.deserialize_data(data)
    except Exception:
        job_result.set_status(JobResultStatusChoices.STATUS_ERRORED)
        stacktrace = traceback.format_exc()
        job_result.log(
            f"Error initializing job:\n```\n{stacktrace}\n```",
            level_choice=LogLevelChoices.LOG_FAILURE,
            grouping="initialization",
            logger=logger,
        )
        job_result.completed = timezone.now()
        job_result.save()
        if file_ids:
            job.delete_files(*file_ids)  # Cleanup FileProxy objects
        return False

    if job.read_only:
        # Force commit to false for read only jobs.
        commit = False

    # TODO: validate that all args required by this job are set in the data or else log helpful errors?

    job.logger.info(f"Running job (commit={commit})")

    job_result.set_status(JobResultStatusChoices.STATUS_RUNNING)
    job_result.save()

    # Add the current request as a property of the job
    job.request = request

    def _run_job():
        """
        Core job execution task.

        We capture this within a subfunction to allow for conditionally wrapping it with the change_logging
        context manager (which is only relevant if commit == True).

        If the job is marked as read_only == True, then commit is forced to False and no log messages will be
        emitted related to reverting database changes.
        """
        started = timezone.now()
        job.results["output"] = ""
        try:
            with transaction.atomic():
                # Script-like behavior
                job.active_test = "run"
                output = job.run(data=data, commit=commit)
                if output:
                    job.results["output"] += "\n" + str(output)

                # Report-like behavior
                for method_name in job.test_methods:
                    job.active_test = method_name
                    output = getattr(job, method_name)()
                    if output:
                        job.results["output"] += "\n" + str(output)

                if job.failed:
                    job.logger.warning("job failed")
                    job_result.set_status(JobResultStatusChoices.STATUS_FAILED)
                else:
                    job.logger.info("job completed successfully")
                    job_result.set_status(JobResultStatusChoices.STATUS_COMPLETED)

                if not commit:
                    raise AbortTransaction()

        except AbortTransaction:
            if not job.read_only:
                job.log_info(message="Database changes have been reverted automatically.")

        except Exception as exc:
            stacktrace = traceback.format_exc()
            job.log_failure(message=f"An exception occurred: `{type(exc).__name__}: {exc}`\n```\n{stacktrace}\n```")
            if not job.read_only:
                job.log_info(message="Database changes have been reverted due to error.")
            job_result.set_status(JobResultStatusChoices.STATUS_ERRORED)

        finally:
            job_result.save()
            job.delete_files(*file_ids)  # Cleanup FileProxy objects

        # record data about this jobrun in the schedule
        if job_result.schedule:
            job_result.schedule.total_run_count += 1
            job_result.schedule.last_run_at = started
            job_result.schedule.save()

        # Perform any post-run tasks
        job.active_test = "post_run"
        output = job.post_run()
        if output:
            job.results["output"] += "\n" + str(output)

        job_result.completed = timezone.now()
        job_result.save()

        job.logger.info(f"Job completed in {job_result.duration}")

    # Execute the job. If commit == True, wrap it with the change_logging context manager to ensure we
    # process change logs, webhooks, etc.
    if commit:
        with change_logging(request):
            _run_job()
    else:
        _run_job()


@nautobot_task
def scheduled_job_handler(*args, **kwargs):
    """
    A thin wrapper around JobResult.enqueue_job() that allows for it to be called as an async task
    for the purposes of enqueuing scheduled jobs at their recurring intervals. Thus, JobResult.enqueue_job()
    is responsible for enqueuing the actual job for execution and this method is the task executed
    by the scheduler to kick off the job execution on a recurring interval.
    """
    from nautobot.extras.models import JobResult  # avoid circular import

    user_pk = kwargs.pop("user")
    user = User.objects.get(pk=user_pk)
    name = kwargs.pop("name")
    scheduled_job_pk = kwargs.pop("scheduled_job_pk")
    schedule = ScheduledJob.objects.get(pk=scheduled_job_pk)

    job_content_type = ContentType.objects.get(app_label="extras", model="job")
    JobResult.enqueue_job(run_job, name, job_content_type, user, schedule=schedule, **kwargs)
