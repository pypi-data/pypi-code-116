"""
Autogenerated state module using `pop-create-idem <https://gitlab.com/saltstack/pop/pop-create-idem>`__

Note..

The describe function uses the describe_spot_instance_requests to request spot instance details.
The present function uses the request_spot_instances to request creation of a spot instance.
The delete function uses the standard terminate_instances as the cancel_spot_requests does
not terminate an instance that comes online.

If you wish to delete or terminate an instance, and it's a spot instance, you must use the describe
function here to obtain the InstanceID and then use ec2.instance.absent to fully terminate the instance.
"""
from collections import OrderedDict
from typing import Any
from typing import Dict
from typing import List


__contracts__ = ["resource"]


async def present(
    hub,
    ctx,
    name: str,
    spot_instance_request_id=None,
    availability_zone_group=None,
    instance_count=None,
    instance_interruption_behavior=None,
    launch_group=None,
    launch_specification=None,
    spot_price=None,
    type=None,
    valid_from=None,
    valid_until=None,
    tags: List = None,
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Request Parameters
        The following parameters are for this specific action. For more information about required
         and optional parameters that are common to all actions, see Common Query Parameters.

        spot_instance_id(Text):
            The spot instance request id

        availability_zone_group
            The user-specified name for a logical grouping of requests.

            When you specify an Availability Zone group in a Spot Instance request,
            all Spot Instances in the request are launched in the same Availability Zone.
            Instance proximity is maintained with this parameter, but the choice of
            Availability Zone is not. The group applies only to requests for Spot Instances
            of the same instance type. Any additional Spot Instance requests that are
            specified with the same Availability Zone group name are launched in that
            same Availability Zone, as long as at least one instance from the group is still active.

            If there is no active instance running in the Availability Zone group that
            you specify for a new Spot Instance request (all instances are terminated,
            the request is expired, or the maximum price you specified falls below
            current Spot price), then Amazon EC2 launches the instance in any Availability
            Zone where the constraint can be met. Consequently, the subsequent set of Spot
            Instances could be placed in a different zone from the original request,
            even if you specified the same Availability Zone group.

            Default: Instances are launched in any available Availability Zone.

            Type: String

            Required: No

        BlockDurationMinutes
            Deprecated.

            Type: Integer

            Required: No

        instance_count
            The maximum number of Spot Instances to launch.

            Default: 1

            Type: Integer

            Required: No

        instance_interruption_behavior
            The behavior when a Spot Instance is interrupted. The default is terminate.

            Type: String

            Valid Values: hibernate | stop | terminate

            Required: No

        launch_group
            The instance launch group. Launch groups are Spot Instances that launch together and terminate together.

            Default: Instances are launched and terminated individually

            Type: String

            Required: No

        launch_specification
            The launch specification.

            Type: RequestSpotLaunchSpecification object dict

            Required: No

            Below are the attributes available for LaunchSpecification:

                SecurityGroupIds (list) --
                One or more security group IDs.

                (string) --
                SecurityGroups (list) --
                One or more security groups. When requesting instances in a VPC,
                you must specify the IDs of the security groups. When requesting
                instances in EC2-Classic, you can specify the names or the IDs
                of the security groups.

                (string) --
                AddressingType (string) --
                Deprecated.

                BlockDeviceMappings (list) --
                One or more block device mapping entries. You can't specify both
                a snapshot ID and an encryption value. This is because only blank
                volumes can be encrypted on creation. If a snapshot is the basis
                for a volume, it is not blank and its encryption status is used
                for the volume encryption status.

                (dict) --
                Describes a block device mapping, which defines the EBS volumes
                and instance store volumes to attach to an instance at launch.

                DeviceName (string) --
                The device name (for example, /dev/sdh or xvdh ).

                VirtualName (string) --
                The virtual device name (ephemeral N). Instance store volumes
                are numbered starting from 0. An instance type with 2 available
                instance store volumes can specify mappings for ephemeral0 and
                ephemeral1. The number of available instance store volumes depends
                on the instance type. After you connect to the instance,
                you must mount the volume.

                NVMe instance store volumes are automatically enumerated and
                assigned a device name. Including them in your block device
                mapping has no effect.

                Constraints: For M3 instances, you must specify instance store
                volumes in the block device mapping for the instance. When you
                launch an M3 instance, we ignore any instance store volumes
                specified in the block device mapping for the AMI.

                Ebs (dict) --
                Parameters used to automatically set up EBS volumes when the
                instance is launched.

                DeleteOnTermination (boolean) --
                Indicates whether the EBS volume is deleted on instance termination. For more information, see Preserving Amazon EBS volumes on instance termination in the Amazon EC2 User Guide .

                Iops (integer) --
                The number of I/O operations per second (IOPS). For gp3 , io1 , and io2 volumes, this represents the number of IOPS that are provisioned for the volume. For gp2 volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.

                The following are the supported values for each volume type:

                gp3 : 3,000-16,000 IOPS
                io1 : 100-64,000 IOPS
                io2 : 100-64,000 IOPS
                For io1 and io2 volumes, we guarantee 64,000 IOPS only for Instances built on the Nitro System . Other instance families guarantee performance up to 32,000 IOPS.

                This parameter is required for io1 and io2 volumes. The default for gp3 volumes is 3,000 IOPS. This parameter is not supported for gp2 , st1 , sc1 , or standard volumes.

                SnapshotId (string) --
                The ID of the snapshot.

                VolumeSize (integer) --
                The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. If you specify a snapshot, the default is the snapshot size. You can specify a volume size that is equal to or larger than the snapshot size.

                The following are the supported volumes sizes for each volume type:

                gp2 and gp3 :1-16,384
                io1 and io2 : 4-16,384
                st1 and sc1 : 125-16,384
                standard : 1-1,024
                VolumeType (string) --
                The volume type. For more information, see Amazon EBS volume types in the Amazon EC2 User Guide . If the volume type is io1 or io2 , you must specify the IOPS that the volume supports.

                KmsKeyId (string) --
                Identifier (key ID, key alias, ID ARN, or alias ARN) for a customer managed CMK under which the EBS volume is encrypted.

                This parameter is only supported on BlockDeviceMapping objects called by RunInstances , RequestSpotFleet , and RequestSpotInstances .

                Throughput (integer) --
                The throughput that the volume supports, in MiB/s.

                This parameter is valid only for gp3 volumes.

                Valid Range: Minimum value of 125. Maximum value of 1000.

                OutpostArn (string) --
                The ARN of the Outpost on which the snapshot is stored.

                Encrypted (boolean) --
                Indicates whether the encryption state of an EBS volume is changed while being restored from a backing snapshot. The effect of setting the encryption state to true depends on the volume origin (new or from a snapshot), starting encryption state, ownership, and whether encryption by default is enabled. For more information, see Amazon EBS encryption in the Amazon EC2 User Guide .

                In no case can you remove encryption from an encrypted volume.

                Encrypted volumes can only be attached to instances that support Amazon EBS encryption. For more information, see Supported instance types .

                This parameter is not returned by .

                NoDevice (string) --
                To omit the device from the block device mapping, specify an empty string. When this property is specified, the device is removed from the block device mapping regardless of the assigned value.

                EbsOptimized (boolean) --
                Indicates whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.

                Default: false

                IamInstanceProfile (dict) --
                The IAM instance profile.

                Arn (string) --
                The Amazon Resource Name (ARN) of the instance profile.

                Name (string) --
                The name of the instance profile.

                ImageId (string) --
                The ID of the AMI.

                InstanceType (string) --
                The instance type.

                KernelId (string) --
                The ID of the kernel.

                KeyName (string) --
                The name of the key pair.

                Monitoring (dict) --
                Indicates whether basic or detailed monitoring is enabled for the instance.

                Default: Disabled

                Enabled (boolean) -- [REQUIRED]
                Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.

                NetworkInterfaces (list) --
                One or more network interfaces. If you specify a network interface, you must specify subnet IDs and security group IDs using the network interface.

                (dict) --
                Describes a network interface.

                AssociatePublicIpAddress (boolean) --
                Indicates whether to assign a public IPv4 address to an instance you launch in a VPC. The public IP address can only be assigned to a network interface for eth0, and can only be assigned to a new network interface, not an existing one. You cannot specify more than one network interface in the request. If launching into a default subnet, the default value is true .

                DeleteOnTermination (boolean) --
                If set to true , the interface is deleted when the instance is terminated. You can specify true only if creating a new network interface when launching an instance.

                Description (string) --
                The description of the network interface. Applies only if creating a network interface when launching an instance.

                DeviceIndex (integer) --
                The position of the network interface in the attachment order. A primary network interface has a device index of 0.

                If you specify a network interface when launching an instance, you must specify the device index.

                Groups (list) --
                The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance.

                (string) --
                Ipv6AddressCount (integer) --
                A number of IPv6 addresses to assign to the network interface. Amazon EC2 chooses the IPv6 addresses from the range of the subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.

                Ipv6Addresses (list) --
                One or more IPv6 addresses to assign to the network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.

                (dict) --
                Describes an IPv6 address.

                Ipv6Address (string) --
                The IPv6 address.

                NetworkInterfaceId (string) --
                The ID of the network interface.

                If you are creating a Spot Fleet, omit this parameter because you can’t specify a network interface ID in a launch specification.

                PrivateIpAddress (string) --
                The private IPv4 address of the network interface. Applies only if creating a network interface when launching an instance. You cannot specify this option if you're launching more than one instance in a RunInstances request.

                PrivateIpAddresses (list) --
                One or more private IPv4 addresses to assign to the network interface. Only one private IPv4 address can be designated as primary. You cannot specify this option if you're launching more than one instance in a RunInstances request.

                (dict) --
                Describes a secondary private IPv4 address for a network interface.

                Primary (boolean) --
                Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.

                PrivateIpAddress (string) --
                The private IPv4 addresses.

                SecondaryPrivateIpAddressCount (integer) --
                The number of secondary private IPv4 addresses. You can't specify this option and specify more than one private IP address using the private IP addresses option. You cannot specify this option if you're launching more than one instance in a RunInstances request.

                SubnetId (string) --
                The ID of the subnet associated with the network interface. Applies only if creating a network interface when launching an instance.

                AssociateCarrierIpAddress (boolean) --
                Indicates whether to assign a carrier IP address to the network interface.

                You can only assign a carrier IP address to a network interface that is in a subnet in a Wavelength Zone. For more information about carrier IP addresses, see Carrier IP addresses in the Amazon Web Services Wavelength Developer Guide.

                InterfaceType (string) --
                The type of network interface.

                To create an Elastic Fabric Adapter (EFA), specify efa . For more information, see Elastic Fabric Adapter in the Amazon Elastic Compute Cloud User Guide .

                Valid values: interface | efa

                NetworkCardIndex (integer) --
                The index of the network card. Some instance types support multiple network cards. The primary network interface must be assigned to network card index 0. The default is network card index 0.

                If you are using RequestSpotInstances to create Spot Instances, omit this parameter because you can’t specify the network card index when using this API. To specify the network card index, use RunInstances .

                Ipv4Prefixes (list) --
                One or more IPv4 delegated prefixes to be assigned to the network interface. You cannot use this option if you use the Ipv4PrefixCount option.

                (dict) --
                Describes the IPv4 prefix option for a network interface.

                Ipv4Prefix (string) --
                The IPv4 prefix. For information, see Assigning prefixes to Amazon EC2 network interfaces in the Amazon Elastic Compute Cloud User Guide .

                Ipv4PrefixCount (integer) --
                The number of IPv4 delegated prefixes to be automatically assigned to the network interface. You cannot use this option if you use the Ipv4Prefix option.

                Ipv6Prefixes (list) --
                One or more IPv6 delegated prefixes to be assigned to the network interface. You cannot use this option if you use the Ipv6PrefixCount option.

                (dict) --
                Describes the IPv4 prefix option for a network interface.

                Ipv6Prefix (string) --
                The IPv6 prefix.

                Ipv6PrefixCount (integer) --
                The number of IPv6 delegated prefixes to be automatically assigned to the network interface. You cannot use this option if you use the Ipv6Prefix option.

                Placement (dict) --
                The placement information for the instance.

                AvailabilityZone (string) --
                The Availability Zone.

                [Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, "us-west-2a, us-west-2b".

                GroupName (string) --
                The name of the placement group.

                Tenancy (string) --
                The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for Spot Instances.

                RamdiskId (string) --
                The ID of the RAM disk.

                SubnetId (string) --
                The ID of the subnet in which to launch the instance.

                UserData (string) --
                The Base64-encoded user data for the instance. User data is limited to 16 KB.

        spot_price
            The maximum price per hour that you are willing to pay for
            a Spot Instance. The default is the On-Demand price.

            Type: String

            Required: No

        tag_specifications
            The key-value pair for tagging the Spot Instance request on creation.
            The value for ResourceType must be spot-instances-request, otherwise
            the Spot Instance request fails. To tag the Spot Instance request
            after it has been created, see CreateTags.

            Type: Array of TagSpecification objects

            tags(List, optional): The tags to assign to the VPC. Defaults to None.
                * Key (string) -- The key of the tag.
                Tag keys are case-sensitive and accept a maximum of 127 Unicode characters.
                May not begin with aws.
                * Value (string) -- The value of the tag. Tag values are case-sensitive
                and accept a maximum of 255 Unicode characters.

            Required: No

        type
            The Spot Instance request type.

            Default: one-time

            Type: String

            Valid Values: one-time | persistent

            Required: No

        valid_from
            The start date of the request. If this is a one-time request,
            the request becomes active at this date and time and remains
            active until all instances launch, the request expires, or
            the request is canceled. If the request is persistent, the
            request becomes active at this date and time and remains
            active until it expires or is canceled.

            The specified start date and time cannot be equal to the current
            date and time. You must specify a start date and time that
            occurs after the current date and time.

            Type: Timestamp

            Required: No

        valid_until
            The end date of the request, in UTC format (YYYY-MM-DDTHH:MM:SSZ).

            For a persistent request, the request remains active until the ValidUntil
            date and time is reached. Otherwise, the request remains active until you cancel it.

            For a one-time request, the request remains active until all instances launch,
            the request is canceled, or the ValidUntil date and time is reached.
            By default, the request is valid for 7 days from the date the request
            was created.

            Type: Timestamp

            Required: No

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            resource_is_present:
              aws.ec2.spot_instance.present:
                - name: value

        .. code-block:: sls

            resource_is_present:
              aws.ec2.spot_instance.present:
                instance_count: 5
                launch_specification:
                    ImageId: ami-fce3c696
                    KeyName: awskey.pem
                    SecurityGroups: ['sg-709f8709']
                    InstanceType: m4.large
                    Placement:
                        AvailabilityZone: us-east-1a
                    BlockDeviceMappings:
                            Ebs:
                                SnapshotId: snap-f70deff0
                                VolumeSize: 100
                                DeleteOnTermination: True
                                VolumeType: gp2
                                Iops: 300
                                Encrypted: False
                    EbsOptimized: True
                    Monitoring:
                        Enabled: True
                    SecurityGroupIds: sg-709f8709
                spot_price: 0.03
                type: one-time
    """
    if spot_instance_request_id is None:
        spot_instance_request_id = name

    result = dict(comment="", old_state=None, new_state=None, name=name, result=True)
    before = await hub.exec.boto3.client.ec2.describe_spot_instance_requests(
        spot_instance_request_id
    )
    result["new_state"] = before

    if ctx.get("test", False):
        if before:
            result["comment"] = "Would update aws.ec2.spot_instance"
            result["result"] = True
        else:
            result["comment"] = "Would create aws.ec2.spot_instance"
            result["result"] = True
        return result

    if not before:
        try:
            # Although it's not specified in the API documentation,
            # apparently 'SecurityGroups' parameter requires the
            # names of the security groups, not the IDs, inside the
            # LaunchSpecification dict
            ret = await hub.exec.boto3.client.ec2.request_spot_instances(
                ctx,
                DryRun=False,
                **{
                    "AvailabilityZoneGroup": availability_zone_group,
                    "InstanceCount": instance_count,
                    "LaunchGroup": launch_group,
                    "LaunchSpecification": launch_specification,
                    "SpotPrice": spot_price,
                    "Type": type,
                    "ValidFrom": valid_from,
                    "ValidUntil": valid_until,
                    "TagSpecifications": [{"ResourceType": "instance", "Tags": tags}]
                    if tags
                    else None,
                    "InstanceInterruptionBehavior": instance_interruption_behavior,
                },
            )
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = f"{e.__class__.__name__}: {e}"
            result["result"] = False
        else:
            result["result"] = ret["result"]
            if not result["result"]:
                result["comment"] = ret["comment"]
                return result
            assert ret["result"] is True
            assert (
                ret["ret"]["SpotInstanceRequests"][0]["Status"]["Code"]
                == "pending-evaluation"
            )
            name = ret["ret"]["SpotInstanceRequests"][0]["SpotInstanceRequestId"]
            # Since we don't have a valid instance yet use the RequestId as the name for lookup
            result["comment"] = name
    else:
        result["comment"] = f"{spot_instance_request_id} already exists."

    if not before:
        try:
            after = await hub.exec.boto3.client.ec2.describe_spot_instance_requests(
                spot_instance_request_id
            )
        except Exception as e:
            result["comment"] = str(e)
            result["result"] = False
        else:
            result["new_state"] = after
            result["old_state"] = before

    return result


async def absent(
    hub, ctx, name: str, spot_instance_request_id: str = None
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Cancels one or more Spot Instance requests.

    Args:
        spot_instance_request_id(Text): The spot instance request id

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            resource_is_absent:
              aws.ec2.spot_instance.absent:
                - name: value
    """
    if spot_instance_request_id is None:
        spot_instance_request_id = name
    result = dict(comment="", old_state=None, new_state=None, name=name, result=True)
    before = await hub.exec.boto3.client.ec2.describe_spot_instance_requests(
        spot_instance_request_id
    )

    if not before:
        result["comment"] = f"'{name}' already absent"
    elif ctx.get("test", False):
        result["comment"] = f"Would cancel aws.ec2.request_spot_instances {name}"
        return result
    else:
        try:
            # Warning...
            # Canceling a Spot Instance request does not terminate
            # running Spot Instances associated with the request
            ret = await hub.exec.boto3.client.ec2.cancel_spot_instance_requests(
                ctx,
                DryRun=False,
                **{"SpotInstanceRequestIds": [spot_instance_request_id]},
            )
            result["result"] = ret["result"]
            if not result["result"]:
                result["comment"] = ret["comment"]
                return result
            result["comment"] = f"Deleted '{name}'"
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = f"{e.__class__.__name__}: {e}"
        result["old_state"] = before

    return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    result = {}
    ret = await hub.exec.boto3.client.ec2.describe_spot_instance_requests(
        ctx, MaxResults=5
    )
    if not ret["result"]:
        hub.log.debug(f"Could not describe spot instances {ret['comment']}")
        return {}

    instances = []
    for reservation in ret["ret"]["SpotInstanceRequests"]:
        instances.append(reservation)
    # Primary parameters for spot instances
    describe_parameters = OrderedDict(
        {
            "CreateTime": "create_time",
            "LaunchedAvailabilityZone": "launched_availability_zone",
            "ProductDescription": "product_description",
            "SpotInstanceRequestId": "spot_instance_request_id",
            "SpotPrice": "spot_price",
            "State": "state",
            "Status": "status",
            "Tags": "tags",
        }
    )

    for instance in instances:
        instance_id = instance.get("InstanceId")
        # Instance specifications described below
        describe_parameters_specs = OrderedDict(
            {
                "BlockDeviceMappings": "block_device_mappings",
                "ImageId": "image_id",
                "InstanceType": "instance_type",
                "Monitoring": "monitoring",
                "Placement": "placement",
                "NetworkInterfaces": "network_interfaces",
                "SecurityGroups": "security_groups",
            }
        )
        instance_translated = []
        for p_old_key, p_new_key in describe_parameters.items():
            if instance.get(p_old_key) is not None:
                instance_translated.append({p_new_key: instance.get(p_old_key)})

        for parameter_old_key, parameter_new_key in describe_parameters_specs.items():
            instance_specs = instance.get("LaunchSpecification")
            if instance_specs.get(parameter_old_key) is not None:
                instance_translated.append(
                    {parameter_new_key: instance_specs.get(parameter_old_key)}
                )

        result[instance_id] = {"aws.ec2.spot_instance.present": instance_translated}
    return result
