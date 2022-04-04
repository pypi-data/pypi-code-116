# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetRoleResult',
    'AwaitableGetRoleResult',
    'get_role',
    'get_role_output',
]

@pulumi.output_type
class GetRoleResult:
    """
    A collection of values returned by getRole.
    """
    def __init__(__self__, arn=None, assume_role_policy=None, create_date=None, description=None, id=None, max_session_duration=None, name=None, path=None, permissions_boundary=None, tags=None, unique_id=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if assume_role_policy and not isinstance(assume_role_policy, str):
            raise TypeError("Expected argument 'assume_role_policy' to be a str")
        pulumi.set(__self__, "assume_role_policy", assume_role_policy)
        if create_date and not isinstance(create_date, str):
            raise TypeError("Expected argument 'create_date' to be a str")
        pulumi.set(__self__, "create_date", create_date)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_session_duration and not isinstance(max_session_duration, int):
            raise TypeError("Expected argument 'max_session_duration' to be a int")
        pulumi.set(__self__, "max_session_duration", max_session_duration)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        pulumi.set(__self__, "path", path)
        if permissions_boundary and not isinstance(permissions_boundary, str):
            raise TypeError("Expected argument 'permissions_boundary' to be a str")
        pulumi.set(__self__, "permissions_boundary", permissions_boundary)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if unique_id and not isinstance(unique_id, str):
            raise TypeError("Expected argument 'unique_id' to be a str")
        pulumi.set(__self__, "unique_id", unique_id)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) specifying the role.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="assumeRolePolicy")
    def assume_role_policy(self) -> str:
        """
        The policy document associated with the role.
        """
        return pulumi.get(self, "assume_role_policy")

    @property
    @pulumi.getter(name="createDate")
    def create_date(self) -> str:
        """
        Creation date of the role in RFC 3339 format.
        """
        return pulumi.get(self, "create_date")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description for the role.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maxSessionDuration")
    def max_session_duration(self) -> int:
        """
        Maximum session duration.
        """
        return pulumi.get(self, "max_session_duration")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        The path to the role.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(self) -> str:
        """
        The ARN of the policy that is used to set the permissions boundary for the role.
        """
        return pulumi.get(self, "permissions_boundary")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        The tags attached to the role.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> str:
        """
        The stable and unique string identifying the role.
        """
        return pulumi.get(self, "unique_id")


class AwaitableGetRoleResult(GetRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleResult(
            arn=self.arn,
            assume_role_policy=self.assume_role_policy,
            create_date=self.create_date,
            description=self.description,
            id=self.id,
            max_session_duration=self.max_session_duration,
            name=self.name,
            path=self.path,
            permissions_boundary=self.permissions_boundary,
            tags=self.tags,
            unique_id=self.unique_id)


def get_role(name: Optional[str] = None,
             tags: Optional[Mapping[str, str]] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoleResult:
    """
    This data source can be used to fetch information about a specific
    IAM role. By using this data source, you can reference IAM role
    properties without having to hard code ARNs as input.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.iam.get_role(name="an_example_role_name")
    ```


    :param str name: The friendly IAM role name to match.
    :param Mapping[str, str] tags: The tags attached to the role.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:iam/getRole:getRole', __args__, opts=opts, typ=GetRoleResult).value

    return AwaitableGetRoleResult(
        arn=__ret__.arn,
        assume_role_policy=__ret__.assume_role_policy,
        create_date=__ret__.create_date,
        description=__ret__.description,
        id=__ret__.id,
        max_session_duration=__ret__.max_session_duration,
        name=__ret__.name,
        path=__ret__.path,
        permissions_boundary=__ret__.permissions_boundary,
        tags=__ret__.tags,
        unique_id=__ret__.unique_id)


@_utilities.lift_output_func(get_role)
def get_role_output(name: Optional[pulumi.Input[str]] = None,
                    tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoleResult]:
    """
    This data source can be used to fetch information about a specific
    IAM role. By using this data source, you can reference IAM role
    properties without having to hard code ARNs as input.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.iam.get_role(name="an_example_role_name")
    ```


    :param str name: The friendly IAM role name to match.
    :param Mapping[str, str] tags: The tags attached to the role.
    """
    ...
