# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VirtualMfaDeviceArgs', 'VirtualMfaDevice']

@pulumi.input_type
class VirtualMfaDeviceArgs:
    def __init__(__self__, *,
                 virtual_mfa_device_name: pulumi.Input[str],
                 path: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a VirtualMfaDevice resource.
        :param pulumi.Input[str] virtual_mfa_device_name: The name of the virtual MFA device. Use with path to uniquely identify a virtual MFA device.
        :param pulumi.Input[str] path: The path for the virtual MFA device.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of resource tags for the virtual mfa device. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "virtual_mfa_device_name", virtual_mfa_device_name)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="virtualMfaDeviceName")
    def virtual_mfa_device_name(self) -> pulumi.Input[str]:
        """
        The name of the virtual MFA device. Use with path to uniquely identify a virtual MFA device.
        """
        return pulumi.get(self, "virtual_mfa_device_name")

    @virtual_mfa_device_name.setter
    def virtual_mfa_device_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_mfa_device_name", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The path for the virtual MFA device.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of resource tags for the virtual mfa device. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _VirtualMfaDeviceState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 base32_string_seed: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 qr_code_png: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_mfa_device_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VirtualMfaDevice resources.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) specifying the virtual mfa device.
        :param pulumi.Input[str] base32_string_seed: The base32 seed defined as specified in [RFC3548](https://tools.ietf.org/html/rfc3548.txt). The `base_32_string_seed` is base64-encoded.
        :param pulumi.Input[str] path: The path for the virtual MFA device.
        :param pulumi.Input[str] qr_code_png: A QR code PNG image that encodes `otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String` where `$virtualMFADeviceName` is one of the create call arguments. AccountName is the user name if set (otherwise, the account ID otherwise), and Base32String is the seed in base32 format.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of resource tags for the virtual mfa device. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        :param pulumi.Input[str] virtual_mfa_device_name: The name of the virtual MFA device. Use with path to uniquely identify a virtual MFA device.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if base32_string_seed is not None:
            pulumi.set(__self__, "base32_string_seed", base32_string_seed)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if qr_code_png is not None:
            pulumi.set(__self__, "qr_code_png", qr_code_png)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if virtual_mfa_device_name is not None:
            pulumi.set(__self__, "virtual_mfa_device_name", virtual_mfa_device_name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) specifying the virtual mfa device.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="base32StringSeed")
    def base32_string_seed(self) -> Optional[pulumi.Input[str]]:
        """
        The base32 seed defined as specified in [RFC3548](https://tools.ietf.org/html/rfc3548.txt). The `base_32_string_seed` is base64-encoded.
        """
        return pulumi.get(self, "base32_string_seed")

    @base32_string_seed.setter
    def base32_string_seed(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base32_string_seed", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The path for the virtual MFA device.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="qrCodePng")
    def qr_code_png(self) -> Optional[pulumi.Input[str]]:
        """
        A QR code PNG image that encodes `otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String` where `$virtualMFADeviceName` is one of the create call arguments. AccountName is the user name if set (otherwise, the account ID otherwise), and Base32String is the seed in base32 format.
        """
        return pulumi.get(self, "qr_code_png")

    @qr_code_png.setter
    def qr_code_png(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "qr_code_png", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of resource tags for the virtual mfa device. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    @pulumi.getter(name="virtualMfaDeviceName")
    def virtual_mfa_device_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the virtual MFA device. Use with path to uniquely identify a virtual MFA device.
        """
        return pulumi.get(self, "virtual_mfa_device_name")

    @virtual_mfa_device_name.setter
    def virtual_mfa_device_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_mfa_device_name", value)


class VirtualMfaDevice(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_mfa_device_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        **Using certs on file:**

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.iam.VirtualMfaDevice("example", virtual_mfa_device_name="example")
        ```

        ## Import

        IAM Virtual MFA Devices can be imported using the `arn`, e.g.,

        ```sh
         $ pulumi import aws:iam/virtualMfaDevice:VirtualMfaDevice example arn:aws:iam::123456789012:mfa/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] path: The path for the virtual MFA device.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of resource tags for the virtual mfa device. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] virtual_mfa_device_name: The name of the virtual MFA device. Use with path to uniquely identify a virtual MFA device.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualMfaDeviceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        **Using certs on file:**

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.iam.VirtualMfaDevice("example", virtual_mfa_device_name="example")
        ```

        ## Import

        IAM Virtual MFA Devices can be imported using the `arn`, e.g.,

        ```sh
         $ pulumi import aws:iam/virtualMfaDevice:VirtualMfaDevice example arn:aws:iam::123456789012:mfa/example
        ```

        :param str resource_name: The name of the resource.
        :param VirtualMfaDeviceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualMfaDeviceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_mfa_device_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = VirtualMfaDeviceArgs.__new__(VirtualMfaDeviceArgs)

            __props__.__dict__["path"] = path
            __props__.__dict__["tags"] = tags
            if virtual_mfa_device_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_mfa_device_name'")
            __props__.__dict__["virtual_mfa_device_name"] = virtual_mfa_device_name
            __props__.__dict__["arn"] = None
            __props__.__dict__["base32_string_seed"] = None
            __props__.__dict__["qr_code_png"] = None
            __props__.__dict__["tags_all"] = None
        super(VirtualMfaDevice, __self__).__init__(
            'aws:iam/virtualMfaDevice:VirtualMfaDevice',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            base32_string_seed: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            qr_code_png: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            virtual_mfa_device_name: Optional[pulumi.Input[str]] = None) -> 'VirtualMfaDevice':
        """
        Get an existing VirtualMfaDevice resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) specifying the virtual mfa device.
        :param pulumi.Input[str] base32_string_seed: The base32 seed defined as specified in [RFC3548](https://tools.ietf.org/html/rfc3548.txt). The `base_32_string_seed` is base64-encoded.
        :param pulumi.Input[str] path: The path for the virtual MFA device.
        :param pulumi.Input[str] qr_code_png: A QR code PNG image that encodes `otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String` where `$virtualMFADeviceName` is one of the create call arguments. AccountName is the user name if set (otherwise, the account ID otherwise), and Base32String is the seed in base32 format.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of resource tags for the virtual mfa device. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        :param pulumi.Input[str] virtual_mfa_device_name: The name of the virtual MFA device. Use with path to uniquely identify a virtual MFA device.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VirtualMfaDeviceState.__new__(_VirtualMfaDeviceState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["base32_string_seed"] = base32_string_seed
        __props__.__dict__["path"] = path
        __props__.__dict__["qr_code_png"] = qr_code_png
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["virtual_mfa_device_name"] = virtual_mfa_device_name
        return VirtualMfaDevice(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) specifying the virtual mfa device.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="base32StringSeed")
    def base32_string_seed(self) -> pulumi.Output[str]:
        """
        The base32 seed defined as specified in [RFC3548](https://tools.ietf.org/html/rfc3548.txt). The `base_32_string_seed` is base64-encoded.
        """
        return pulumi.get(self, "base32_string_seed")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[Optional[str]]:
        """
        The path for the virtual MFA device.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="qrCodePng")
    def qr_code_png(self) -> pulumi.Output[str]:
        """
        A QR code PNG image that encodes `otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String` where `$virtualMFADeviceName` is one of the create call arguments. AccountName is the user name if set (otherwise, the account ID otherwise), and Base32String is the seed in base32 format.
        """
        return pulumi.get(self, "qr_code_png")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Map of resource tags for the virtual mfa device. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    @pulumi.getter(name="virtualMfaDeviceName")
    def virtual_mfa_device_name(self) -> pulumi.Output[str]:
        """
        The name of the virtual MFA device. Use with path to uniquely identify a virtual MFA device.
        """
        return pulumi.get(self, "virtual_mfa_device_name")

