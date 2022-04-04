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

__all__ = ['WorkspaceArgs', 'Workspace']

@pulumi.input_type
class WorkspaceArgs:
    def __init__(__self__, *,
                 bundle_id: pulumi.Input[str],
                 directory_id: pulumi.Input[str],
                 user_name: pulumi.Input[str],
                 root_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 volume_encryption_key: Optional[pulumi.Input[str]] = None,
                 workspace_properties: Optional[pulumi.Input['WorkspaceWorkspacePropertiesArgs']] = None):
        """
        The set of arguments for constructing a Workspace resource.
        :param pulumi.Input[str] bundle_id: The ID of the bundle for the WorkSpace.
        :param pulumi.Input[str] directory_id: The ID of the directory for the WorkSpace.
        :param pulumi.Input[str] user_name: The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
        :param pulumi.Input[bool] root_volume_encryption_enabled: Indicates whether the data stored on the root volume is encrypted.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags for the WorkSpace. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[bool] user_volume_encryption_enabled: Indicates whether the data stored on the user volume is encrypted.
        :param pulumi.Input[str] volume_encryption_key: The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
        :param pulumi.Input['WorkspaceWorkspacePropertiesArgs'] workspace_properties: The WorkSpace properties.
        """
        pulumi.set(__self__, "bundle_id", bundle_id)
        pulumi.set(__self__, "directory_id", directory_id)
        pulumi.set(__self__, "user_name", user_name)
        if root_volume_encryption_enabled is not None:
            pulumi.set(__self__, "root_volume_encryption_enabled", root_volume_encryption_enabled)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if user_volume_encryption_enabled is not None:
            pulumi.set(__self__, "user_volume_encryption_enabled", user_volume_encryption_enabled)
        if volume_encryption_key is not None:
            pulumi.set(__self__, "volume_encryption_key", volume_encryption_key)
        if workspace_properties is not None:
            pulumi.set(__self__, "workspace_properties", workspace_properties)

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Input[str]:
        """
        The ID of the bundle for the WorkSpace.
        """
        return pulumi.get(self, "bundle_id")

    @bundle_id.setter
    def bundle_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "bundle_id", value)

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Input[str]:
        """
        The ID of the directory for the WorkSpace.
        """
        return pulumi.get(self, "directory_id")

    @directory_id.setter
    def directory_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "directory_id", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[str]:
        """
        The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_name", value)

    @property
    @pulumi.getter(name="rootVolumeEncryptionEnabled")
    def root_volume_encryption_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the data stored on the root volume is encrypted.
        """
        return pulumi.get(self, "root_volume_encryption_enabled")

    @root_volume_encryption_enabled.setter
    def root_volume_encryption_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "root_volume_encryption_enabled", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags for the WorkSpace. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="userVolumeEncryptionEnabled")
    def user_volume_encryption_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the data stored on the user volume is encrypted.
        """
        return pulumi.get(self, "user_volume_encryption_enabled")

    @user_volume_encryption_enabled.setter
    def user_volume_encryption_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "user_volume_encryption_enabled", value)

    @property
    @pulumi.getter(name="volumeEncryptionKey")
    def volume_encryption_key(self) -> Optional[pulumi.Input[str]]:
        """
        The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
        """
        return pulumi.get(self, "volume_encryption_key")

    @volume_encryption_key.setter
    def volume_encryption_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_encryption_key", value)

    @property
    @pulumi.getter(name="workspaceProperties")
    def workspace_properties(self) -> Optional[pulumi.Input['WorkspaceWorkspacePropertiesArgs']]:
        """
        The WorkSpace properties.
        """
        return pulumi.get(self, "workspace_properties")

    @workspace_properties.setter
    def workspace_properties(self, value: Optional[pulumi.Input['WorkspaceWorkspacePropertiesArgs']]):
        pulumi.set(self, "workspace_properties", value)


@pulumi.input_type
class _WorkspaceState:
    def __init__(__self__, *,
                 bundle_id: Optional[pulumi.Input[str]] = None,
                 computer_name: Optional[pulumi.Input[str]] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 root_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 user_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 volume_encryption_key: Optional[pulumi.Input[str]] = None,
                 workspace_properties: Optional[pulumi.Input['WorkspaceWorkspacePropertiesArgs']] = None):
        """
        Input properties used for looking up and filtering Workspace resources.
        :param pulumi.Input[str] bundle_id: The ID of the bundle for the WorkSpace.
        :param pulumi.Input[str] computer_name: The name of the WorkSpace, as seen by the operating system.
        :param pulumi.Input[str] directory_id: The ID of the directory for the WorkSpace.
        :param pulumi.Input[str] ip_address: The IP address of the WorkSpace.
        :param pulumi.Input[bool] root_volume_encryption_enabled: Indicates whether the data stored on the root volume is encrypted.
        :param pulumi.Input[str] state: The operational state of the WorkSpace.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags for the WorkSpace. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        :param pulumi.Input[str] user_name: The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
        :param pulumi.Input[bool] user_volume_encryption_enabled: Indicates whether the data stored on the user volume is encrypted.
        :param pulumi.Input[str] volume_encryption_key: The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
        :param pulumi.Input['WorkspaceWorkspacePropertiesArgs'] workspace_properties: The WorkSpace properties.
        """
        if bundle_id is not None:
            pulumi.set(__self__, "bundle_id", bundle_id)
        if computer_name is not None:
            pulumi.set(__self__, "computer_name", computer_name)
        if directory_id is not None:
            pulumi.set(__self__, "directory_id", directory_id)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if root_volume_encryption_enabled is not None:
            pulumi.set(__self__, "root_volume_encryption_enabled", root_volume_encryption_enabled)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if user_name is not None:
            pulumi.set(__self__, "user_name", user_name)
        if user_volume_encryption_enabled is not None:
            pulumi.set(__self__, "user_volume_encryption_enabled", user_volume_encryption_enabled)
        if volume_encryption_key is not None:
            pulumi.set(__self__, "volume_encryption_key", volume_encryption_key)
        if workspace_properties is not None:
            pulumi.set(__self__, "workspace_properties", workspace_properties)

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the bundle for the WorkSpace.
        """
        return pulumi.get(self, "bundle_id")

    @bundle_id.setter
    def bundle_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bundle_id", value)

    @property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the WorkSpace, as seen by the operating system.
        """
        return pulumi.get(self, "computer_name")

    @computer_name.setter
    def computer_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "computer_name", value)

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the directory for the WorkSpace.
        """
        return pulumi.get(self, "directory_id")

    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_id", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the WorkSpace.
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="rootVolumeEncryptionEnabled")
    def root_volume_encryption_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the data stored on the root volume is encrypted.
        """
        return pulumi.get(self, "root_volume_encryption_enabled")

    @root_volume_encryption_enabled.setter
    def root_volume_encryption_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "root_volume_encryption_enabled", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The operational state of the WorkSpace.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags for the WorkSpace. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)

    @property
    @pulumi.getter(name="userVolumeEncryptionEnabled")
    def user_volume_encryption_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the data stored on the user volume is encrypted.
        """
        return pulumi.get(self, "user_volume_encryption_enabled")

    @user_volume_encryption_enabled.setter
    def user_volume_encryption_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "user_volume_encryption_enabled", value)

    @property
    @pulumi.getter(name="volumeEncryptionKey")
    def volume_encryption_key(self) -> Optional[pulumi.Input[str]]:
        """
        The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
        """
        return pulumi.get(self, "volume_encryption_key")

    @volume_encryption_key.setter
    def volume_encryption_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_encryption_key", value)

    @property
    @pulumi.getter(name="workspaceProperties")
    def workspace_properties(self) -> Optional[pulumi.Input['WorkspaceWorkspacePropertiesArgs']]:
        """
        The WorkSpace properties.
        """
        return pulumi.get(self, "workspace_properties")

    @workspace_properties.setter
    def workspace_properties(self, value: Optional[pulumi.Input['WorkspaceWorkspacePropertiesArgs']]):
        pulumi.set(self, "workspace_properties", value)


class Workspace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bundle_id: Optional[pulumi.Input[str]] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 root_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 user_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 volume_encryption_key: Optional[pulumi.Input[str]] = None,
                 workspace_properties: Optional[pulumi.Input[pulumi.InputType['WorkspaceWorkspacePropertiesArgs']]] = None,
                 __props__=None):
        """
        Provides a workspace in [AWS Workspaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html) Service

        > **NOTE:** AWS WorkSpaces service requires [`workspaces_DefaultRole`](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-access-control.html#create-default-role) IAM role to operate normally.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        value_windows10 = aws.workspaces.get_bundle(bundle_id="wsb-bh8rsxt14")
        example = aws.workspaces.Workspace("example",
            directory_id=aws_workspaces_directory["example"]["id"],
            bundle_id=value_windows10.id,
            user_name="john.doe",
            root_volume_encryption_enabled=True,
            user_volume_encryption_enabled=True,
            volume_encryption_key="alias/aws/workspaces",
            workspace_properties=aws.workspaces.WorkspaceWorkspacePropertiesArgs(
                compute_type_name="VALUE",
                user_volume_size_gib=10,
                root_volume_size_gib=80,
                running_mode="AUTO_STOP",
                running_mode_auto_stop_timeout_in_minutes=60,
            ),
            tags={
                "Department": "IT",
            })
        ```

        ## Import

        Workspaces can be imported using their ID, e.g.,

        ```sh
         $ pulumi import aws:workspaces/workspace:Workspace example ws-9z9zmbkhv
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bundle_id: The ID of the bundle for the WorkSpace.
        :param pulumi.Input[str] directory_id: The ID of the directory for the WorkSpace.
        :param pulumi.Input[bool] root_volume_encryption_enabled: Indicates whether the data stored on the root volume is encrypted.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags for the WorkSpace. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] user_name: The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
        :param pulumi.Input[bool] user_volume_encryption_enabled: Indicates whether the data stored on the user volume is encrypted.
        :param pulumi.Input[str] volume_encryption_key: The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
        :param pulumi.Input[pulumi.InputType['WorkspaceWorkspacePropertiesArgs']] workspace_properties: The WorkSpace properties.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a workspace in [AWS Workspaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html) Service

        > **NOTE:** AWS WorkSpaces service requires [`workspaces_DefaultRole`](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-access-control.html#create-default-role) IAM role to operate normally.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        value_windows10 = aws.workspaces.get_bundle(bundle_id="wsb-bh8rsxt14")
        example = aws.workspaces.Workspace("example",
            directory_id=aws_workspaces_directory["example"]["id"],
            bundle_id=value_windows10.id,
            user_name="john.doe",
            root_volume_encryption_enabled=True,
            user_volume_encryption_enabled=True,
            volume_encryption_key="alias/aws/workspaces",
            workspace_properties=aws.workspaces.WorkspaceWorkspacePropertiesArgs(
                compute_type_name="VALUE",
                user_volume_size_gib=10,
                root_volume_size_gib=80,
                running_mode="AUTO_STOP",
                running_mode_auto_stop_timeout_in_minutes=60,
            ),
            tags={
                "Department": "IT",
            })
        ```

        ## Import

        Workspaces can be imported using their ID, e.g.,

        ```sh
         $ pulumi import aws:workspaces/workspace:Workspace example ws-9z9zmbkhv
        ```

        :param str resource_name: The name of the resource.
        :param WorkspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bundle_id: Optional[pulumi.Input[str]] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 root_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 user_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
                 volume_encryption_key: Optional[pulumi.Input[str]] = None,
                 workspace_properties: Optional[pulumi.Input[pulumi.InputType['WorkspaceWorkspacePropertiesArgs']]] = None,
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
            __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

            if bundle_id is None and not opts.urn:
                raise TypeError("Missing required property 'bundle_id'")
            __props__.__dict__["bundle_id"] = bundle_id
            if directory_id is None and not opts.urn:
                raise TypeError("Missing required property 'directory_id'")
            __props__.__dict__["directory_id"] = directory_id
            __props__.__dict__["root_volume_encryption_enabled"] = root_volume_encryption_enabled
            __props__.__dict__["tags"] = tags
            if user_name is None and not opts.urn:
                raise TypeError("Missing required property 'user_name'")
            __props__.__dict__["user_name"] = user_name
            __props__.__dict__["user_volume_encryption_enabled"] = user_volume_encryption_enabled
            __props__.__dict__["volume_encryption_key"] = volume_encryption_key
            __props__.__dict__["workspace_properties"] = workspace_properties
            __props__.__dict__["computer_name"] = None
            __props__.__dict__["ip_address"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["tags_all"] = None
        super(Workspace, __self__).__init__(
            'aws:workspaces/workspace:Workspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bundle_id: Optional[pulumi.Input[str]] = None,
            computer_name: Optional[pulumi.Input[str]] = None,
            directory_id: Optional[pulumi.Input[str]] = None,
            ip_address: Optional[pulumi.Input[str]] = None,
            root_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
            state: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            user_name: Optional[pulumi.Input[str]] = None,
            user_volume_encryption_enabled: Optional[pulumi.Input[bool]] = None,
            volume_encryption_key: Optional[pulumi.Input[str]] = None,
            workspace_properties: Optional[pulumi.Input[pulumi.InputType['WorkspaceWorkspacePropertiesArgs']]] = None) -> 'Workspace':
        """
        Get an existing Workspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bundle_id: The ID of the bundle for the WorkSpace.
        :param pulumi.Input[str] computer_name: The name of the WorkSpace, as seen by the operating system.
        :param pulumi.Input[str] directory_id: The ID of the directory for the WorkSpace.
        :param pulumi.Input[str] ip_address: The IP address of the WorkSpace.
        :param pulumi.Input[bool] root_volume_encryption_enabled: Indicates whether the data stored on the root volume is encrypted.
        :param pulumi.Input[str] state: The operational state of the WorkSpace.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags for the WorkSpace. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        :param pulumi.Input[str] user_name: The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
        :param pulumi.Input[bool] user_volume_encryption_enabled: Indicates whether the data stored on the user volume is encrypted.
        :param pulumi.Input[str] volume_encryption_key: The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
        :param pulumi.Input[pulumi.InputType['WorkspaceWorkspacePropertiesArgs']] workspace_properties: The WorkSpace properties.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkspaceState.__new__(_WorkspaceState)

        __props__.__dict__["bundle_id"] = bundle_id
        __props__.__dict__["computer_name"] = computer_name
        __props__.__dict__["directory_id"] = directory_id
        __props__.__dict__["ip_address"] = ip_address
        __props__.__dict__["root_volume_encryption_enabled"] = root_volume_encryption_enabled
        __props__.__dict__["state"] = state
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["user_name"] = user_name
        __props__.__dict__["user_volume_encryption_enabled"] = user_volume_encryption_enabled
        __props__.__dict__["volume_encryption_key"] = volume_encryption_key
        __props__.__dict__["workspace_properties"] = workspace_properties
        return Workspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Output[str]:
        """
        The ID of the bundle for the WorkSpace.
        """
        return pulumi.get(self, "bundle_id")

    @property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> pulumi.Output[str]:
        """
        The name of the WorkSpace, as seen by the operating system.
        """
        return pulumi.get(self, "computer_name")

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[str]:
        """
        The ID of the directory for the WorkSpace.
        """
        return pulumi.get(self, "directory_id")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
        The IP address of the WorkSpace.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="rootVolumeEncryptionEnabled")
    def root_volume_encryption_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the data stored on the root volume is encrypted.
        """
        return pulumi.get(self, "root_volume_encryption_enabled")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The operational state of the WorkSpace.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags for the WorkSpace. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
        """
        return pulumi.get(self, "user_name")

    @property
    @pulumi.getter(name="userVolumeEncryptionEnabled")
    def user_volume_encryption_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the data stored on the user volume is encrypted.
        """
        return pulumi.get(self, "user_volume_encryption_enabled")

    @property
    @pulumi.getter(name="volumeEncryptionKey")
    def volume_encryption_key(self) -> pulumi.Output[Optional[str]]:
        """
        The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
        """
        return pulumi.get(self, "volume_encryption_key")

    @property
    @pulumi.getter(name="workspaceProperties")
    def workspace_properties(self) -> pulumi.Output['outputs.WorkspaceWorkspaceProperties']:
        """
        The WorkSpace properties.
        """
        return pulumi.get(self, "workspace_properties")

