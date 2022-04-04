# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ConstraintArgs', 'Constraint']

@pulumi.input_type
class ConstraintArgs:
    def __init__(__self__, *,
                 parameters: pulumi.Input[str],
                 portfolio_id: pulumi.Input[str],
                 product_id: pulumi.Input[str],
                 type: pulumi.Input[str],
                 accept_language: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Constraint resource.
        :param pulumi.Input[str] parameters: Constraint parameters in JSON format. The syntax depends on the constraint type. See details below.
        :param pulumi.Input[str] portfolio_id: Portfolio identifier.
        :param pulumi.Input[str] product_id: Product identifier.
        :param pulumi.Input[str] type: Type of constraint. Valid values are `LAUNCH`, `NOTIFICATION`, `RESOURCE_UPDATE`, `STACKSET`, and `TEMPLATE`.
        :param pulumi.Input[str] accept_language: Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default value is `en`.
        :param pulumi.Input[str] description: Description of the constraint.
        """
        pulumi.set(__self__, "parameters", parameters)
        pulumi.set(__self__, "portfolio_id", portfolio_id)
        pulumi.set(__self__, "product_id", product_id)
        pulumi.set(__self__, "type", type)
        if accept_language is not None:
            pulumi.set(__self__, "accept_language", accept_language)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[str]:
        """
        Constraint parameters in JSON format. The syntax depends on the constraint type. See details below.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: pulumi.Input[str]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> pulumi.Input[str]:
        """
        Portfolio identifier.
        """
        return pulumi.get(self, "portfolio_id")

    @portfolio_id.setter
    def portfolio_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "portfolio_id", value)

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Input[str]:
        """
        Product identifier.
        """
        return pulumi.get(self, "product_id")

    @product_id.setter
    def product_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "product_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Type of constraint. Valid values are `LAUNCH`, `NOTIFICATION`, `RESOURCE_UPDATE`, `STACKSET`, and `TEMPLATE`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input[str]]:
        """
        Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default value is `en`.
        """
        return pulumi.get(self, "accept_language")

    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accept_language", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the constraint.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class _ConstraintState:
    def __init__(__self__, *,
                 accept_language: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[str]] = None,
                 portfolio_id: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Constraint resources.
        :param pulumi.Input[str] accept_language: Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default value is `en`.
        :param pulumi.Input[str] description: Description of the constraint.
        :param pulumi.Input[str] owner: Owner of the constraint.
        :param pulumi.Input[str] parameters: Constraint parameters in JSON format. The syntax depends on the constraint type. See details below.
        :param pulumi.Input[str] portfolio_id: Portfolio identifier.
        :param pulumi.Input[str] product_id: Product identifier.
        :param pulumi.Input[str] type: Type of constraint. Valid values are `LAUNCH`, `NOTIFICATION`, `RESOURCE_UPDATE`, `STACKSET`, and `TEMPLATE`.
        """
        if accept_language is not None:
            pulumi.set(__self__, "accept_language", accept_language)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if portfolio_id is not None:
            pulumi.set(__self__, "portfolio_id", portfolio_id)
        if product_id is not None:
            pulumi.set(__self__, "product_id", product_id)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input[str]]:
        """
        Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default value is `en`.
        """
        return pulumi.get(self, "accept_language")

    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accept_language", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the constraint.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        Owner of the constraint.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[str]]:
        """
        Constraint parameters in JSON format. The syntax depends on the constraint type. See details below.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> Optional[pulumi.Input[str]]:
        """
        Portfolio identifier.
        """
        return pulumi.get(self, "portfolio_id")

    @portfolio_id.setter
    def portfolio_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "portfolio_id", value)

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[pulumi.Input[str]]:
        """
        Product identifier.
        """
        return pulumi.get(self, "product_id")

    @product_id.setter
    def product_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of constraint. Valid values are `LAUNCH`, `NOTIFICATION`, `RESOURCE_UPDATE`, `STACKSET`, and `TEMPLATE`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Constraint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_language: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[str]] = None,
                 portfolio_id: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Service Catalog Constraint.

        > **NOTE:** This resource does not associate a Service Catalog product and portfolio. However, the product and portfolio must be associated (see the `servicecatalog.ProductPortfolioAssociation` resource) prior to creating a constraint or you will receive an error.

        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        example = aws.servicecatalog.Constraint("example",
            description="Back off, man. I'm a scientist.",
            portfolio_id=aws_servicecatalog_portfolio["example"]["id"],
            product_id=aws_servicecatalog_product["example"]["id"],
            type="LAUNCH",
            parameters=json.dumps({
                "RoleArn": "arn:aws:iam::123456789012:role/LaunchRole",
            }))
        ```

        ## Import

        `aws_servicecatalog_constraint` can be imported using the constraint ID, e.g.,

        ```sh
         $ pulumi import aws:servicecatalog/constraint:Constraint example cons-nmdkb6cgxfcrs
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accept_language: Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default value is `en`.
        :param pulumi.Input[str] description: Description of the constraint.
        :param pulumi.Input[str] parameters: Constraint parameters in JSON format. The syntax depends on the constraint type. See details below.
        :param pulumi.Input[str] portfolio_id: Portfolio identifier.
        :param pulumi.Input[str] product_id: Product identifier.
        :param pulumi.Input[str] type: Type of constraint. Valid values are `LAUNCH`, `NOTIFICATION`, `RESOURCE_UPDATE`, `STACKSET`, and `TEMPLATE`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConstraintArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Service Catalog Constraint.

        > **NOTE:** This resource does not associate a Service Catalog product and portfolio. However, the product and portfolio must be associated (see the `servicecatalog.ProductPortfolioAssociation` resource) prior to creating a constraint or you will receive an error.

        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        example = aws.servicecatalog.Constraint("example",
            description="Back off, man. I'm a scientist.",
            portfolio_id=aws_servicecatalog_portfolio["example"]["id"],
            product_id=aws_servicecatalog_product["example"]["id"],
            type="LAUNCH",
            parameters=json.dumps({
                "RoleArn": "arn:aws:iam::123456789012:role/LaunchRole",
            }))
        ```

        ## Import

        `aws_servicecatalog_constraint` can be imported using the constraint ID, e.g.,

        ```sh
         $ pulumi import aws:servicecatalog/constraint:Constraint example cons-nmdkb6cgxfcrs
        ```

        :param str resource_name: The name of the resource.
        :param ConstraintArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConstraintArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_language: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[str]] = None,
                 portfolio_id: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
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
            __props__ = ConstraintArgs.__new__(ConstraintArgs)

            __props__.__dict__["accept_language"] = accept_language
            __props__.__dict__["description"] = description
            if parameters is None and not opts.urn:
                raise TypeError("Missing required property 'parameters'")
            __props__.__dict__["parameters"] = parameters
            if portfolio_id is None and not opts.urn:
                raise TypeError("Missing required property 'portfolio_id'")
            __props__.__dict__["portfolio_id"] = portfolio_id
            if product_id is None and not opts.urn:
                raise TypeError("Missing required property 'product_id'")
            __props__.__dict__["product_id"] = product_id
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["owner"] = None
            __props__.__dict__["status"] = None
        super(Constraint, __self__).__init__(
            'aws:servicecatalog/constraint:Constraint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accept_language: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[str]] = None,
            portfolio_id: Optional[pulumi.Input[str]] = None,
            product_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Constraint':
        """
        Get an existing Constraint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accept_language: Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default value is `en`.
        :param pulumi.Input[str] description: Description of the constraint.
        :param pulumi.Input[str] owner: Owner of the constraint.
        :param pulumi.Input[str] parameters: Constraint parameters in JSON format. The syntax depends on the constraint type. See details below.
        :param pulumi.Input[str] portfolio_id: Portfolio identifier.
        :param pulumi.Input[str] product_id: Product identifier.
        :param pulumi.Input[str] type: Type of constraint. Valid values are `LAUNCH`, `NOTIFICATION`, `RESOURCE_UPDATE`, `STACKSET`, and `TEMPLATE`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConstraintState.__new__(_ConstraintState)

        __props__.__dict__["accept_language"] = accept_language
        __props__.__dict__["description"] = description
        __props__.__dict__["owner"] = owner
        __props__.__dict__["parameters"] = parameters
        __props__.__dict__["portfolio_id"] = portfolio_id
        __props__.__dict__["product_id"] = product_id
        __props__.__dict__["status"] = status
        __props__.__dict__["type"] = type
        return Constraint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> pulumi.Output[Optional[str]]:
        """
        Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default value is `en`.
        """
        return pulumi.get(self, "accept_language")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description of the constraint.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        Owner of the constraint.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[str]:
        """
        Constraint parameters in JSON format. The syntax depends on the constraint type. See details below.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> pulumi.Output[str]:
        """
        Portfolio identifier.
        """
        return pulumi.get(self, "portfolio_id")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Output[str]:
        """
        Product identifier.
        """
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of constraint. Valid values are `LAUNCH`, `NOTIFICATION`, `RESOURCE_UPDATE`, `STACKSET`, and `TEMPLATE`.
        """
        return pulumi.get(self, "type")

