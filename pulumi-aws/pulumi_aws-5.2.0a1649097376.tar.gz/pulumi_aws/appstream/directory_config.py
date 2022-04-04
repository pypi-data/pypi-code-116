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

__all__ = ['DirectoryConfigArgs', 'DirectoryConfig']

@pulumi.input_type
class DirectoryConfigArgs:
    def __init__(__self__, *,
                 directory_name: pulumi.Input[str],
                 organizational_unit_distinguished_names: pulumi.Input[Sequence[pulumi.Input[str]]],
                 service_account_credentials: pulumi.Input['DirectoryConfigServiceAccountCredentialsArgs']):
        """
        The set of arguments for constructing a DirectoryConfig resource.
        :param pulumi.Input[str] directory_name: Fully qualified name of the directory.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] organizational_unit_distinguished_names: Distinguished names of the organizational units for computer accounts.
        :param pulumi.Input['DirectoryConfigServiceAccountCredentialsArgs'] service_account_credentials: Configuration block for the name of the directory and organizational unit (OU) to use to join the directory config to a Microsoft Active Directory domain. See `service_account_credentials` below.
        """
        pulumi.set(__self__, "directory_name", directory_name)
        pulumi.set(__self__, "organizational_unit_distinguished_names", organizational_unit_distinguished_names)
        pulumi.set(__self__, "service_account_credentials", service_account_credentials)

    @property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> pulumi.Input[str]:
        """
        Fully qualified name of the directory.
        """
        return pulumi.get(self, "directory_name")

    @directory_name.setter
    def directory_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "directory_name", value)

    @property
    @pulumi.getter(name="organizationalUnitDistinguishedNames")
    def organizational_unit_distinguished_names(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Distinguished names of the organizational units for computer accounts.
        """
        return pulumi.get(self, "organizational_unit_distinguished_names")

    @organizational_unit_distinguished_names.setter
    def organizational_unit_distinguished_names(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "organizational_unit_distinguished_names", value)

    @property
    @pulumi.getter(name="serviceAccountCredentials")
    def service_account_credentials(self) -> pulumi.Input['DirectoryConfigServiceAccountCredentialsArgs']:
        """
        Configuration block for the name of the directory and organizational unit (OU) to use to join the directory config to a Microsoft Active Directory domain. See `service_account_credentials` below.
        """
        return pulumi.get(self, "service_account_credentials")

    @service_account_credentials.setter
    def service_account_credentials(self, value: pulumi.Input['DirectoryConfigServiceAccountCredentialsArgs']):
        pulumi.set(self, "service_account_credentials", value)


@pulumi.input_type
class _DirectoryConfigState:
    def __init__(__self__, *,
                 created_time: Optional[pulumi.Input[str]] = None,
                 directory_name: Optional[pulumi.Input[str]] = None,
                 organizational_unit_distinguished_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_account_credentials: Optional[pulumi.Input['DirectoryConfigServiceAccountCredentialsArgs']] = None):
        """
        Input properties used for looking up and filtering DirectoryConfig resources.
        :param pulumi.Input[str] created_time: Date and time, in UTC and extended RFC 3339 format, when the directory config was created.
        :param pulumi.Input[str] directory_name: Fully qualified name of the directory.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] organizational_unit_distinguished_names: Distinguished names of the organizational units for computer accounts.
        :param pulumi.Input['DirectoryConfigServiceAccountCredentialsArgs'] service_account_credentials: Configuration block for the name of the directory and organizational unit (OU) to use to join the directory config to a Microsoft Active Directory domain. See `service_account_credentials` below.
        """
        if created_time is not None:
            pulumi.set(__self__, "created_time", created_time)
        if directory_name is not None:
            pulumi.set(__self__, "directory_name", directory_name)
        if organizational_unit_distinguished_names is not None:
            pulumi.set(__self__, "organizational_unit_distinguished_names", organizational_unit_distinguished_names)
        if service_account_credentials is not None:
            pulumi.set(__self__, "service_account_credentials", service_account_credentials)

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time, in UTC and extended RFC 3339 format, when the directory config was created.
        """
        return pulumi.get(self, "created_time")

    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_time", value)

    @property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> Optional[pulumi.Input[str]]:
        """
        Fully qualified name of the directory.
        """
        return pulumi.get(self, "directory_name")

    @directory_name.setter
    def directory_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_name", value)

    @property
    @pulumi.getter(name="organizationalUnitDistinguishedNames")
    def organizational_unit_distinguished_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Distinguished names of the organizational units for computer accounts.
        """
        return pulumi.get(self, "organizational_unit_distinguished_names")

    @organizational_unit_distinguished_names.setter
    def organizational_unit_distinguished_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "organizational_unit_distinguished_names", value)

    @property
    @pulumi.getter(name="serviceAccountCredentials")
    def service_account_credentials(self) -> Optional[pulumi.Input['DirectoryConfigServiceAccountCredentialsArgs']]:
        """
        Configuration block for the name of the directory and organizational unit (OU) to use to join the directory config to a Microsoft Active Directory domain. See `service_account_credentials` below.
        """
        return pulumi.get(self, "service_account_credentials")

    @service_account_credentials.setter
    def service_account_credentials(self, value: Optional[pulumi.Input['DirectoryConfigServiceAccountCredentialsArgs']]):
        pulumi.set(self, "service_account_credentials", value)


class DirectoryConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 directory_name: Optional[pulumi.Input[str]] = None,
                 organizational_unit_distinguished_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_account_credentials: Optional[pulumi.Input[pulumi.InputType['DirectoryConfigServiceAccountCredentialsArgs']]] = None,
                 __props__=None):
        """
        Provides an AppStream Directory Config.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.appstream.DirectoryConfig("example",
            directory_name="NAME OF DIRECTORY",
            organizational_unit_distinguished_names=["DISTINGUISHED NAME"],
            service_account_credentials=aws.appstream.DirectoryConfigServiceAccountCredentialsArgs(
                account_name="NAME OF ACCOUNT",
                account_password="PASSWORD OF ACCOUNT",
            ))
        ```

        ## Import

        `aws_appstream_directory_config` can be imported using the id, e.g.,

        ```sh
         $ pulumi import aws:appstream/directoryConfig:DirectoryConfig example directoryNameExample
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] directory_name: Fully qualified name of the directory.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] organizational_unit_distinguished_names: Distinguished names of the organizational units for computer accounts.
        :param pulumi.Input[pulumi.InputType['DirectoryConfigServiceAccountCredentialsArgs']] service_account_credentials: Configuration block for the name of the directory and organizational unit (OU) to use to join the directory config to a Microsoft Active Directory domain. See `service_account_credentials` below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DirectoryConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an AppStream Directory Config.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.appstream.DirectoryConfig("example",
            directory_name="NAME OF DIRECTORY",
            organizational_unit_distinguished_names=["DISTINGUISHED NAME"],
            service_account_credentials=aws.appstream.DirectoryConfigServiceAccountCredentialsArgs(
                account_name="NAME OF ACCOUNT",
                account_password="PASSWORD OF ACCOUNT",
            ))
        ```

        ## Import

        `aws_appstream_directory_config` can be imported using the id, e.g.,

        ```sh
         $ pulumi import aws:appstream/directoryConfig:DirectoryConfig example directoryNameExample
        ```

        :param str resource_name: The name of the resource.
        :param DirectoryConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DirectoryConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 directory_name: Optional[pulumi.Input[str]] = None,
                 organizational_unit_distinguished_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_account_credentials: Optional[pulumi.Input[pulumi.InputType['DirectoryConfigServiceAccountCredentialsArgs']]] = None,
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
            __props__ = DirectoryConfigArgs.__new__(DirectoryConfigArgs)

            if directory_name is None and not opts.urn:
                raise TypeError("Missing required property 'directory_name'")
            __props__.__dict__["directory_name"] = directory_name
            if organizational_unit_distinguished_names is None and not opts.urn:
                raise TypeError("Missing required property 'organizational_unit_distinguished_names'")
            __props__.__dict__["organizational_unit_distinguished_names"] = organizational_unit_distinguished_names
            if service_account_credentials is None and not opts.urn:
                raise TypeError("Missing required property 'service_account_credentials'")
            __props__.__dict__["service_account_credentials"] = service_account_credentials
            __props__.__dict__["created_time"] = None
        super(DirectoryConfig, __self__).__init__(
            'aws:appstream/directoryConfig:DirectoryConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_time: Optional[pulumi.Input[str]] = None,
            directory_name: Optional[pulumi.Input[str]] = None,
            organizational_unit_distinguished_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            service_account_credentials: Optional[pulumi.Input[pulumi.InputType['DirectoryConfigServiceAccountCredentialsArgs']]] = None) -> 'DirectoryConfig':
        """
        Get an existing DirectoryConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_time: Date and time, in UTC and extended RFC 3339 format, when the directory config was created.
        :param pulumi.Input[str] directory_name: Fully qualified name of the directory.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] organizational_unit_distinguished_names: Distinguished names of the organizational units for computer accounts.
        :param pulumi.Input[pulumi.InputType['DirectoryConfigServiceAccountCredentialsArgs']] service_account_credentials: Configuration block for the name of the directory and organizational unit (OU) to use to join the directory config to a Microsoft Active Directory domain. See `service_account_credentials` below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DirectoryConfigState.__new__(_DirectoryConfigState)

        __props__.__dict__["created_time"] = created_time
        __props__.__dict__["directory_name"] = directory_name
        __props__.__dict__["organizational_unit_distinguished_names"] = organizational_unit_distinguished_names
        __props__.__dict__["service_account_credentials"] = service_account_credentials
        return DirectoryConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        Date and time, in UTC and extended RFC 3339 format, when the directory config was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> pulumi.Output[str]:
        """
        Fully qualified name of the directory.
        """
        return pulumi.get(self, "directory_name")

    @property
    @pulumi.getter(name="organizationalUnitDistinguishedNames")
    def organizational_unit_distinguished_names(self) -> pulumi.Output[Sequence[str]]:
        """
        Distinguished names of the organizational units for computer accounts.
        """
        return pulumi.get(self, "organizational_unit_distinguished_names")

    @property
    @pulumi.getter(name="serviceAccountCredentials")
    def service_account_credentials(self) -> pulumi.Output['outputs.DirectoryConfigServiceAccountCredentials']:
        """
        Configuration block for the name of the directory and organizational unit (OU) to use to join the directory config to a Microsoft Active Directory domain. See `service_account_credentials` below.
        """
        return pulumi.get(self, "service_account_credentials")

