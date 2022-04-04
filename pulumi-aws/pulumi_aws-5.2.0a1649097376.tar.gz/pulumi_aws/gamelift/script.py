# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ScriptArgs', 'Script']

@pulumi.input_type
class ScriptArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_location: Optional[pulumi.Input['ScriptStorageLocationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 zip_file: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Script resource.
        :param pulumi.Input[str] name: Name of the script
        :param pulumi.Input['ScriptStorageLocationArgs'] storage_location: Information indicating where your game script files are stored. See below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] version: Version that is associated with this script.
        :param pulumi.Input[str] zip_file: A data object containing your Realtime scripts and dependencies as a zip  file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if storage_location is not None:
            pulumi.set(__self__, "storage_location", storage_location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if version is not None:
            pulumi.set(__self__, "version", version)
        if zip_file is not None:
            pulumi.set(__self__, "zip_file", zip_file)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the script
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> Optional[pulumi.Input['ScriptStorageLocationArgs']]:
        """
        Information indicating where your game script files are stored. See below.
        """
        return pulumi.get(self, "storage_location")

    @storage_location.setter
    def storage_location(self, value: Optional[pulumi.Input['ScriptStorageLocationArgs']]):
        pulumi.set(self, "storage_location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Version that is associated with this script.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter(name="zipFile")
    def zip_file(self) -> Optional[pulumi.Input[str]]:
        """
        A data object containing your Realtime scripts and dependencies as a zip  file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.
        """
        return pulumi.get(self, "zip_file")

    @zip_file.setter
    def zip_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zip_file", value)


@pulumi.input_type
class _ScriptState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_location: Optional[pulumi.Input['ScriptStorageLocationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 zip_file: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Script resources.
        :param pulumi.Input[str] arn: Gamelift Script ARN.
        :param pulumi.Input[str] name: Name of the script
        :param pulumi.Input['ScriptStorageLocationArgs'] storage_location: Information indicating where your game script files are stored. See below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        :param pulumi.Input[str] version: Version that is associated with this script.
        :param pulumi.Input[str] zip_file: A data object containing your Realtime scripts and dependencies as a zip  file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if storage_location is not None:
            pulumi.set(__self__, "storage_location", storage_location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if version is not None:
            pulumi.set(__self__, "version", version)
        if zip_file is not None:
            pulumi.set(__self__, "zip_file", zip_file)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        Gamelift Script ARN.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the script
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> Optional[pulumi.Input['ScriptStorageLocationArgs']]:
        """
        Information indicating where your game script files are stored. See below.
        """
        return pulumi.get(self, "storage_location")

    @storage_location.setter
    def storage_location(self, value: Optional[pulumi.Input['ScriptStorageLocationArgs']]):
        pulumi.set(self, "storage_location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Version that is associated with this script.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter(name="zipFile")
    def zip_file(self) -> Optional[pulumi.Input[str]]:
        """
        A data object containing your Realtime scripts and dependencies as a zip  file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.
        """
        return pulumi.get(self, "zip_file")

    @zip_file.setter
    def zip_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zip_file", value)


class Script(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_location: Optional[pulumi.Input[pulumi.InputType['ScriptStorageLocationArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 zip_file: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an Gamelift Script resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.gamelift.Script("example", storage_location=aws.gamelift.ScriptStorageLocationArgs(
            bucket=aws_s3_bucket["example"]["bucket"],
            key=aws_s3_object["example"]["key"],
            role_arn=aws_iam_role["example"]["arn"],
        ))
        ```

        ## Import

        Gamelift Scripts can be imported using the ID, e.g.,

        ```sh
         $ pulumi import aws:gamelift/script:Script example <script-id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of the script
        :param pulumi.Input[pulumi.InputType['ScriptStorageLocationArgs']] storage_location: Information indicating where your game script files are stored. See below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] version: Version that is associated with this script.
        :param pulumi.Input[str] zip_file: A data object containing your Realtime scripts and dependencies as a zip  file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ScriptArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Gamelift Script resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.gamelift.Script("example", storage_location=aws.gamelift.ScriptStorageLocationArgs(
            bucket=aws_s3_bucket["example"]["bucket"],
            key=aws_s3_object["example"]["key"],
            role_arn=aws_iam_role["example"]["arn"],
        ))
        ```

        ## Import

        Gamelift Scripts can be imported using the ID, e.g.,

        ```sh
         $ pulumi import aws:gamelift/script:Script example <script-id>
        ```

        :param str resource_name: The name of the resource.
        :param ScriptArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScriptArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_location: Optional[pulumi.Input[pulumi.InputType['ScriptStorageLocationArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 zip_file: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScriptArgs.__new__(ScriptArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["storage_location"] = storage_location
            __props__.__dict__["tags"] = tags
            __props__.__dict__["version"] = version
            __props__.__dict__["zip_file"] = zip_file
            __props__.__dict__["arn"] = None
            __props__.__dict__["tags_all"] = None
        super(Script, __self__).__init__(
            'aws:gamelift/script:Script',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            storage_location: Optional[pulumi.Input[pulumi.InputType['ScriptStorageLocationArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            version: Optional[pulumi.Input[str]] = None,
            zip_file: Optional[pulumi.Input[str]] = None) -> 'Script':
        """
        Get an existing Script resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Gamelift Script ARN.
        :param pulumi.Input[str] name: Name of the script
        :param pulumi.Input[pulumi.InputType['ScriptStorageLocationArgs']] storage_location: Information indicating where your game script files are stored. See below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        :param pulumi.Input[str] version: Version that is associated with this script.
        :param pulumi.Input[str] zip_file: A data object containing your Realtime scripts and dependencies as a zip  file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ScriptState.__new__(_ScriptState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["name"] = name
        __props__.__dict__["storage_location"] = storage_location
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["version"] = version
        __props__.__dict__["zip_file"] = zip_file
        return Script(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Gamelift Script ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the script
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> pulumi.Output['outputs.ScriptStorageLocation']:
        """
        Information indicating where your game script files are stored. See below.
        """
        return pulumi.get(self, "storage_location")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        Version that is associated with this script.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="zipFile")
    def zip_file(self) -> pulumi.Output[Optional[str]]:
        """
        A data object containing your Realtime scripts and dependencies as a zip  file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.
        """
        return pulumi.get(self, "zip_file")

