"""
Autogenerated state module using `pop-create-idem <https://gitlab.com/saltstack/pop/pop-create-idem>`__

hub.exec.boto3.client.ec2.create_vpc
hub.exec.boto3.client.ec2.delete_vpc
hub.exec.boto3.client.ec2.describe_vpcs
resource = hub.tool.boto3.resource.create(ctx, "ec2", "Vpc", name)
hub.tool.boto3.resource.exec(resource, associate_dhcp_options, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, attach_classic_link_instance, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, attach_internet_gateway, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, create_network_acl, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, create_route_table, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, create_security_group, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, create_subnet, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, create_tags, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, delete, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, describe_attribute, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, detach_classic_link_instance, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, detach_internet_gateway, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, disable_classic_link, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, enable_classic_link, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, modify_attribute, *args, **kwargs)
hub.tool.boto3.resource.exec(resource, request_vpc_peering_connection, *args, **kwargs)
"""
import copy
from typing import Any
from typing import Dict
from typing import List

__contracts__ = ["resource"]


async def present(
    hub,
    ctx,
    name: str,
    resource_id: str = None,
    cidr_block_association_set: List = None,
    ipv6_cidr_block_association_set: List = None,
    instance_tenancy: str = None,
    tags: List = None,
    enable_dns_hostnames: bool = None,
    enable_dns_support: bool = None,
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Creates a VPC with the specified IPv4 CIDR block. The smallest VPC you can create uses a /28 netmask (16 IPv4
    addresses), and the largest uses a /16 netmask (65,536 IPv4 addresses). For more information about how large to
    make your VPC, see Your VPC and subnets in the Amazon Virtual Private Cloud User Guide. You can optionally
    request an IPv6 CIDR block for the VPC. You can request an Amazon-provided IPv6 CIDR block from Amazon's pool of
    IPv6 addresses, or an IPv6 CIDR block from an IPv6 address pool that you provisioned through bring your own IP
    addresses (BYOIP). By default, each instance you launch in the VPC has the default DHCP options, which include
    only a default DNS server that we provide (AmazonProvidedDNS). For more information, see DHCP options sets in
    the Amazon Virtual Private Cloud User Guide. You can specify the instance tenancy value for the VPC when you
    create it. You can't change this value for the VPC after you create it. For more information, see Dedicated
    Instances in the Amazon Elastic Compute Cloud User Guide.

    Args:
        name(Text): An Idem name of the resource.
        resource_id(Text): AWS VPC id to identify the resource
        cidr_block_association_set(List, optional): Information about the IPv4 CIDR blocks associated with the VPC.
            Defaults to None.
            * CidrBlock (string) -- An IPv4 CIDR block to associate with the VPC.
            * Ipv4IpamPoolId (string) -- Associate a CIDR allocated from an IPv4 IPAM pool to a VPC.
            * Ipv4NetmaskLength (integer) -- The netmask length of the IPv4 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool.
        ipv6_cidr_block_association_set(List, optional): Information about the IPv6 CIDR blocks associated with the VPC.
            Defaults to None.
            * Ipv6CidrBlock (string) -- An IPv6 CIDR block from the IPv6 address pool. You must also specify Ipv6Pool in the request.
            * Ipv6IpamPoolId (string) -- Associates a CIDR allocated from an IPv6 IPAM pool to a VPC.
            * Ipv6NetmaskLength (integer) -- The netmask length of the IPv6 CIDR you would like to associate from an
             Amazon VPC IP Address Manager (IPAM) pool.
            * Ipv6CidrBlockNetworkBorderGroup (string) -- The name of the location from which we advertise the IPV6 CIDR
             block. Use this parameter to limit the CIDR block to this location. You must set AmazonProvidedIpv6CidrBlock
              to true to use this parameter. You can have one IPv6 CIDR block association per network border group.
            * AmazonProvidedIpv6CidrBlock (boolean) -- Requests an Amazon-provided IPv6 CIDR block with a /56 prefix
             length for the VPC. You cannot specify the range of IPv6 addresses, or the size of the CIDR block.
        instance_tenancy(Text, optional): The tenancy options for instances launched into the VPC. For default, instances are launched
            with shared tenancy by default. You can launch instances with any tenancy into a shared tenancy
            VPC. For dedicated, instances are launched as dedicated tenancy instances by default. You can
            only launch instances with a tenancy of dedicated or host into a dedicated tenancy VPC.
            Important: The host value cannot be used with this parameter. Use the default or dedicated
            values only. Default: default. Defaults to None.
        tags(List, optional): The tags to assign to the VPC. Defaults to None.
            * Key (string) -- The key of the tag. Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws: .
            * Value (string) -- The value of the tag. Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
        enable_dns_hostnames(bool, optional): Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances
            in the VPC get DNS hostnames; otherwise, they do not. You cannot modify the DNS resolution and DNS hostnames attributes in the same request.
            Use separate requests for each attribute. You can only enable DNS hostnames if you've enabled DNS support.
        enable_dns_support(bool, optional): Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided
            DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled,
            the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled. You cannot modify the DNS resolution
            and DNS hostnames attributes in the same request. Use separate requests for each attribute.

    Request Syntax:
        [vpc-resource-id]:
          aws.ec2.vpc.present:
          - resource_id: 'string'
          - cidr_block_association_set:
            - CidrBlock: 'string'
              Ipv4IpamPoolId: 'string'
              Ipv4NetmaskLength: 'integer'
          - ipv6_cidr_block_association_set:
            - Ipv6CidrBlock: 'string'
              Ipv6IpamPoolId: 'string'
              Ipv6NetmaskLength: 'integer'
              Ipv6CidrBlockNetworkBorderGroup: 'string'
              AmazonProvidedIpv6CidrBlock: True|False
          - instance_tenancy: 'default'|'dedicated'|'host'
          - tags:
            - Key: 'string'
              Value: 'string'
          - enable_dns_support: 'Boolean'
          - enable_dns_hostnames: 'Boolean'

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            vpc-01234672f3336db8:
              aws.ec2.vpc.present:
              - cidr_block_association_set:
                - CidrBlock: 10.1.150.0/28
              - instance_tenancy: default
              - enable_dns_support: True
              - enable_dns_hostnames: False
              - tags:
                - Key: Name
                  Value: vpc-name
                - Key: vpc-tag-key-2
                  Value: vpc-tag-value-2
    """
    result = dict(comment=(), old_state=None, new_state=None, name=name, result=True)
    before = None
    resource_updated = False
    if resource_id:
        resource = hub.tool.boto3.resource.create(ctx, "ec2", "Vpc", resource_id)
        before = await hub.tool.boto3.resource.describe(resource)
    if before:
        try:
            result[
                "old_state"
            ] = await hub.tool.aws.ec2.conversion_utils.convert_raw_vpc_to_present(
                ctx, raw_resource=before, idem_resource_name=name
            )
            plan_state = copy.deepcopy(result["old_state"])
            # Update cidr blocks
            update_ret = await hub.exec.aws.ec2.vpc.update_cidr_blocks(
                ctx=ctx,
                vpc_id=result["old_state"]["resource_id"],
                old_ipv4_cidr_blocks=result["old_state"].get(
                    "cidr_block_association_set", []
                ),
                old_ipv6_cidr_blocks=result["old_state"].get(
                    "ipv6_cidr_block_association_set", []
                ),
                new_ipv4_cidr_blocks=cidr_block_association_set,
                new_ipv6_cidr_blocks=ipv6_cidr_block_association_set,
            )
            result["comment"] = update_ret["comment"]
            result["result"] = update_ret["result"]
            resource_updated = resource_updated or bool(update_ret["ret"])
            if update_ret["ret"] and ctx.get("test", False):
                if update_ret["ret"].get("cidr_block_association_set") is not None:
                    plan_state["cidr_block_association_set"] = update_ret["ret"].get(
                        "cidr_block_association_set"
                    )
                if update_ret["ret"].get("ipv6_cidr_block_association_set") is not None:
                    plan_state["ipv6_cidr_block_association_set"] = update_ret[
                        "ret"
                    ].get("ipv6_cidr_block_association_set")
            # modify vpc attribute if the old and new attributes are not same
            if enable_dns_hostnames is not None or enable_dns_support is not None:
                update_ret = await hub.exec.aws.ec2.vpc.update_vpc_attributes(
                    ctx, enable_dns_hostnames, enable_dns_support, resource_id
                )
                result["comment"] = result["comment"] + update_ret["comment"]
                result["result"] = result["result"] and update_ret["result"]
                resource_updated = resource_updated or bool(update_ret["ret"])
                if update_ret["ret"] and ctx.get("test", False):
                    if enable_dns_support is not None:
                        plan_state["enable_dns_support"] = enable_dns_support
                    if enable_dns_hostnames is not None and enable_dns_support:
                        plan_state["enable_dns_hostnames"] = enable_dns_hostnames
            if tags is not None:
                # Update tags
                update_ret = await hub.exec.aws.ec2.tag.update_tags(
                    ctx=ctx,
                    resource_id=result["old_state"].get("resource_id"),
                    old_tags=result["old_state"].get("tags"),
                    new_tags=tags,
                )
                result["comment"] = result["comment"] + update_ret["comment"]
                result["result"] = result["result"] and update_ret["result"]
                resource_updated = resource_updated or bool(update_ret["ret"])
                if ctx.get("test", False) and update_ret["ret"] is not None:
                    plan_state["tags"] = update_ret["ret"].get("tags")
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = result["comment"] + (f"{e.__class__.__name__}: {e}",)
            result["result"] = False
    else:
        if ctx.get("test", False):
            result["new_state"] = hub.tool.aws.test_state_utils.generate_test_state(
                enforced_state={},
                desired_state={
                    "name": name,
                    "cidr_block_association_set": cidr_block_association_set,
                    "ipv6_cidr_block_association_set": ipv6_cidr_block_association_set,
                    "instance_tenancy": instance_tenancy,
                    "tags": tags,
                    "enable_dns_hostnames": enable_dns_hostnames,
                    "enable_dns_support": enable_dns_support,
                },
            )
            result["comment"] = (f"Would create aws.ec2.vpc '{name}'",)
            return result
        cidr_request_payload = {}
        # Since boto3 only allows one cidr association when creating a vpc, we use the first cidr associations
        # during vpc creation, associate the rest after creation.
        if cidr_block_association_set:
            cidr_request_payload = (
                hub.tool.aws.network_utils.generate_cidr_request_payload_for_vpc(
                    cidr_block_association_set[0], "ipv4"
                )
            )
            cidr_block_association_set.pop(0)
        elif ipv6_cidr_block_association_set:
            cidr_request_payload = (
                hub.tool.aws.network_utils.generate_cidr_request_payload_for_vpc(
                    ipv6_cidr_block_association_set[0], "ipv6"
                )
            )
            ipv6_cidr_block_association_set.pop(0)
        try:
            ret = await hub.exec.boto3.client.ec2.create_vpc(
                ctx,
                InstanceTenancy=instance_tenancy,
                TagSpecifications=[{"ResourceType": "vpc", "Tags": tags}]
                if tags
                else None,
                **cidr_request_payload,
            )
            result["result"] = ret["result"]
            if not result["result"]:
                result["comment"] = ret["comment"]
                return result
            result["comment"] = (f"Created '{name}'",)
            resource_id = ret["ret"]["Vpc"]["VpcId"]
            # Associate the rest cidr associations
            update_ret = await hub.exec.aws.ec2.vpc.update_cidr_blocks(
                ctx=ctx,
                vpc_id=resource_id,
                old_ipv4_cidr_blocks=[],
                old_ipv6_cidr_blocks=[],
                new_ipv4_cidr_blocks=cidr_block_association_set,
                new_ipv6_cidr_blocks=ipv6_cidr_block_association_set,
            )
            result["comment"] = result["comment"] + update_ret["comment"]
            result["result"] = result["result"] and update_ret["result"]

            # modify vpc attribute if the old and new attributes are not same
            if enable_dns_hostnames is not None or enable_dns_support is not None:
                update_ret = await hub.exec.aws.ec2.vpc.update_vpc_attributes(
                    ctx, enable_dns_hostnames, enable_dns_support, resource_id
                )
                result["comment"] = result["comment"] + update_ret["comment"]
                result["result"] = result["result"] and update_ret["result"]

        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = result["comment"] + (f"{e.__class__.__name__}: {e}",)
            result["result"] = False
    try:
        if ctx.get("test", False):
            result["new_state"] = plan_state
        elif (not before) or resource_updated:
            resource = hub.tool.boto3.resource.create(ctx, "ec2", "Vpc", resource_id)
            after = await hub.tool.boto3.resource.describe(resource)
            result[
                "new_state"
            ] = await hub.tool.aws.ec2.conversion_utils.convert_raw_vpc_to_present(
                ctx, raw_resource=after, idem_resource_name=name
            )
        else:
            result["new_state"] = copy.deepcopy(result["old_state"])
    except Exception as e:
        result["comment"] = result["comment"] + (str(e),)
        result["result"] = False
    return result


async def absent(
    hub,
    ctx,
    name: str,
    resource_id: str,
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Deletes the specified VPC. You must detach or delete all gateways and resources that are associated with the VPC
    before you can delete it. For example, you must terminate all instances running in the VPC, delete all security
    groups associated with the VPC (except the default one), delete all route tables associated with the VPC (except
    the default one), and so on.

    Args:
        name(Text): The Idem name of the VPC.
        resource_id(Text): The AWS ID of the VPC

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            vpc-01234672f3336db8:
              aws.ec2.vpc.absent:
                - resource_id: value
    """

    result = dict(comment=(), old_state=None, new_state=None, name=name, result=True)
    resource = hub.tool.boto3.resource.create(ctx, "ec2", "Vpc", resource_id)
    before = await hub.tool.boto3.resource.describe(resource)

    if not before:
        result["comment"] = (f"'{name}' already absent",)
    elif ctx.get("test", False):
        result[
            "old_state"
        ] = await hub.tool.aws.ec2.conversion_utils.convert_raw_vpc_to_present(
            ctx, raw_resource=before, idem_resource_name=name
        )
        result["comment"] = (f"Would delete aws.ec2.vpc '{name}'",)
        return result
    else:
        result[
            "old_state"
        ] = await hub.tool.aws.ec2.conversion_utils.convert_raw_vpc_to_present(
            ctx, raw_resource=before, idem_resource_name=name
        )
        try:
            ret = await hub.exec.boto3.client.ec2.delete_vpc(ctx, VpcId=resource_id)
            result["result"] = ret["result"]
            if not result["result"]:
                result["comment"] = ret["comment"]
                result["result"] = False
                return result
            result["comment"] = (f"Deleted '{name}'",)
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = result["comment"] + (f"{e.__class__.__name__}: {e}",)

    return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    result = {}
    ret = await hub.exec.boto3.client.ec2.describe_vpcs(ctx)

    if not ret["result"]:
        hub.log.debug(f"Could not describe VPCs {ret['comment']}")
        return {}

    for resource in ret["ret"]["Vpcs"]:
        resource_id = resource.get("VpcId")
        resource_translated = (
            await hub.tool.aws.ec2.conversion_utils.convert_raw_vpc_to_present(
                ctx, raw_resource=resource, idem_resource_name=resource_id
            )
        )
        result[resource_id] = {
            "aws.ec2.vpc.present": [
                {parameter_key: parameter_value}
                for parameter_key, parameter_value in resource_translated.items()
            ]
        }
    return result


async def search(
    hub, ctx, name, filters: List = None, resource_id: str = None, default: bool = None
):
    """
    Use an un-managed VPC as a data-source. Supply one of the inputs as the filter.

    Args:
        name(string): The name of the Idem state.
        resource_id(string, optional): AWS VPC id to identify the resource.
        default(bool, optional): Indicate whether the VPC is the default VPC.
        filters(list, optional): One or more filters: for example, tag :<key>, tag-key. A complete list of filters can be found at
         https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_vpcs

    Request Syntax:
        [Idem-state-name]:
          aws.ec2.vpc.search:
          - resource_id: 'string'
          - default: 'bool'
          - filters:
            - name: 'string'
              values: 'list'
            - name: 'string'
              values: 'list'

        Examples:

            my-unmanaged-vpc:
              aws.ec2.vpc.search:
                - resource_id: value
    """
    result = dict(comment=(), old_state=None, new_state=None, name=name, result=True)
    syntax_validation = hub.tool.aws.search_utils.search_filter_syntax_validation(
        filters=filters
    )
    if not syntax_validation["result"]:
        result["comment"] = syntax_validation["comment"]
        return result
    boto3_filter = hub.tool.aws.search_utils.convert_search_filter_to_boto3(
        filters=filters
    )
    if default is not None:
        boto3_filter.append({"Name": "is-default", "Values": [default]})
    ret = await hub.exec.boto3.client.ec2.describe_vpcs(
        ctx,
        Filters=boto3_filter,
        VpcIds=[resource_id],
    )
    if not ret["result"]:
        result["result"] = False
        result["comment"] = ret["comment"]
        return result
    if not ret["ret"]["Vpcs"]:
        result["comment"] = (
            f"Unable to find aws.ec2.vpc resource with filters {filters} and vpc id {resource_id}",
        )
    resource = ret["ret"]["Vpcs"][0]
    if len(ret["ret"]["Vpcs"]) > 1:
        result["comment"] = (
            f"More than one aws.ec2.vpc resource was found. Use resource {resource.get('VpcId')}",
        )
    result[
        "old_state"
    ] = await hub.tool.aws.ec2.conversion_utils.convert_raw_vpc_to_present(
        ctx, raw_resource=resource, idem_resource_name=name
    )
    # Populate both "old_state" and "new_state" with the same data
    result["new_state"] = copy.deepcopy(result["old_state"])
    return result
