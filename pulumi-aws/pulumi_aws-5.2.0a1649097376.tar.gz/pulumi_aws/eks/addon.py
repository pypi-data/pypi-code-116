# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AddonArgs', 'Addon']

@pulumi.input_type
class AddonArgs:
    def __init__(__self__, *,
                 addon_name: pulumi.Input[str],
                 cluster_name: pulumi.Input[str],
                 addon_version: Optional[pulumi.Input[str]] = None,
                 resolve_conflicts: Optional[pulumi.Input[str]] = None,
                 service_account_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Addon resource.
        :param pulumi.Input[str] addon_name: Name of the EKS add-on. The name must match one of
               the names returned by [list-addon](https://docs.aws.amazon.com/cli/latest/reference/eks/list-addons.html).
        :param pulumi.Input[str] cluster_name: Name of the EKS Cluster. Must be between 1-100 characters in length. Must begin with an alphanumeric character, and must only contain alphanumeric characters, dashes and underscores (`^[0-9A-Za-z][A-Za-z0-9\-_]+$`).
        :param pulumi.Input[str] addon_version: The version of the EKS add-on. The version must
               match one of the versions returned by [describe-addon-versions](https://docs.aws.amazon.com/cli/latest/reference/eks/describe-addon-versions.html).
        :param pulumi.Input[str] resolve_conflicts: Define how to resolve parameter value conflicts
               when migrating an existing add-on to an Amazon EKS add-on or when applying
               version updates to the add-on. Valid values are `NONE` and `OVERWRITE`.
        :param pulumi.Input[str] service_account_role_arn: The Amazon Resource Name (ARN) of an
               existing IAM role to bind to the add-on's service account. The role must be
               assigned the IAM permissions required by the add-on. If you don't specify
               an existing IAM role, then the add-on uses the permissions assigned to the node
               IAM role. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html)
               in the Amazon EKS User Guide.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "addon_name", addon_name)
        pulumi.set(__self__, "cluster_name", cluster_name)
        if addon_version is not None:
            pulumi.set(__self__, "addon_version", addon_version)
        if resolve_conflicts is not None:
            pulumi.set(__self__, "resolve_conflicts", resolve_conflicts)
        if service_account_role_arn is not None:
            pulumi.set(__self__, "service_account_role_arn", service_account_role_arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="addonName")
    def addon_name(self) -> pulumi.Input[str]:
        """
        Name of the EKS add-on. The name must match one of
        the names returned by [list-addon](https://docs.aws.amazon.com/cli/latest/reference/eks/list-addons.html).
        """
        return pulumi.get(self, "addon_name")

    @addon_name.setter
    def addon_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "addon_name", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        Name of the EKS Cluster. Must be between 1-100 characters in length. Must begin with an alphanumeric character, and must only contain alphanumeric characters, dashes and underscores (`^[0-9A-Za-z][A-Za-z0-9\-_]+$`).
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="addonVersion")
    def addon_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the EKS add-on. The version must
        match one of the versions returned by [describe-addon-versions](https://docs.aws.amazon.com/cli/latest/reference/eks/describe-addon-versions.html).
        """
        return pulumi.get(self, "addon_version")

    @addon_version.setter
    def addon_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "addon_version", value)

    @property
    @pulumi.getter(name="resolveConflicts")
    def resolve_conflicts(self) -> Optional[pulumi.Input[str]]:
        """
        Define how to resolve parameter value conflicts
        when migrating an existing add-on to an Amazon EKS add-on or when applying
        version updates to the add-on. Valid values are `NONE` and `OVERWRITE`.
        """
        return pulumi.get(self, "resolve_conflicts")

    @resolve_conflicts.setter
    def resolve_conflicts(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resolve_conflicts", value)

    @property
    @pulumi.getter(name="serviceAccountRoleArn")
    def service_account_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of an
        existing IAM role to bind to the add-on's service account. The role must be
        assigned the IAM permissions required by the add-on. If you don't specify
        an existing IAM role, then the add-on uses the permissions assigned to the node
        IAM role. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html)
        in the Amazon EKS User Guide.
        """
        return pulumi.get(self, "service_account_role_arn")

    @service_account_role_arn.setter
    def service_account_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_role_arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _AddonState:
    def __init__(__self__, *,
                 addon_name: Optional[pulumi.Input[str]] = None,
                 addon_version: Optional[pulumi.Input[str]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 modified_at: Optional[pulumi.Input[str]] = None,
                 resolve_conflicts: Optional[pulumi.Input[str]] = None,
                 service_account_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Addon resources.
        :param pulumi.Input[str] addon_name: Name of the EKS add-on. The name must match one of
               the names returned by [list-addon](https://docs.aws.amazon.com/cli/latest/reference/eks/list-addons.html).
        :param pulumi.Input[str] addon_version: The version of the EKS add-on. The version must
               match one of the versions returned by [describe-addon-versions](https://docs.aws.amazon.com/cli/latest/reference/eks/describe-addon-versions.html).
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the EKS add-on.
        :param pulumi.Input[str] cluster_name: Name of the EKS Cluster. Must be between 1-100 characters in length. Must begin with an alphanumeric character, and must only contain alphanumeric characters, dashes and underscores (`^[0-9A-Za-z][A-Za-z0-9\-_]+$`).
        :param pulumi.Input[str] created_at: Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the EKS add-on was created.
        :param pulumi.Input[str] modified_at: Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the EKS add-on was updated.
        :param pulumi.Input[str] resolve_conflicts: Define how to resolve parameter value conflicts
               when migrating an existing add-on to an Amazon EKS add-on or when applying
               version updates to the add-on. Valid values are `NONE` and `OVERWRITE`.
        :param pulumi.Input[str] service_account_role_arn: The Amazon Resource Name (ARN) of an
               existing IAM role to bind to the add-on's service account. The role must be
               assigned the IAM permissions required by the add-on. If you don't specify
               an existing IAM role, then the add-on uses the permissions assigned to the node
               IAM role. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html)
               in the Amazon EKS User Guide.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: (Optional) Key-value map of resource tags, including those inherited from the provider .
        """
        if addon_name is not None:
            pulumi.set(__self__, "addon_name", addon_name)
        if addon_version is not None:
            pulumi.set(__self__, "addon_version", addon_version)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if modified_at is not None:
            pulumi.set(__self__, "modified_at", modified_at)
        if resolve_conflicts is not None:
            pulumi.set(__self__, "resolve_conflicts", resolve_conflicts)
        if service_account_role_arn is not None:
            pulumi.set(__self__, "service_account_role_arn", service_account_role_arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter(name="addonName")
    def addon_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the EKS add-on. The name must match one of
        the names returned by [list-addon](https://docs.aws.amazon.com/cli/latest/reference/eks/list-addons.html).
        """
        return pulumi.get(self, "addon_name")

    @addon_name.setter
    def addon_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "addon_name", value)

    @property
    @pulumi.getter(name="addonVersion")
    def addon_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the EKS add-on. The version must
        match one of the versions returned by [describe-addon-versions](https://docs.aws.amazon.com/cli/latest/reference/eks/describe-addon-versions.html).
        """
        return pulumi.get(self, "addon_version")

    @addon_version.setter
    def addon_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "addon_version", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of the EKS add-on.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the EKS Cluster. Must be between 1-100 characters in length. Must begin with an alphanumeric character, and must only contain alphanumeric characters, dashes and underscores (`^[0-9A-Za-z][A-Za-z0-9\-_]+$`).
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the EKS add-on was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the EKS add-on was updated.
        """
        return pulumi.get(self, "modified_at")

    @modified_at.setter
    def modified_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modified_at", value)

    @property
    @pulumi.getter(name="resolveConflicts")
    def resolve_conflicts(self) -> Optional[pulumi.Input[str]]:
        """
        Define how to resolve parameter value conflicts
        when migrating an existing add-on to an Amazon EKS add-on or when applying
        version updates to the add-on. Valid values are `NONE` and `OVERWRITE`.
        """
        return pulumi.get(self, "resolve_conflicts")

    @resolve_conflicts.setter
    def resolve_conflicts(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resolve_conflicts", value)

    @property
    @pulumi.getter(name="serviceAccountRoleArn")
    def service_account_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of an
        existing IAM role to bind to the add-on's service account. The role must be
        assigned the IAM permissions required by the add-on. If you don't specify
        an existing IAM role, then the add-on uses the permissions assigned to the node
        IAM role. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html)
        in the Amazon EKS User Guide.
        """
        return pulumi.get(self, "service_account_role_arn")

    @service_account_role_arn.setter
    def service_account_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_role_arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        (Optional) Key-value map of resource tags, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class Addon(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 addon_name: Optional[pulumi.Input[str]] = None,
                 addon_version: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 resolve_conflicts: Optional[pulumi.Input[str]] = None,
                 service_account_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages an EKS add-on.

        > **Note:** Amazon EKS add-on can only be used with Amazon EKS Clusters
        running version 1.18 with platform version eks.3 or later
        because add-ons rely on the Server-side Apply Kubernetes feature,
        which is only available in Kubernetes 1.18 and later.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.eks.Addon("example",
            cluster_name=aws_eks_cluster["example"]["name"],
            addon_name="vpc-cni")
        ```

        ## Import

        EKS add-on can be imported using the `cluster_name` and `addon_name` separated by a colon (`:`), e.g.,

        ```sh
         $ pulumi import aws:eks/addon:Addon my_eks_addon my_cluster_name:my_addon_name
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] addon_name: Name of the EKS add-on. The name must match one of
               the names returned by [list-addon](https://docs.aws.amazon.com/cli/latest/reference/eks/list-addons.html).
        :param pulumi.Input[str] addon_version: The version of the EKS add-on. The version must
               match one of the versions returned by [describe-addon-versions](https://docs.aws.amazon.com/cli/latest/reference/eks/describe-addon-versions.html).
        :param pulumi.Input[str] cluster_name: Name of the EKS Cluster. Must be between 1-100 characters in length. Must begin with an alphanumeric character, and must only contain alphanumeric characters, dashes and underscores (`^[0-9A-Za-z][A-Za-z0-9\-_]+$`).
        :param pulumi.Input[str] resolve_conflicts: Define how to resolve parameter value conflicts
               when migrating an existing add-on to an Amazon EKS add-on or when applying
               version updates to the add-on. Valid values are `NONE` and `OVERWRITE`.
        :param pulumi.Input[str] service_account_role_arn: The Amazon Resource Name (ARN) of an
               existing IAM role to bind to the add-on's service account. The role must be
               assigned the IAM permissions required by the add-on. If you don't specify
               an existing IAM role, then the add-on uses the permissions assigned to the node
               IAM role. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html)
               in the Amazon EKS User Guide.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AddonArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an EKS add-on.

        > **Note:** Amazon EKS add-on can only be used with Amazon EKS Clusters
        running version 1.18 with platform version eks.3 or later
        because add-ons rely on the Server-side Apply Kubernetes feature,
        which is only available in Kubernetes 1.18 and later.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.eks.Addon("example",
            cluster_name=aws_eks_cluster["example"]["name"],
            addon_name="vpc-cni")
        ```

        ## Import

        EKS add-on can be imported using the `cluster_name` and `addon_name` separated by a colon (`:`), e.g.,

        ```sh
         $ pulumi import aws:eks/addon:Addon my_eks_addon my_cluster_name:my_addon_name
        ```

        :param str resource_name: The name of the resource.
        :param AddonArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AddonArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 addon_name: Optional[pulumi.Input[str]] = None,
                 addon_version: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 resolve_conflicts: Optional[pulumi.Input[str]] = None,
                 service_account_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = AddonArgs.__new__(AddonArgs)

            if addon_name is None and not opts.urn:
                raise TypeError("Missing required property 'addon_name'")
            __props__.__dict__["addon_name"] = addon_name
            __props__.__dict__["addon_version"] = addon_version
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["resolve_conflicts"] = resolve_conflicts
            __props__.__dict__["service_account_role_arn"] = service_account_role_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["modified_at"] = None
            __props__.__dict__["tags_all"] = None
        super(Addon, __self__).__init__(
            'aws:eks/addon:Addon',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            addon_name: Optional[pulumi.Input[str]] = None,
            addon_version: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            cluster_name: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            modified_at: Optional[pulumi.Input[str]] = None,
            resolve_conflicts: Optional[pulumi.Input[str]] = None,
            service_account_role_arn: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Addon':
        """
        Get an existing Addon resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] addon_name: Name of the EKS add-on. The name must match one of
               the names returned by [list-addon](https://docs.aws.amazon.com/cli/latest/reference/eks/list-addons.html).
        :param pulumi.Input[str] addon_version: The version of the EKS add-on. The version must
               match one of the versions returned by [describe-addon-versions](https://docs.aws.amazon.com/cli/latest/reference/eks/describe-addon-versions.html).
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the EKS add-on.
        :param pulumi.Input[str] cluster_name: Name of the EKS Cluster. Must be between 1-100 characters in length. Must begin with an alphanumeric character, and must only contain alphanumeric characters, dashes and underscores (`^[0-9A-Za-z][A-Za-z0-9\-_]+$`).
        :param pulumi.Input[str] created_at: Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the EKS add-on was created.
        :param pulumi.Input[str] modified_at: Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the EKS add-on was updated.
        :param pulumi.Input[str] resolve_conflicts: Define how to resolve parameter value conflicts
               when migrating an existing add-on to an Amazon EKS add-on or when applying
               version updates to the add-on. Valid values are `NONE` and `OVERWRITE`.
        :param pulumi.Input[str] service_account_role_arn: The Amazon Resource Name (ARN) of an
               existing IAM role to bind to the add-on's service account. The role must be
               assigned the IAM permissions required by the add-on. If you don't specify
               an existing IAM role, then the add-on uses the permissions assigned to the node
               IAM role. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html)
               in the Amazon EKS User Guide.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: (Optional) Key-value map of resource tags, including those inherited from the provider .
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AddonState.__new__(_AddonState)

        __props__.__dict__["addon_name"] = addon_name
        __props__.__dict__["addon_version"] = addon_version
        __props__.__dict__["arn"] = arn
        __props__.__dict__["cluster_name"] = cluster_name
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["modified_at"] = modified_at
        __props__.__dict__["resolve_conflicts"] = resolve_conflicts
        __props__.__dict__["service_account_role_arn"] = service_account_role_arn
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return Addon(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addonName")
    def addon_name(self) -> pulumi.Output[str]:
        """
        Name of the EKS add-on. The name must match one of
        the names returned by [list-addon](https://docs.aws.amazon.com/cli/latest/reference/eks/list-addons.html).
        """
        return pulumi.get(self, "addon_name")

    @property
    @pulumi.getter(name="addonVersion")
    def addon_version(self) -> pulumi.Output[str]:
        """
        The version of the EKS add-on. The version must
        match one of the versions returned by [describe-addon-versions](https://docs.aws.amazon.com/cli/latest/reference/eks/describe-addon-versions.html).
        """
        return pulumi.get(self, "addon_version")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the EKS add-on.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        Name of the EKS Cluster. Must be between 1-100 characters in length. Must begin with an alphanumeric character, and must only contain alphanumeric characters, dashes and underscores (`^[0-9A-Za-z][A-Za-z0-9\-_]+$`).
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the EKS add-on was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> pulumi.Output[str]:
        """
        Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the EKS add-on was updated.
        """
        return pulumi.get(self, "modified_at")

    @property
    @pulumi.getter(name="resolveConflicts")
    def resolve_conflicts(self) -> pulumi.Output[Optional[str]]:
        """
        Define how to resolve parameter value conflicts
        when migrating an existing add-on to an Amazon EKS add-on or when applying
        version updates to the add-on. Valid values are `NONE` and `OVERWRITE`.
        """
        return pulumi.get(self, "resolve_conflicts")

    @property
    @pulumi.getter(name="serviceAccountRoleArn")
    def service_account_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of an
        existing IAM role to bind to the add-on's service account. The role must be
        assigned the IAM permissions required by the add-on. If you don't specify
        an existing IAM role, then the add-on uses the permissions assigned to the node
        IAM role. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html)
        in the Amazon EKS User Guide.
        """
        return pulumi.get(self, "service_account_role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        (Optional) Key-value map of resource tags, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

