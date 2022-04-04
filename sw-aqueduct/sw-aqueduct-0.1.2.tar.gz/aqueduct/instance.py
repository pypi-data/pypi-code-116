# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from io import BytesIO

from attr import asdict
from swimlane import Swimlane
from .decorators import log_exception

from .models import (
    Asset,
    User,
    UserLight,
    Role,
    Group,
    Report,
    Package,
    Dashboard,
    Plugin,
    PluginLight,
    Task,
    TaskLight,
    Workflow,
    Workspace
)


class SwimlaneInstance:

    """Creates a connection to a single Swimlane instance
    """

    application_dict = {}
    workflow_dict = {}
    dashboard_dict = {}

    def __init__(self, host='https://sw_web:4443', username=None, password=None, access_token=None,
                 verify_ssl=False, verify_server_version=False, default_timeout=300,
                 resource_cache_size=0, write_to_read_only=False):
        if username and password:
            self.swimlane = Swimlane(
                host=host,
                username=username,
                password=password,
                verify_ssl=verify_ssl,
                verify_server_version=verify_server_version,
                default_timeout=default_timeout,
                resource_cache_size=resource_cache_size,
                write_to_read_only=write_to_read_only
            )
        elif access_token:
            self.swimlane = Swimlane(
                host=host,
                access_token=access_token,
                verify_ssl=verify_ssl,
                verify_server_version=verify_server_version,
                default_timeout=default_timeout,
                resource_cache_size=resource_cache_size,
                write_to_read_only=write_to_read_only
            )
        else:
            raise AttributeError('Please provide either a username and password or a access token!')

        if not self.application_dict:
            self.application_dict = self.__create_application_dict()
        self.plugin_dict = self.__create_plugin_dict()
        self.workflow_dict = self.__create_workflow_dict()
        self.dashboard_dict = self.__create_dashboard_dict()

    def __create_application_dict(self):
        return_dict = {}
        for item in self.get_applications_light():
            if item.get('name') and item['name'] not in return_dict:
                return_dict[item['name']] = item
        return return_dict

    def __create_plugin_dict(self):
        return_dict = {}
        for item in self.get_plugins():
            return_dict[item.id] = self.get_plugin(item.id).fileId
        return return_dict

    def __create_dashboard_dict(self):
        return_dict = {}
        for item in self.get_dashboards():
            return_dict[item.uid] = item
        return return_dict

    def __create_workflow_dict(self):
        return_dict = {}
        if not self.application_dict:
            self.application_dict = self.__create_application_dict()
        for workflow in self.get_workflows():
            for name, item in self.application_dict.items():
                if item.get('id') and workflow.applicationId == item['id']:
                    return_dict[name] = workflow
        return return_dict

    @log_exception
    def get_credentials(self):
        """Used to retrieve keystore items

        Returns:
            dict : A dictionary of keystore keys and encrypted values
        """
        return self.swimlane.request('GET', '/credentials').json()

    @log_exception
    def get_credential(self, name: str):
        """Retrieves keystore item if exists on the desired instance

        Args:
            name (str): A name of a keystore item

        Returns:
            dict : A dictionary of a keystore item
        """
        try:
            return self.swimlane.request('GET', f"/credentials/{name}").json()
        except:
            return False

    @log_exception
    def add_credential(self, credential: dict):
        """Used to add a keystore key name (but not it's value) to a Swimlane instance

        Args:
            credential (dict): A keystore item to add to a Swimlane instance

        Returns:
            dict : A dictionary of a keystore item
        """
        return self.swimlane.request('POST', '/credentials', json=credential).json()

    @log_exception
    def get_tasks(self):
        """Retrieves a list of tasks for a Swimlane instance.

        These tasks are modeled after the `TaskLight` data model

        Returns:
            list: A list of TaskLight objects
        """
        return_list = []
        for task in self.swimlane.request('GET', '/task/list').json().get('tasks'):
            return_list.append(TaskLight(**task))
        return return_list

    @log_exception
    def get_task(self, task_id: str):
        """Gets a task by a provided task ID.

        If the task ID does not exist then this method returns False.

        If the task ID does exist it will return a `Task` object

        Args:
            task_id (str): A task ID to retrieve the entire `Task` object

        Returns:
            Task: A Task data model object
        """
        try:
            return Task(**self.swimlane.request('GET', f'/task/{task_id}').json())
        except:
            return False

    @log_exception
    def add_task(self, task: Task):
        """Adds a provided Task object to a Swimlane instance

        Args:
            task (Task): A Task data model object

        Returns:
            Task: A Task data model object
        """
        return Task(**self.swimlane.request('POST', '/task', json=asdict(task)).json())

    @log_exception
    def update_task(self, task_id: str, task: Task):
        """Updates a provided task ID with the data contained in the provided Task data model object

        Args:
            task_id (str): A task ID to update on a Swimlane instance
            task (Task): A Task data model object

        Returns:
            Task: A Task data model object
        """
        return Task(**self.swimlane.request('PUT', f"/task/{task_id}", json=asdict(task)).json())

    @log_exception
    def get_plugins(self):
        """Retrieves a list of plugins for a Swimlane instance.

        These plugins are modeled after the `PluginLight` data model

        Returns:
            list: A list of PluginLight objects
        """
        return_list = []
        for item in self.swimlane.request('GET', '/task/packages').json():
            return_list.append(PluginLight(**item))
        return return_list

    @log_exception
    def get_plugin(self, name: str):
        """Gets a plugin by a provided plugin name

        If the plugin does not exist then this method returns False.

        If the plugin does exist it will return a `Plugin` object

        Args:
            name (str): A plugin name

        Returns:
            Plugin: A Plugin data model object
        """
        try:
            return Plugin(**self.swimlane.request('GET', f"/task/packages/{name}").json())
        except:
            return False

    @log_exception
    def download_plugin(self, file_id: str):
        """A Swimlane internal fileId for a plugin or Python package to download

        Args:
            file_id (str): A internal Swimlane fileId to download a plugin or python package

        Returns:
            BytesIO: A bytesIO object of the downloaded file
        """
        stream = BytesIO()
        response = self.swimlane.request('GET', f'attachment/download/{file_id}', stream=True)
        for chunk in response.iter_content(1024):
            stream.write(chunk) 
        stream.seek(0)
        return stream

    @log_exception
    def upload_plugin(self, filename, stream):
        """Uploads a plugin to a Swimlane instance given a filename and a BytesIO file stream

        Args:
            filename (str): A filename string
            stream (BytesIO): A BytesIO file stream

        Returns:
            json: JSON Response from uploading a plugin
        """
        if not filename.endswith('.swimbundle'):
            filename = filename.split('.')[0] + '.swimbundle'
        return self.swimlane.request(
            'POST', 
            '/task/packages', 
            files={'file': (filename, stream.read())}
        ).json()

    @log_exception
    def upgrade_plugin(self, filename, stream):
        """Uploads a plugin to be upgraded on a Swimlane instance given a filename and a BytesIO file stream

        Args:
            filename (str): A filename string
            stream (BytesIO): A BytesIO file stream

        Returns:
            json: JSON Response from uploading a plugin
        """
        if not filename.endswith('.swimbundle'):
            filename = filename.split('.')[0] + '.swimbundle'
        return self.swimlane.request(
            'POST', 
            '/task/packages/upgrade', 
            files={'file': (filename, stream.read())}
        ).json()

    @log_exception
    def get_pip_packages(self, versions=['Python2_7', 'Python3_6', 'Python3']):
        """Retrieves a list of pip packages for a Swimlane instance.

        These packages are modeled after the `Package` data model

        Args:
            versions (list, optional): A list of Python versions. Defaults to ['Python2_7', 'Python3_6', 'Python3'].

        Returns:
            list: A list of Package objects
        """
        return_list = []
        for version in versions:
            resp = self.swimlane.request('GET', f"/pip/packages/{version}").json()
            if resp:
                for item in resp:
                    return_list.append(Package(**item))
        return return_list

    @log_exception
    def install_package(self, package: Package):
        """Installs a Python (pip) package based on the provided Package data model object

        Args:
            package (Package): A Package data model object

        Returns:
            dict: A dictionary of a Python pip package
        """
        return self.swimlane.request(
            'POST', 
            '/pip/packages', 
            json={
                "name": package.name, 
                "version": package.version, 
                "pythonVersion": package.pythonVersion
            }
        ).json()

    @log_exception
    def install_package_offline(self, filename, stream, data):
        """Installs a Python package wheel file offline to a Swimlane instance given a filename and a BytesIO file stream

        Args:
            filename (str): A filename string
            stream (BytesIO): A BytesIO file stream
            data (dict): A dictionary of additional request information

        Returns:
            json: JSON Response from installing a python package wheel file
        """
        return self.swimlane.request(
            'POST', 
            '/pip/packages/offline', 
            data=data,
            files={"wheel": (filename, stream.read())},
            timeout=120
        )

    @log_exception
    def get_assets(self):
        """Retrieves a list of assets for a Swimlane instance.

        These assets are modeled after the `Asset` data model

        Returns:
            list: A list of Asset objects
        """
        return_list = []
        for asset in self.swimlane.request('GET', '/asset').json():
            return_list.append(Asset(**asset))
        return return_list

    @log_exception
    def get_asset(self, asset_id: str):
        """Gets a asset by a provided ID

        If the asset does not exist then this method returns False.

        If the asset does exist it will return a `Asset` object

        Args:
            asset_id (str): A Swimlane asset ID

        Returns:
            Asset: A Asset data model object
        """
        try:
            return Asset(**self.swimlane.request('GET', f'/asset/{asset_id}').json())
        except:
            return False

    @log_exception
    def add_asset(self, asset: Asset):
        """Adds a provided Asset object to a Swimlane instance

        Args:
            asset (Asset): A Asset data model object

        Returns:
            Asset: A Asset data model object
        """
        return Asset(**self.swimlane.request('POST', '/asset', json=asdict(asset)).json())

    @log_exception
    def update_asset(self, asset_id: str, asset: Asset):
        """Updates a provided asset ID with the data contained in the provided Asset data model object

        Args:
            asset_id (str): A asset ID to update on a Swimlane instance
            asset (Asset): A Asset data model object

        Returns:
            Asset: A Asset data model object
        """
        return Asset(**self.swimlane.request('PUT', f"/asset/{asset_id}", json=asdict(asset)).json())

    @log_exception
    def get_applications(self):
        """Retrieves a list of applications for a Swimlane instance.

        Returns:
            list: A list of json objects
        """
        return self.swimlane.request('GET', '/app').json()

    @log_exception
    def get_application(self, application_id):
        """Gets a application by a provided ID

        If the application does not exist then this method returns False.

        If the application does exist it will return a JSON object

        Args:
            application_id (str): A Swimlane application ID

        Returns:
            json: A Swimlane application JSON
        """
        try:
            return self.swimlane.request('GET', f'/app/{application_id}').json()
        except:
            return False

    @log_exception
    def get_applications_light(self):
        """Gets light version of all applications

        Returns:
            list: A list of application light objects
        """
        return self.swimlane.request('GET', '/app/light').json()

    @log_exception
    def update_application(self, application):
        """Updates the application based on the provided dictionary object

        Args:
            application (dict): A application dictionary object.

        Returns:
            dict: A Swimlane application object
        """
        return self.swimlane.request('PUT', '/app', json=application).json()

    @log_exception
    def add_application(self, application):
        """Adds an application based on the provided dictionary object

        Args:
            application (dict): A application dictionary object.

        Returns:
            dict: A Swimlane application object
        """
        return self.swimlane.request('POST', '/app', json=application).json()

    @log_exception
    def get_default_report_by_application_id(self, application_id):
        """Gets the default report for an application based on the provided ID

        Args:
            application_id (str): A application dictionary object.

        Returns:
            dict: A Swimlane application object
        """
        try:
            return Report(**self.swimlane.request('GET', f'/reports/app/{application_id}/default').json())
        except:
            return False

    @log_exception
    def get_workspaces(self):
        """Retrieves a list of workspaces for a Swimlane instance.

        These workspaces are modeled after the `Workspace` data model

        Returns:
            list: A list of Workspace objects
        """
        return_list = []
        for workspace in self.swimlane.request('GET', '/workspaces').json():
            return_list.append(Workspace(**workspace))
        return return_list

    @log_exception
    def get_workspace(self, workspace_id: str):
        """Gets a workspace by a provided ID

        If the workspace does not exist then this method returns False.

        If the workspace does exist it will return a `Workspace` object

        Args:
            workspace_id (str): A Swimlane workspace ID

        Returns:
            Workspace: A Workspace data model object
        """
        try:
            return Workspace(**self.swimlane.request('GET', f"/workspaces/{workspace_id}").json())
        except:
            return False

    @log_exception
    def add_workspace(self, workspace: Workspace):
        """Adds a provided Workspace object to a Swimlane instance

        Args:
            workspace (Workspace): A Workspace data model object

        Returns:
            Workspace: A Workspace data model object
        """
        return Workspace(**self.swimlane.request('POST', '/workspaces', json=asdict(workspace)).json())

    @log_exception
    def update_workspace(self, workspace_id: str, workspace: Workspace):
        """Updates a provided workspace ID with the data contained in the provided Workspace data model object

        Args:
            workspace_id (str): A workspace ID to update on a Swimlane instance
            workspace (Workspace): A Workspace data model object

        Returns:
            Workspace: A Workspace data model object
        """
        return Workspace(**self.swimlane.request('PUT', f"/workspaces/{workspace_id}", json=asdict(workspace)).json())

    @log_exception
    def get_dashboards(self):
        """Retrieves a list of dashboards for a Swimlane instance.

        These dashboards are modeled after the `Dashboard` data model

        Returns:
            list: A list of Dashboard objects
        """
        return_list = []
        for dashboard in self.swimlane.request('GET', '/dashboard').json():
            if dashboard:
                return_list.append(Dashboard(**dashboard))
        return return_list

    @log_exception
    def get_dashboard(self, dashboard_id: str):
        """Gets a dashboard by a provided ID

        If the dashboard does not exist then this method returns False.

        If the dashboard does exist it will return a `Dashboard` object

        Args:
            dashboard_id (str): A Swimlane dashboard ID

        Returns:
            Dashboard: A Dashboard data model object
        """
        try:
            return Dashboard(**self.swimlane.request('GET', f"/dashboard/{dashboard_id}").json())
        except:
            return False

    @log_exception
    def update_dashboard(self, dashboard: Dashboard):
        """Updates a Swimlane instance dashboard based on the provied Dashboard data model object

        Args:
            dashboard (Dashboard): A Dashboard data model object

        Returns:
            Dashboard: A Dashboard data model object
        """
        return Dashboard(**self.swimlane.request('PUT', f"/dashboard/{dashboard.id}", json=asdict(dashboard)).json())

    @log_exception
    def add_dashboard(self, dashboard: Dashboard):
        """Adds a provided Dashboard object to a Swimlane instance

        Args:
            dashboard (Dashboard): A Dashboard data model object

        Returns:
            Dashboard: A Dashboard data model object
        """
        return Dashboard(**self.swimlane.request('POST', '/dashboard', json=asdict(dashboard)).json())

    @log_exception
    def get_reports(self):
        """Retrieves a list of reports for a Swimlane instance.

        These reports are modeled after the `Report` data model

        Returns:
            list: A list of Report objects
        """
        return_list = []
        for report in self.swimlane.request('GET', '/reports').json():
            return_list.append(Report(**report))
        return return_list

    @log_exception
    def get_report(self, report_id: str):
        """Gets a report by a provided ID

        If the report does not exist then this method returns False.

        If the report does exist it will return a `Report` object

        Args:
            report_id (str): A Swimlane report ID

        Returns:
            Report: A Report data model object
        """
        try:
            return Report(**self.swimlane.request('GET', f"/reports/{report_id}").json())
        except:
            return False

    @log_exception
    def add_report(self, report: Report):
        """Adds a provided Report object to a Swimlane instance

        Args:
            report (Report): A Report data model object

        Returns:
            Report: A Report data model object
        """
        return Report(**self.swimlane.request('POST', '/reports', json=asdict(report)).json())

    @log_exception
    def update_report(self, report_id: str, report: Report):
        """Updates a provided report ID with the data contained in the provided Report data model object

        Args:
            report_id (str): A report ID to update on a Swimlane instance
            report (Report): A Report data model object

        Returns:
            Report: A Report data model object
        """
        resp = self.swimlane.request('PUT', f"/reports/{report_id}", json=asdict(report))
        if resp.ok:
            return True

    @log_exception
    def update_default_report(self, report: Report):
        """Updates a Swimlane applications default report with the data contained in the provided Report data model object

        Args:
            report (Report): A Report data model object

        Returns:
            Report: A Report data model object
        """
        return Report(**self.swimlane.request('PUT', f"/reports/app/{report.applicationIds[0]}/default", json=asdict(report)).json())

    @log_exception
    def get_users(self):
        """Retrieves a list of users for a Swimlane instance.

        These users are modeled after the `User` data model

        Returns:
            list: A list of User objects
        """
        user_list = []
        for user in self.swimlane.request('GET', '/user/light').json():
            user_list.append(UserLight(**user))
        return user_list

    @log_exception
    def get_user(self, user_id: str):
        """Gets a user by a provided ID

        If the user does not exist then this method returns False.

        If the user does exist it will return a `User` object

        Args:
            user_id (str): A Swimlane user ID

        Returns:
            User: A User data model object
        """
        try:
            return User(**self.swimlane.request('GET', f'/user/{user_id}').json())
        except:
            return False

    @log_exception
    def search_user(self, query_string: str):
        """Searches for a user by a query string

        If the user does not exist then this method returns False.

        If the user does exist it will return a `User` object

        Args:
            query_string (str): A query string typically a display name

        Returns:
            User: A User data model object
        """
        try:
            resp = self.swimlane.request('GET', f"/user/search?query={query_string}").json()
            if resp:
                return User(**resp[0])
        except:
            return False

    @log_exception
    def add_user(self, user: User):
        """Adds a provided User object to a Swimlane instance

        Args:
            user (User): A User data model object

        Returns:
            User: A User data model object
        """
        return User(**self.swimlane.request('POST', '/user', json=asdict(user)).json())

    @log_exception
    def update_user(self, user_id: str, user: User):
        """Updates a provided user ID with the data contained in the provided User data model object

        Args:
            user_id (str): A user ID to update on a Swimlane instance
            user (User): A User data model object

        Returns:
            User: A User data model object
        """
        return User(**self.swimlane.request('PUT', f"/user/{user_id}", json=asdict(user)).json())

    @log_exception
    def get_groups(self):
        """Retrieves a list of groups for a Swimlane instance.

        These groups are modeled after the `Group` data model

        Returns:
            list: A list of Group objects
        """
        return_list = []
        for item in self.swimlane.request('GET', '/groups').json().get('items'):
            return_list.append(Group(**item))
        return return_list

    @log_exception
    def get_group_by_name(self, group_name: str):
        """Gets a group by a provided name

        If the group does not exist then this method returns False.

        If the group does exist it will return a `Group` object

        Args:
            group_name (str): A Swimlane group name

        Returns:
            Group: A Group data model object
        """
        try:
            return Group(**self.swimlane.request('GET', f'/groups/lookup?name={group_name}').json()[0])
        except:
            return False

    @log_exception
    def get_group_by_id(self, group_id: str):
        """Gets a group by a provided id

        If the group does not exist then this method returns False.

        If the group does exist it will return a `Group` object

        Args:
            group_id (str): A Swimlane group ID

        Returns:
            Group: A Group data model object
        """
        try:
            return Group(**self.swimlane.request('GET', f'/groups/{group_id}').json())
        except:
            return False

    @log_exception
    def add_group(self, group: Group):
        """Adds a provided Group object to a Swimlane instance

        Args:
            group (Group): A Group data model object

        Returns:
            Group: A Group data model object
        """
        return Group(**self.swimlane.request('POST', '/groups', json=asdict(group)).json())

    @log_exception
    def update_group(self, group_id: str, group: Group):
        """Updates a provided group ID with the data contained in the provided Group data model object

        Args:
            group_id (str): A group ID to update on a Swimlane instance
            group (Group): A Group data model object

        Returns:
            Group: A Group data model object
        """
        return Group(**self.swimlane.request('PUT', f'/groups/{group_id}', json=asdict(group)).json())

    @log_exception
    def get_roles(self):
        """Retrieves a list of roles for a Swimlane instance.

        These roles are modeled after the `Role` data model

        Returns:
            list: A list of Role objects
        """
        return_list = []
        for role in self.swimlane.request('GET', '/roles').json().get('items'):
            return_list.append(Role(**role))
        return return_list

    @log_exception
    def get_role(self, role_id: str):
        """Gets a role by a provided ID

        If the role does not exist then this method returns False.

        If the role does exist it will return a `Role` object

        Args:
            role_id (str): A Swimlane role ID

        Returns:
            Role: A Role data model object
        """
        try:
            return Role(**self.swimlane.request('GET', f"/roles/{role_id}").json())
        except:
            return False

    @log_exception
    def get_role_by_name(self, role_name: str):
        """Gets a role by a provided name

        If the role does not exist then this method returns False.

        If the role does exist it will return a `Role` object

        Args:
            role_name (str): A Swimlane role name

        Returns:
            Role: A Role data model object
        """
        try:
            return Role(**self.swimlane.request('GET', f'/roles/?searchFieldName=name&searchValue={role_name}').json())
        except:
            return False

    @log_exception
    def add_role(self, role: Role):
        """Adds a provided Role object to a Swimlane instance

        Args:
            role (Role): A Role data model object

        Returns:
            Role: A Role data model object
        """
        return Role(**self.swimlane.request('POST', '/roles', json=asdict(role)).json())

    @log_exception
    def update_role(self, role_id: str, role: Role):
        """Updates a provided role ID with the data contained in the provided Role data model object

        Args:
            role_id (str): A role ID to update on a Swimlane instance
            role (Role): A Role data model object

        Returns:
            Role: A Role data model object
        """
        return self.swimlane.request('PUT', f'/roles/{role_id}', json=asdict(role)).json()

    @log_exception
    def get_workflows(self):
        """Retrieves a list of workflows for a Swimlane instance.

        These workflow are modeled after the `Workflow` data model

        Returns:
            list: A list of Workflow objects
        """
        return_list = []
        for workflow in self.swimlane.request('GET', '/workflow/').json():
            return_list.append(Workflow(**workflow))
        return return_list

    @log_exception
    def get_workflow(self, application_id: str):
        """Gets a workflow by a provided application ID

        If the workflow does not exist then this method returns False.

        If the workflow does exist it will return a `Workflow` object

        Args:
            application_id (str): A Swimlane application ID

        Returns:
            Workflow: A Workflow data model object
        """
        try:
            return Workflow(**self.swimlane.request('GET', f"/workflow/{application_id}").json())
        except:
            return False

    @log_exception
    def add_workflow(self, workflow: Workflow):
        """Adds a provided Workflow object to a Swimlane instance

        Args:
            workflow (Workflow): A Workflow data model object

        Returns:
            Workflow: A Workflow data model object
        """
        return Workflow(**self.swimlane.request('POST', '/workflow/', json=asdict(workflow)).json())

    @log_exception
    def update_workflow(self, workflow: Workflow):
        """Updates a Swimlane instance with the provided Workflow data model object

        Args:
            workflow (Workflow): A Workflow data model object

        Returns:
            Workflow: A Workflow data model object
        """
        return Workflow(**self.swimlane.request('PUT', f"/workflow/{workflow.id}", json=asdict(workflow)).json())
