# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'CustomPluginLocation',
    'CustomPluginLocationS3',
]

@pulumi.output_type
class CustomPluginLocation(dict):
    def __init__(__self__, *,
                 s3: 'outputs.CustomPluginLocationS3'):
        """
        :param 'CustomPluginLocationS3Args' s3: Information of the plugin file stored in Amazon S3. See below.
        """
        pulumi.set(__self__, "s3", s3)

    @property
    @pulumi.getter
    def s3(self) -> 'outputs.CustomPluginLocationS3':
        """
        Information of the plugin file stored in Amazon S3. See below.
        """
        return pulumi.get(self, "s3")


@pulumi.output_type
class CustomPluginLocationS3(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bucketArn":
            suggest = "bucket_arn"
        elif key == "fileKey":
            suggest = "file_key"
        elif key == "objectVersion":
            suggest = "object_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomPluginLocationS3. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomPluginLocationS3.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomPluginLocationS3.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bucket_arn: str,
                 file_key: str,
                 object_version: Optional[str] = None):
        """
        :param str bucket_arn: The Amazon Resource Name (ARN) of an S3 bucket.
        :param str file_key: The file key for an object in an S3 bucket.
        :param str object_version: The version of an object in an S3 bucket.
        """
        pulumi.set(__self__, "bucket_arn", bucket_arn)
        pulumi.set(__self__, "file_key", file_key)
        if object_version is not None:
            pulumi.set(__self__, "object_version", object_version)

    @property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of an S3 bucket.
        """
        return pulumi.get(self, "bucket_arn")

    @property
    @pulumi.getter(name="fileKey")
    def file_key(self) -> str:
        """
        The file key for an object in an S3 bucket.
        """
        return pulumi.get(self, "file_key")

    @property
    @pulumi.getter(name="objectVersion")
    def object_version(self) -> Optional[str]:
        """
        The version of an object in an S3 bucket.
        """
        return pulumi.get(self, "object_version")


