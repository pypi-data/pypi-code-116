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

__all__ = ['CloudFormationTypeArgs', 'CloudFormationType']

@pulumi.input_type
class CloudFormationTypeArgs:
    def __init__(__self__, *,
                 schema_handler_package: pulumi.Input[str],
                 type_name: pulumi.Input[str],
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 logging_config: Optional[pulumi.Input['CloudFormationTypeLoggingConfigArgs']] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CloudFormationType resource.
        :param pulumi.Input[str] schema_handler_package: URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register. Must begin with `s3://` or `https://`. For example, `s3://example-bucket/example-object`.
        :param pulumi.Input[str] type_name: CloudFormation Type name. For example, `ExampleCompany::ExampleService::ExampleResource`.
        :param pulumi.Input[str] execution_role_arn: Amazon Resource Name (ARN) of the IAM Role for CloudFormation to assume when invoking the extension. If your extension calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. When CloudFormation needs to invoke the extension handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the extension handler, thereby supplying your extension with the appropriate credentials.
        :param pulumi.Input['CloudFormationTypeLoggingConfigArgs'] logging_config: Configuration block containing logging configuration.
        :param pulumi.Input[str] type: CloudFormation Registry Type. For example, `RESOURCE` or `MODULE`.
        """
        pulumi.set(__self__, "schema_handler_package", schema_handler_package)
        pulumi.set(__self__, "type_name", type_name)
        if execution_role_arn is not None:
            pulumi.set(__self__, "execution_role_arn", execution_role_arn)
        if logging_config is not None:
            pulumi.set(__self__, "logging_config", logging_config)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="schemaHandlerPackage")
    def schema_handler_package(self) -> pulumi.Input[str]:
        """
        URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register. Must begin with `s3://` or `https://`. For example, `s3://example-bucket/example-object`.
        """
        return pulumi.get(self, "schema_handler_package")

    @schema_handler_package.setter
    def schema_handler_package(self, value: pulumi.Input[str]):
        pulumi.set(self, "schema_handler_package", value)

    @property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[str]:
        """
        CloudFormation Type name. For example, `ExampleCompany::ExampleService::ExampleResource`.
        """
        return pulumi.get(self, "type_name")

    @type_name.setter
    def type_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "type_name", value)

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of the IAM Role for CloudFormation to assume when invoking the extension. If your extension calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. When CloudFormation needs to invoke the extension handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the extension handler, thereby supplying your extension with the appropriate credentials.
        """
        return pulumi.get(self, "execution_role_arn")

    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "execution_role_arn", value)

    @property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input['CloudFormationTypeLoggingConfigArgs']]:
        """
        Configuration block containing logging configuration.
        """
        return pulumi.get(self, "logging_config")

    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input['CloudFormationTypeLoggingConfigArgs']]):
        pulumi.set(self, "logging_config", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        CloudFormation Registry Type. For example, `RESOURCE` or `MODULE`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _CloudFormationTypeState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 default_version_id: Optional[pulumi.Input[str]] = None,
                 deprecated_status: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 documentation_url: Optional[pulumi.Input[str]] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 is_default_version: Optional[pulumi.Input[bool]] = None,
                 logging_config: Optional[pulumi.Input['CloudFormationTypeLoggingConfigArgs']] = None,
                 provisioning_type: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 schema_handler_package: Optional[pulumi.Input[str]] = None,
                 source_url: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 type_arn: Optional[pulumi.Input[str]] = None,
                 type_name: Optional[pulumi.Input[str]] = None,
                 version_id: Optional[pulumi.Input[str]] = None,
                 visibility: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CloudFormationType resources.
        :param pulumi.Input[str] arn: (Optional) Amazon Resource Name (ARN) of the CloudFormation Type version. See also `type_arn`.
        :param pulumi.Input[str] default_version_id: Identifier of the CloudFormation Type default version.
        :param pulumi.Input[str] deprecated_status: Deprecation status of the version.
        :param pulumi.Input[str] description: Description of the version.
        :param pulumi.Input[str] documentation_url: URL of the documentation for the CloudFormation Type.
        :param pulumi.Input[str] execution_role_arn: Amazon Resource Name (ARN) of the IAM Role for CloudFormation to assume when invoking the extension. If your extension calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. When CloudFormation needs to invoke the extension handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the extension handler, thereby supplying your extension with the appropriate credentials.
        :param pulumi.Input[bool] is_default_version: Whether the CloudFormation Type version is the default version.
        :param pulumi.Input['CloudFormationTypeLoggingConfigArgs'] logging_config: Configuration block containing logging configuration.
        :param pulumi.Input[str] provisioning_type: Provisioning behavior of the CloudFormation Type.
        :param pulumi.Input[str] schema: JSON document of the CloudFormation Type schema.
        :param pulumi.Input[str] schema_handler_package: URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register. Must begin with `s3://` or `https://`. For example, `s3://example-bucket/example-object`.
        :param pulumi.Input[str] source_url: URL of the source code for the CloudFormation Type.
        :param pulumi.Input[str] type: CloudFormation Registry Type. For example, `RESOURCE` or `MODULE`.
        :param pulumi.Input[str] type_arn: (Optional) Amazon Resource Name (ARN) of the CloudFormation Type. See also `arn`.
        :param pulumi.Input[str] type_name: CloudFormation Type name. For example, `ExampleCompany::ExampleService::ExampleResource`.
        :param pulumi.Input[str] version_id: (Optional) Identifier of the CloudFormation Type version.
        :param pulumi.Input[str] visibility: Scope of the CloudFormation Type.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if default_version_id is not None:
            pulumi.set(__self__, "default_version_id", default_version_id)
        if deprecated_status is not None:
            pulumi.set(__self__, "deprecated_status", deprecated_status)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if documentation_url is not None:
            pulumi.set(__self__, "documentation_url", documentation_url)
        if execution_role_arn is not None:
            pulumi.set(__self__, "execution_role_arn", execution_role_arn)
        if is_default_version is not None:
            pulumi.set(__self__, "is_default_version", is_default_version)
        if logging_config is not None:
            pulumi.set(__self__, "logging_config", logging_config)
        if provisioning_type is not None:
            pulumi.set(__self__, "provisioning_type", provisioning_type)
        if schema is not None:
            pulumi.set(__self__, "schema", schema)
        if schema_handler_package is not None:
            pulumi.set(__self__, "schema_handler_package", schema_handler_package)
        if source_url is not None:
            pulumi.set(__self__, "source_url", source_url)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if type_arn is not None:
            pulumi.set(__self__, "type_arn", type_arn)
        if type_name is not None:
            pulumi.set(__self__, "type_name", type_name)
        if version_id is not None:
            pulumi.set(__self__, "version_id", version_id)
        if visibility is not None:
            pulumi.set(__self__, "visibility", visibility)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        (Optional) Amazon Resource Name (ARN) of the CloudFormation Type version. See also `type_arn`.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="defaultVersionId")
    def default_version_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the CloudFormation Type default version.
        """
        return pulumi.get(self, "default_version_id")

    @default_version_id.setter
    def default_version_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_version_id", value)

    @property
    @pulumi.getter(name="deprecatedStatus")
    def deprecated_status(self) -> Optional[pulumi.Input[str]]:
        """
        Deprecation status of the version.
        """
        return pulumi.get(self, "deprecated_status")

    @deprecated_status.setter
    def deprecated_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deprecated_status", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the version.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="documentationUrl")
    def documentation_url(self) -> Optional[pulumi.Input[str]]:
        """
        URL of the documentation for the CloudFormation Type.
        """
        return pulumi.get(self, "documentation_url")

    @documentation_url.setter
    def documentation_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "documentation_url", value)

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of the IAM Role for CloudFormation to assume when invoking the extension. If your extension calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. When CloudFormation needs to invoke the extension handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the extension handler, thereby supplying your extension with the appropriate credentials.
        """
        return pulumi.get(self, "execution_role_arn")

    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "execution_role_arn", value)

    @property
    @pulumi.getter(name="isDefaultVersion")
    def is_default_version(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the CloudFormation Type version is the default version.
        """
        return pulumi.get(self, "is_default_version")

    @is_default_version.setter
    def is_default_version(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_default_version", value)

    @property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input['CloudFormationTypeLoggingConfigArgs']]:
        """
        Configuration block containing logging configuration.
        """
        return pulumi.get(self, "logging_config")

    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input['CloudFormationTypeLoggingConfigArgs']]):
        pulumi.set(self, "logging_config", value)

    @property
    @pulumi.getter(name="provisioningType")
    def provisioning_type(self) -> Optional[pulumi.Input[str]]:
        """
        Provisioning behavior of the CloudFormation Type.
        """
        return pulumi.get(self, "provisioning_type")

    @provisioning_type.setter
    def provisioning_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_type", value)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[str]]:
        """
        JSON document of the CloudFormation Type schema.
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="schemaHandlerPackage")
    def schema_handler_package(self) -> Optional[pulumi.Input[str]]:
        """
        URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register. Must begin with `s3://` or `https://`. For example, `s3://example-bucket/example-object`.
        """
        return pulumi.get(self, "schema_handler_package")

    @schema_handler_package.setter
    def schema_handler_package(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_handler_package", value)

    @property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> Optional[pulumi.Input[str]]:
        """
        URL of the source code for the CloudFormation Type.
        """
        return pulumi.get(self, "source_url")

    @source_url.setter
    def source_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_url", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        CloudFormation Registry Type. For example, `RESOURCE` or `MODULE`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="typeArn")
    def type_arn(self) -> Optional[pulumi.Input[str]]:
        """
        (Optional) Amazon Resource Name (ARN) of the CloudFormation Type. See also `arn`.
        """
        return pulumi.get(self, "type_arn")

    @type_arn.setter
    def type_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type_arn", value)

    @property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[pulumi.Input[str]]:
        """
        CloudFormation Type name. For example, `ExampleCompany::ExampleService::ExampleResource`.
        """
        return pulumi.get(self, "type_name")

    @type_name.setter
    def type_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type_name", value)

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Optional) Identifier of the CloudFormation Type version.
        """
        return pulumi.get(self, "version_id")

    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_id", value)

    @property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[str]]:
        """
        Scope of the CloudFormation Type.
        """
        return pulumi.get(self, "visibility")

    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "visibility", value)


class CloudFormationType(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 logging_config: Optional[pulumi.Input[pulumi.InputType['CloudFormationTypeLoggingConfigArgs']]] = None,
                 schema_handler_package: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 type_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cloudformation.CloudFormationType("example",
            schema_handler_package=f"s3://{aws_s3_object['example']['bucket']}/{aws_s3_object['example']['key']}",
            type="RESOURCE",
            type_name="ExampleCompany::ExampleService::ExampleResource",
            logging_config=aws.cloudformation.CloudFormationTypeLoggingConfigArgs(
                log_group_name=aws_cloudwatch_log_group["example"]["name"],
                log_role_arn=aws_iam_role["example"]["arn"],
            ))
        ```

        ## Import

        `aws_cloudformation_type` can be imported with their type version Amazon Resource Name (ARN), e.g.,

        ```sh
         $ pulumi import aws:cloudformation/cloudFormationType:CloudFormationType example arn:aws:cloudformation:us-east-1:123456789012:type/resource/ExampleCompany-ExampleService-ExampleType/1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] execution_role_arn: Amazon Resource Name (ARN) of the IAM Role for CloudFormation to assume when invoking the extension. If your extension calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. When CloudFormation needs to invoke the extension handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the extension handler, thereby supplying your extension with the appropriate credentials.
        :param pulumi.Input[pulumi.InputType['CloudFormationTypeLoggingConfigArgs']] logging_config: Configuration block containing logging configuration.
        :param pulumi.Input[str] schema_handler_package: URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register. Must begin with `s3://` or `https://`. For example, `s3://example-bucket/example-object`.
        :param pulumi.Input[str] type: CloudFormation Registry Type. For example, `RESOURCE` or `MODULE`.
        :param pulumi.Input[str] type_name: CloudFormation Type name. For example, `ExampleCompany::ExampleService::ExampleResource`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudFormationTypeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cloudformation.CloudFormationType("example",
            schema_handler_package=f"s3://{aws_s3_object['example']['bucket']}/{aws_s3_object['example']['key']}",
            type="RESOURCE",
            type_name="ExampleCompany::ExampleService::ExampleResource",
            logging_config=aws.cloudformation.CloudFormationTypeLoggingConfigArgs(
                log_group_name=aws_cloudwatch_log_group["example"]["name"],
                log_role_arn=aws_iam_role["example"]["arn"],
            ))
        ```

        ## Import

        `aws_cloudformation_type` can be imported with their type version Amazon Resource Name (ARN), e.g.,

        ```sh
         $ pulumi import aws:cloudformation/cloudFormationType:CloudFormationType example arn:aws:cloudformation:us-east-1:123456789012:type/resource/ExampleCompany-ExampleService-ExampleType/1
        ```

        :param str resource_name: The name of the resource.
        :param CloudFormationTypeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudFormationTypeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 execution_role_arn: Optional[pulumi.Input[str]] = None,
                 logging_config: Optional[pulumi.Input[pulumi.InputType['CloudFormationTypeLoggingConfigArgs']]] = None,
                 schema_handler_package: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 type_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = CloudFormationTypeArgs.__new__(CloudFormationTypeArgs)

            __props__.__dict__["execution_role_arn"] = execution_role_arn
            __props__.__dict__["logging_config"] = logging_config
            if schema_handler_package is None and not opts.urn:
                raise TypeError("Missing required property 'schema_handler_package'")
            __props__.__dict__["schema_handler_package"] = schema_handler_package
            __props__.__dict__["type"] = type
            if type_name is None and not opts.urn:
                raise TypeError("Missing required property 'type_name'")
            __props__.__dict__["type_name"] = type_name
            __props__.__dict__["arn"] = None
            __props__.__dict__["default_version_id"] = None
            __props__.__dict__["deprecated_status"] = None
            __props__.__dict__["description"] = None
            __props__.__dict__["documentation_url"] = None
            __props__.__dict__["is_default_version"] = None
            __props__.__dict__["provisioning_type"] = None
            __props__.__dict__["schema"] = None
            __props__.__dict__["source_url"] = None
            __props__.__dict__["type_arn"] = None
            __props__.__dict__["version_id"] = None
            __props__.__dict__["visibility"] = None
        super(CloudFormationType, __self__).__init__(
            'aws:cloudformation/cloudFormationType:CloudFormationType',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            default_version_id: Optional[pulumi.Input[str]] = None,
            deprecated_status: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            documentation_url: Optional[pulumi.Input[str]] = None,
            execution_role_arn: Optional[pulumi.Input[str]] = None,
            is_default_version: Optional[pulumi.Input[bool]] = None,
            logging_config: Optional[pulumi.Input[pulumi.InputType['CloudFormationTypeLoggingConfigArgs']]] = None,
            provisioning_type: Optional[pulumi.Input[str]] = None,
            schema: Optional[pulumi.Input[str]] = None,
            schema_handler_package: Optional[pulumi.Input[str]] = None,
            source_url: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            type_arn: Optional[pulumi.Input[str]] = None,
            type_name: Optional[pulumi.Input[str]] = None,
            version_id: Optional[pulumi.Input[str]] = None,
            visibility: Optional[pulumi.Input[str]] = None) -> 'CloudFormationType':
        """
        Get an existing CloudFormationType resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: (Optional) Amazon Resource Name (ARN) of the CloudFormation Type version. See also `type_arn`.
        :param pulumi.Input[str] default_version_id: Identifier of the CloudFormation Type default version.
        :param pulumi.Input[str] deprecated_status: Deprecation status of the version.
        :param pulumi.Input[str] description: Description of the version.
        :param pulumi.Input[str] documentation_url: URL of the documentation for the CloudFormation Type.
        :param pulumi.Input[str] execution_role_arn: Amazon Resource Name (ARN) of the IAM Role for CloudFormation to assume when invoking the extension. If your extension calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. When CloudFormation needs to invoke the extension handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the extension handler, thereby supplying your extension with the appropriate credentials.
        :param pulumi.Input[bool] is_default_version: Whether the CloudFormation Type version is the default version.
        :param pulumi.Input[pulumi.InputType['CloudFormationTypeLoggingConfigArgs']] logging_config: Configuration block containing logging configuration.
        :param pulumi.Input[str] provisioning_type: Provisioning behavior of the CloudFormation Type.
        :param pulumi.Input[str] schema: JSON document of the CloudFormation Type schema.
        :param pulumi.Input[str] schema_handler_package: URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register. Must begin with `s3://` or `https://`. For example, `s3://example-bucket/example-object`.
        :param pulumi.Input[str] source_url: URL of the source code for the CloudFormation Type.
        :param pulumi.Input[str] type: CloudFormation Registry Type. For example, `RESOURCE` or `MODULE`.
        :param pulumi.Input[str] type_arn: (Optional) Amazon Resource Name (ARN) of the CloudFormation Type. See also `arn`.
        :param pulumi.Input[str] type_name: CloudFormation Type name. For example, `ExampleCompany::ExampleService::ExampleResource`.
        :param pulumi.Input[str] version_id: (Optional) Identifier of the CloudFormation Type version.
        :param pulumi.Input[str] visibility: Scope of the CloudFormation Type.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CloudFormationTypeState.__new__(_CloudFormationTypeState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["default_version_id"] = default_version_id
        __props__.__dict__["deprecated_status"] = deprecated_status
        __props__.__dict__["description"] = description
        __props__.__dict__["documentation_url"] = documentation_url
        __props__.__dict__["execution_role_arn"] = execution_role_arn
        __props__.__dict__["is_default_version"] = is_default_version
        __props__.__dict__["logging_config"] = logging_config
        __props__.__dict__["provisioning_type"] = provisioning_type
        __props__.__dict__["schema"] = schema
        __props__.__dict__["schema_handler_package"] = schema_handler_package
        __props__.__dict__["source_url"] = source_url
        __props__.__dict__["type"] = type
        __props__.__dict__["type_arn"] = type_arn
        __props__.__dict__["type_name"] = type_name
        __props__.__dict__["version_id"] = version_id
        __props__.__dict__["visibility"] = visibility
        return CloudFormationType(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        (Optional) Amazon Resource Name (ARN) of the CloudFormation Type version. See also `type_arn`.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="defaultVersionId")
    def default_version_id(self) -> pulumi.Output[str]:
        """
        Identifier of the CloudFormation Type default version.
        """
        return pulumi.get(self, "default_version_id")

    @property
    @pulumi.getter(name="deprecatedStatus")
    def deprecated_status(self) -> pulumi.Output[str]:
        """
        Deprecation status of the version.
        """
        return pulumi.get(self, "deprecated_status")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description of the version.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="documentationUrl")
    def documentation_url(self) -> pulumi.Output[str]:
        """
        URL of the documentation for the CloudFormation Type.
        """
        return pulumi.get(self, "documentation_url")

    @property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        Amazon Resource Name (ARN) of the IAM Role for CloudFormation to assume when invoking the extension. If your extension calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. When CloudFormation needs to invoke the extension handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the extension handler, thereby supplying your extension with the appropriate credentials.
        """
        return pulumi.get(self, "execution_role_arn")

    @property
    @pulumi.getter(name="isDefaultVersion")
    def is_default_version(self) -> pulumi.Output[bool]:
        """
        Whether the CloudFormation Type version is the default version.
        """
        return pulumi.get(self, "is_default_version")

    @property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> pulumi.Output[Optional['outputs.CloudFormationTypeLoggingConfig']]:
        """
        Configuration block containing logging configuration.
        """
        return pulumi.get(self, "logging_config")

    @property
    @pulumi.getter(name="provisioningType")
    def provisioning_type(self) -> pulumi.Output[str]:
        """
        Provisioning behavior of the CloudFormation Type.
        """
        return pulumi.get(self, "provisioning_type")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output[str]:
        """
        JSON document of the CloudFormation Type schema.
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="schemaHandlerPackage")
    def schema_handler_package(self) -> pulumi.Output[str]:
        """
        URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register. Must begin with `s3://` or `https://`. For example, `s3://example-bucket/example-object`.
        """
        return pulumi.get(self, "schema_handler_package")

    @property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> pulumi.Output[str]:
        """
        URL of the source code for the CloudFormation Type.
        """
        return pulumi.get(self, "source_url")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        CloudFormation Registry Type. For example, `RESOURCE` or `MODULE`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="typeArn")
    def type_arn(self) -> pulumi.Output[str]:
        """
        (Optional) Amazon Resource Name (ARN) of the CloudFormation Type. See also `arn`.
        """
        return pulumi.get(self, "type_arn")

    @property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Output[str]:
        """
        CloudFormation Type name. For example, `ExampleCompany::ExampleService::ExampleResource`.
        """
        return pulumi.get(self, "type_name")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[str]:
        """
        (Optional) Identifier of the CloudFormation Type version.
        """
        return pulumi.get(self, "version_id")

    @property
    @pulumi.getter
    def visibility(self) -> pulumi.Output[str]:
        """
        Scope of the CloudFormation Type.
        """
        return pulumi.get(self, "visibility")

