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

__all__ = ['AnalyticsConfigurationArgs', 'AnalyticsConfiguration']

@pulumi.input_type
class AnalyticsConfigurationArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 filter: Optional[pulumi.Input['AnalyticsConfigurationFilterArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_class_analysis: Optional[pulumi.Input['AnalyticsConfigurationStorageClassAnalysisArgs']] = None):
        """
        The set of arguments for constructing a AnalyticsConfiguration resource.
        :param pulumi.Input[str] bucket: The name of the bucket this analytics configuration is associated with.
        :param pulumi.Input['AnalyticsConfigurationFilterArgs'] filter: Object filtering that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).
        :param pulumi.Input[str] name: Unique identifier of the analytics configuration for the bucket.
        :param pulumi.Input['AnalyticsConfigurationStorageClassAnalysisArgs'] storage_class_analysis: Configuration for the analytics data export (documented below).
        """
        pulumi.set(__self__, "bucket", bucket)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if storage_class_analysis is not None:
            pulumi.set(__self__, "storage_class_analysis", storage_class_analysis)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        The name of the bucket this analytics configuration is associated with.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input['AnalyticsConfigurationFilterArgs']]:
        """
        Object filtering that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input['AnalyticsConfigurationFilterArgs']]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the analytics configuration for the bucket.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="storageClassAnalysis")
    def storage_class_analysis(self) -> Optional[pulumi.Input['AnalyticsConfigurationStorageClassAnalysisArgs']]:
        """
        Configuration for the analytics data export (documented below).
        """
        return pulumi.get(self, "storage_class_analysis")

    @storage_class_analysis.setter
    def storage_class_analysis(self, value: Optional[pulumi.Input['AnalyticsConfigurationStorageClassAnalysisArgs']]):
        pulumi.set(self, "storage_class_analysis", value)


@pulumi.input_type
class _AnalyticsConfigurationState:
    def __init__(__self__, *,
                 bucket: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input['AnalyticsConfigurationFilterArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_class_analysis: Optional[pulumi.Input['AnalyticsConfigurationStorageClassAnalysisArgs']] = None):
        """
        Input properties used for looking up and filtering AnalyticsConfiguration resources.
        :param pulumi.Input[str] bucket: The name of the bucket this analytics configuration is associated with.
        :param pulumi.Input['AnalyticsConfigurationFilterArgs'] filter: Object filtering that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).
        :param pulumi.Input[str] name: Unique identifier of the analytics configuration for the bucket.
        :param pulumi.Input['AnalyticsConfigurationStorageClassAnalysisArgs'] storage_class_analysis: Configuration for the analytics data export (documented below).
        """
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if storage_class_analysis is not None:
            pulumi.set(__self__, "storage_class_analysis", storage_class_analysis)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the bucket this analytics configuration is associated with.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input['AnalyticsConfigurationFilterArgs']]:
        """
        Object filtering that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input['AnalyticsConfigurationFilterArgs']]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the analytics configuration for the bucket.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="storageClassAnalysis")
    def storage_class_analysis(self) -> Optional[pulumi.Input['AnalyticsConfigurationStorageClassAnalysisArgs']]:
        """
        Configuration for the analytics data export (documented below).
        """
        return pulumi.get(self, "storage_class_analysis")

    @storage_class_analysis.setter
    def storage_class_analysis(self, value: Optional[pulumi.Input['AnalyticsConfigurationStorageClassAnalysisArgs']]):
        pulumi.set(self, "storage_class_analysis", value)


class AnalyticsConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[pulumi.InputType['AnalyticsConfigurationFilterArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_class_analysis: Optional[pulumi.Input[pulumi.InputType['AnalyticsConfigurationStorageClassAnalysisArgs']]] = None,
                 __props__=None):
        """
        Provides a S3 bucket [analytics configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html) resource.

        ## Example Usage
        ### Add analytics configuration for entire S3 bucket and export results to a second S3 bucket

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketV2("example")
        analytics = aws.s3.BucketV2("analytics")
        example_entire_bucket = aws.s3.AnalyticsConfiguration("example-entire-bucket",
            bucket=example.bucket,
            storage_class_analysis=aws.s3.AnalyticsConfigurationStorageClassAnalysisArgs(
                data_export=aws.s3.AnalyticsConfigurationStorageClassAnalysisDataExportArgs(
                    destination=aws.s3.AnalyticsConfigurationStorageClassAnalysisDataExportDestinationArgs(
                        s3_bucket_destination=aws.s3.AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationArgs(
                            bucket_arn=analytics.arn,
                        ),
                    ),
                ),
            ))
        ```
        ### Add analytics configuration with S3 object filter

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketV2("example")
        example_filtered = aws.s3.AnalyticsConfiguration("example-filtered",
            bucket=example.bucket,
            filter=aws.s3.AnalyticsConfigurationFilterArgs(
                prefix="documents/",
                tags={
                    "priority": "high",
                    "class": "blue",
                },
            ))
        ```

        ## Import

        S3 bucket analytics configurations can be imported using `bucket:analytics`, e.g.,

        ```sh
         $ pulumi import aws:s3/analyticsConfiguration:AnalyticsConfiguration my-bucket-entire-bucket my-bucket:EntireBucket
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket this analytics configuration is associated with.
        :param pulumi.Input[pulumi.InputType['AnalyticsConfigurationFilterArgs']] filter: Object filtering that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).
        :param pulumi.Input[str] name: Unique identifier of the analytics configuration for the bucket.
        :param pulumi.Input[pulumi.InputType['AnalyticsConfigurationStorageClassAnalysisArgs']] storage_class_analysis: Configuration for the analytics data export (documented below).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AnalyticsConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a S3 bucket [analytics configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/analytics-storage-class.html) resource.

        ## Example Usage
        ### Add analytics configuration for entire S3 bucket and export results to a second S3 bucket

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketV2("example")
        analytics = aws.s3.BucketV2("analytics")
        example_entire_bucket = aws.s3.AnalyticsConfiguration("example-entire-bucket",
            bucket=example.bucket,
            storage_class_analysis=aws.s3.AnalyticsConfigurationStorageClassAnalysisArgs(
                data_export=aws.s3.AnalyticsConfigurationStorageClassAnalysisDataExportArgs(
                    destination=aws.s3.AnalyticsConfigurationStorageClassAnalysisDataExportDestinationArgs(
                        s3_bucket_destination=aws.s3.AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationArgs(
                            bucket_arn=analytics.arn,
                        ),
                    ),
                ),
            ))
        ```
        ### Add analytics configuration with S3 object filter

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketV2("example")
        example_filtered = aws.s3.AnalyticsConfiguration("example-filtered",
            bucket=example.bucket,
            filter=aws.s3.AnalyticsConfigurationFilterArgs(
                prefix="documents/",
                tags={
                    "priority": "high",
                    "class": "blue",
                },
            ))
        ```

        ## Import

        S3 bucket analytics configurations can be imported using `bucket:analytics`, e.g.,

        ```sh
         $ pulumi import aws:s3/analyticsConfiguration:AnalyticsConfiguration my-bucket-entire-bucket my-bucket:EntireBucket
        ```

        :param str resource_name: The name of the resource.
        :param AnalyticsConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AnalyticsConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[pulumi.InputType['AnalyticsConfigurationFilterArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_class_analysis: Optional[pulumi.Input[pulumi.InputType['AnalyticsConfigurationStorageClassAnalysisArgs']]] = None,
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
            __props__ = AnalyticsConfigurationArgs.__new__(AnalyticsConfigurationArgs)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["filter"] = filter
            __props__.__dict__["name"] = name
            __props__.__dict__["storage_class_analysis"] = storage_class_analysis
        super(AnalyticsConfiguration, __self__).__init__(
            'aws:s3/analyticsConfiguration:AnalyticsConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            filter: Optional[pulumi.Input[pulumi.InputType['AnalyticsConfigurationFilterArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            storage_class_analysis: Optional[pulumi.Input[pulumi.InputType['AnalyticsConfigurationStorageClassAnalysisArgs']]] = None) -> 'AnalyticsConfiguration':
        """
        Get an existing AnalyticsConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket this analytics configuration is associated with.
        :param pulumi.Input[pulumi.InputType['AnalyticsConfigurationFilterArgs']] filter: Object filtering that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).
        :param pulumi.Input[str] name: Unique identifier of the analytics configuration for the bucket.
        :param pulumi.Input[pulumi.InputType['AnalyticsConfigurationStorageClassAnalysisArgs']] storage_class_analysis: Configuration for the analytics data export (documented below).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AnalyticsConfigurationState.__new__(_AnalyticsConfigurationState)

        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["filter"] = filter
        __props__.__dict__["name"] = name
        __props__.__dict__["storage_class_analysis"] = storage_class_analysis
        return AnalyticsConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        The name of the bucket this analytics configuration is associated with.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional['outputs.AnalyticsConfigurationFilter']]:
        """
        Object filtering that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unique identifier of the analytics configuration for the bucket.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageClassAnalysis")
    def storage_class_analysis(self) -> pulumi.Output[Optional['outputs.AnalyticsConfigurationStorageClassAnalysis']]:
        """
        Configuration for the analytics data export (documented below).
        """
        return pulumi.get(self, "storage_class_analysis")

