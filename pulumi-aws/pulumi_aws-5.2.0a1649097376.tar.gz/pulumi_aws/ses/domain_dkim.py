# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DomainDkimArgs', 'DomainDkim']

@pulumi.input_type
class DomainDkimArgs:
    def __init__(__self__, *,
                 domain: pulumi.Input[str]):
        """
        The set of arguments for constructing a DomainDkim resource.
        :param pulumi.Input[str] domain: Verified domain name to generate DKIM tokens for.
        """
        pulumi.set(__self__, "domain", domain)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        Verified domain name to generate DKIM tokens for.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)


@pulumi.input_type
class _DomainDkimState:
    def __init__(__self__, *,
                 dkim_tokens: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 domain: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DomainDkim resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dkim_tokens: DKIM tokens generated by SES.
               These tokens should be used to create CNAME records used to verify SES Easy DKIM.
               See below for an example of how this might be achieved
               when the domain is hosted in Route 53 and managed by this provider.
               Find out more about verifying domains in Amazon SES
               in the [AWS SES docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html).
        :param pulumi.Input[str] domain: Verified domain name to generate DKIM tokens for.
        """
        if dkim_tokens is not None:
            pulumi.set(__self__, "dkim_tokens", dkim_tokens)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)

    @property
    @pulumi.getter(name="dkimTokens")
    def dkim_tokens(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        DKIM tokens generated by SES.
        These tokens should be used to create CNAME records used to verify SES Easy DKIM.
        See below for an example of how this might be achieved
        when the domain is hosted in Route 53 and managed by this provider.
        Find out more about verifying domains in Amazon SES
        in the [AWS SES docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html).
        """
        return pulumi.get(self, "dkim_tokens")

    @dkim_tokens.setter
    def dkim_tokens(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dkim_tokens", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        Verified domain name to generate DKIM tokens for.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)


class DomainDkim(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an SES domain DKIM generation resource.

        Domain ownership needs to be confirmed first using `ses.DomainIdentity` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_domain_identity = aws.ses.DomainIdentity("exampleDomainIdentity", domain="example.com")
        example_domain_dkim = aws.ses.DomainDkim("exampleDomainDkim", domain=example_domain_identity.domain)
        example_amazonses_dkim_record = []
        for range in [{"value": i} for i in range(0, 3)]:
            example_amazonses_dkim_record.append(aws.route53.Record(f"exampleAmazonsesDkimRecord-{range['value']}",
                zone_id="ABCDEFGHIJ123",
                name=example_domain_dkim.dkim_tokens[range["value"]].apply(lambda dkim_tokens: f"{dkim_tokens}._domainkey"),
                type="CNAME",
                ttl=600,
                records=[example_domain_dkim.dkim_tokens[range["value"]].apply(lambda dkim_tokens: f"{dkim_tokens}.dkim.amazonses.com")]))
        ```

        ## Import

        DKIM tokens can be imported using the `domain` attribute, e.g.,

        ```sh
         $ pulumi import aws:ses/domainDkim:DomainDkim example example.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain: Verified domain name to generate DKIM tokens for.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainDkimArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an SES domain DKIM generation resource.

        Domain ownership needs to be confirmed first using `ses.DomainIdentity` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_domain_identity = aws.ses.DomainIdentity("exampleDomainIdentity", domain="example.com")
        example_domain_dkim = aws.ses.DomainDkim("exampleDomainDkim", domain=example_domain_identity.domain)
        example_amazonses_dkim_record = []
        for range in [{"value": i} for i in range(0, 3)]:
            example_amazonses_dkim_record.append(aws.route53.Record(f"exampleAmazonsesDkimRecord-{range['value']}",
                zone_id="ABCDEFGHIJ123",
                name=example_domain_dkim.dkim_tokens[range["value"]].apply(lambda dkim_tokens: f"{dkim_tokens}._domainkey"),
                type="CNAME",
                ttl=600,
                records=[example_domain_dkim.dkim_tokens[range["value"]].apply(lambda dkim_tokens: f"{dkim_tokens}.dkim.amazonses.com")]))
        ```

        ## Import

        DKIM tokens can be imported using the `domain` attribute, e.g.,

        ```sh
         $ pulumi import aws:ses/domainDkim:DomainDkim example example.com
        ```

        :param str resource_name: The name of the resource.
        :param DomainDkimArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainDkimArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain: Optional[pulumi.Input[str]] = None,
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
            __props__ = DomainDkimArgs.__new__(DomainDkimArgs)

            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            __props__.__dict__["dkim_tokens"] = None
        super(DomainDkim, __self__).__init__(
            'aws:ses/domainDkim:DomainDkim',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dkim_tokens: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            domain: Optional[pulumi.Input[str]] = None) -> 'DomainDkim':
        """
        Get an existing DomainDkim resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dkim_tokens: DKIM tokens generated by SES.
               These tokens should be used to create CNAME records used to verify SES Easy DKIM.
               See below for an example of how this might be achieved
               when the domain is hosted in Route 53 and managed by this provider.
               Find out more about verifying domains in Amazon SES
               in the [AWS SES docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html).
        :param pulumi.Input[str] domain: Verified domain name to generate DKIM tokens for.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainDkimState.__new__(_DomainDkimState)

        __props__.__dict__["dkim_tokens"] = dkim_tokens
        __props__.__dict__["domain"] = domain
        return DomainDkim(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dkimTokens")
    def dkim_tokens(self) -> pulumi.Output[Sequence[str]]:
        """
        DKIM tokens generated by SES.
        These tokens should be used to create CNAME records used to verify SES Easy DKIM.
        See below for an example of how this might be achieved
        when the domain is hosted in Route 53 and managed by this provider.
        Find out more about verifying domains in Amazon SES
        in the [AWS SES docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html).
        """
        return pulumi.get(self, "dkim_tokens")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        Verified domain name to generate DKIM tokens for.
        """
        return pulumi.get(self, "domain")

