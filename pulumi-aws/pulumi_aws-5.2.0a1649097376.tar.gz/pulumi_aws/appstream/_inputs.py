# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DirectoryConfigServiceAccountCredentialsArgs',
    'FleetComputeCapacityArgs',
    'FleetDomainJoinInfoArgs',
    'FleetVpcConfigArgs',
    'ImageBuilderAccessEndpointArgs',
    'ImageBuilderDomainJoinInfoArgs',
    'ImageBuilderVpcConfigArgs',
    'StackAccessEndpointArgs',
    'StackApplicationSettingsArgs',
    'StackStorageConnectorArgs',
    'StackUserSettingArgs',
]

@pulumi.input_type
class DirectoryConfigServiceAccountCredentialsArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 account_password: pulumi.Input[str]):
        """
        :param pulumi.Input[str] account_name: User name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.
        :param pulumi.Input[str] account_password: Password for the account.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "account_password", account_password)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        User name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="accountPassword")
    def account_password(self) -> pulumi.Input[str]:
        """
        Password for the account.
        """
        return pulumi.get(self, "account_password")

    @account_password.setter
    def account_password(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_password", value)


@pulumi.input_type
class FleetComputeCapacityArgs:
    def __init__(__self__, *,
                 desired_instances: pulumi.Input[int],
                 available: Optional[pulumi.Input[int]] = None,
                 in_use: Optional[pulumi.Input[int]] = None,
                 running: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] desired_instances: Desired number of streaming instances.
        :param pulumi.Input[int] available: Number of currently available instances that can be used to stream sessions.
        :param pulumi.Input[int] in_use: Number of instances in use for streaming.
        :param pulumi.Input[int] running: Total number of simultaneous streaming instances that are running.
        """
        pulumi.set(__self__, "desired_instances", desired_instances)
        if available is not None:
            pulumi.set(__self__, "available", available)
        if in_use is not None:
            pulumi.set(__self__, "in_use", in_use)
        if running is not None:
            pulumi.set(__self__, "running", running)

    @property
    @pulumi.getter(name="desiredInstances")
    def desired_instances(self) -> pulumi.Input[int]:
        """
        Desired number of streaming instances.
        """
        return pulumi.get(self, "desired_instances")

    @desired_instances.setter
    def desired_instances(self, value: pulumi.Input[int]):
        pulumi.set(self, "desired_instances", value)

    @property
    @pulumi.getter
    def available(self) -> Optional[pulumi.Input[int]]:
        """
        Number of currently available instances that can be used to stream sessions.
        """
        return pulumi.get(self, "available")

    @available.setter
    def available(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "available", value)

    @property
    @pulumi.getter(name="inUse")
    def in_use(self) -> Optional[pulumi.Input[int]]:
        """
        Number of instances in use for streaming.
        """
        return pulumi.get(self, "in_use")

    @in_use.setter
    def in_use(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "in_use", value)

    @property
    @pulumi.getter
    def running(self) -> Optional[pulumi.Input[int]]:
        """
        Total number of simultaneous streaming instances that are running.
        """
        return pulumi.get(self, "running")

    @running.setter
    def running(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "running", value)


@pulumi.input_type
class FleetDomainJoinInfoArgs:
    def __init__(__self__, *,
                 directory_name: Optional[pulumi.Input[str]] = None,
                 organizational_unit_distinguished_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] directory_name: Fully qualified name of the directory (for example, corp.example.com).
        :param pulumi.Input[str] organizational_unit_distinguished_name: Distinguished name of the organizational unit for computer accounts.
        """
        if directory_name is not None:
            pulumi.set(__self__, "directory_name", directory_name)
        if organizational_unit_distinguished_name is not None:
            pulumi.set(__self__, "organizational_unit_distinguished_name", organizational_unit_distinguished_name)

    @property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> Optional[pulumi.Input[str]]:
        """
        Fully qualified name of the directory (for example, corp.example.com).
        """
        return pulumi.get(self, "directory_name")

    @directory_name.setter
    def directory_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_name", value)

    @property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> Optional[pulumi.Input[str]]:
        """
        Distinguished name of the organizational unit for computer accounts.
        """
        return pulumi.get(self, "organizational_unit_distinguished_name")

    @organizational_unit_distinguished_name.setter
    def organizational_unit_distinguished_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organizational_unit_distinguished_name", value)


@pulumi.input_type
class FleetVpcConfigArgs:
    def __init__(__self__, *,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: Identifiers of the security groups for the fleet or image builder.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: Identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance.
        """
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Identifiers of the security groups for the fleet or image builder.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)


@pulumi.input_type
class ImageBuilderAccessEndpointArgs:
    def __init__(__self__, *,
                 endpoint_type: pulumi.Input[str],
                 vpce_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] endpoint_type: Type of interface endpoint.
        :param pulumi.Input[str] vpce_id: Identifier (ID) of the VPC in which the interface endpoint is used.
        """
        pulumi.set(__self__, "endpoint_type", endpoint_type)
        if vpce_id is not None:
            pulumi.set(__self__, "vpce_id", vpce_id)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[str]:
        """
        Type of interface endpoint.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="vpceId")
    def vpce_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier (ID) of the VPC in which the interface endpoint is used.
        """
        return pulumi.get(self, "vpce_id")

    @vpce_id.setter
    def vpce_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpce_id", value)


@pulumi.input_type
class ImageBuilderDomainJoinInfoArgs:
    def __init__(__self__, *,
                 directory_name: Optional[pulumi.Input[str]] = None,
                 organizational_unit_distinguished_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] directory_name: Fully qualified name of the directory (for example, corp.example.com).
        :param pulumi.Input[str] organizational_unit_distinguished_name: Distinguished name of the organizational unit for computer accounts.
        """
        if directory_name is not None:
            pulumi.set(__self__, "directory_name", directory_name)
        if organizational_unit_distinguished_name is not None:
            pulumi.set(__self__, "organizational_unit_distinguished_name", organizational_unit_distinguished_name)

    @property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> Optional[pulumi.Input[str]]:
        """
        Fully qualified name of the directory (for example, corp.example.com).
        """
        return pulumi.get(self, "directory_name")

    @directory_name.setter
    def directory_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_name", value)

    @property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> Optional[pulumi.Input[str]]:
        """
        Distinguished name of the organizational unit for computer accounts.
        """
        return pulumi.get(self, "organizational_unit_distinguished_name")

    @organizational_unit_distinguished_name.setter
    def organizational_unit_distinguished_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organizational_unit_distinguished_name", value)


@pulumi.input_type
class ImageBuilderVpcConfigArgs:
    def __init__(__self__, *,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: Identifiers of the security groups for the image builder or image builder.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: Identifiers of the subnets to which a network interface is attached from the image builder instance or image builder instance.
        """
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Identifiers of the security groups for the image builder or image builder.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Identifiers of the subnets to which a network interface is attached from the image builder instance or image builder instance.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)


@pulumi.input_type
class StackAccessEndpointArgs:
    def __init__(__self__, *,
                 endpoint_type: pulumi.Input[str],
                 vpce_id: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "endpoint_type", endpoint_type)
        if vpce_id is not None:
            pulumi.set(__self__, "vpce_id", vpce_id)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="vpceId")
    def vpce_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vpce_id")

    @vpce_id.setter
    def vpce_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpce_id", value)


@pulumi.input_type
class StackApplicationSettingsArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 settings_group: Optional[pulumi.Input[str]] = None):
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if settings_group is not None:
            pulumi.set(__self__, "settings_group", settings_group)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="settingsGroup")
    def settings_group(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "settings_group")

    @settings_group.setter
    def settings_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "settings_group", value)


@pulumi.input_type
class StackStorageConnectorArgs:
    def __init__(__self__, *,
                 connector_type: pulumi.Input[str],
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_identifier: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] connector_type: Type of storage connector. Valid values are: `HOMEFOLDERS`, `GOOGLE_DRIVE`, `ONE_DRIVE`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domains: Names of the domains for the account.
        :param pulumi.Input[str] resource_identifier: ARN of the storage connector.
        """
        pulumi.set(__self__, "connector_type", connector_type)
        if domains is not None:
            pulumi.set(__self__, "domains", domains)
        if resource_identifier is not None:
            pulumi.set(__self__, "resource_identifier", resource_identifier)

    @property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Input[str]:
        """
        Type of storage connector. Valid values are: `HOMEFOLDERS`, `GOOGLE_DRIVE`, `ONE_DRIVE`.
        """
        return pulumi.get(self, "connector_type")

    @connector_type.setter
    def connector_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "connector_type", value)

    @property
    @pulumi.getter
    def domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Names of the domains for the account.
        """
        return pulumi.get(self, "domains")

    @domains.setter
    def domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "domains", value)

    @property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the storage connector.
        """
        return pulumi.get(self, "resource_identifier")

    @resource_identifier.setter
    def resource_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_identifier", value)


@pulumi.input_type
class StackUserSettingArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 permission: pulumi.Input[str]):
        """
        :param pulumi.Input[str] action: Action that is enabled or disabled. Valid values are: `CLIPBOARD_COPY_FROM_LOCAL_DEVICE`,  `CLIPBOARD_COPY_TO_LOCAL_DEVICE`, `FILE_UPLOAD`, `FILE_DOWNLOAD`, `PRINTING_TO_LOCAL_DEVICE`, `DOMAIN_PASSWORD_SIGNIN`, `DOMAIN_SMART_CARD_SIGNIN`.
        :param pulumi.Input[str] permission: Indicates whether the action is enabled or disabled. Valid values are: `ENABLED`, `DISABLED`.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "permission", permission)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        """
        Action that is enabled or disabled. Valid values are: `CLIPBOARD_COPY_FROM_LOCAL_DEVICE`,  `CLIPBOARD_COPY_TO_LOCAL_DEVICE`, `FILE_UPLOAD`, `FILE_DOWNLOAD`, `PRINTING_TO_LOCAL_DEVICE`, `DOMAIN_PASSWORD_SIGNIN`, `DOMAIN_SMART_CARD_SIGNIN`.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def permission(self) -> pulumi.Input[str]:
        """
        Indicates whether the action is enabled or disabled. Valid values are: `ENABLED`, `DISABLED`.
        """
        return pulumi.get(self, "permission")

    @permission.setter
    def permission(self, value: pulumi.Input[str]):
        pulumi.set(self, "permission", value)


