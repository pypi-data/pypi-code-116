# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, double, integer
from .validators.batch import (
    validate_allocation_strategy,
    validate_environment_state,
    validate_launch_template_specification,
    validate_queue_state,
)


class Ec2ConfigurationObject(AWSProperty):
    """
    `Ec2ConfigurationObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html>`__
    """

    props: PropsDictType = {
        "ImageIdOverride": (str, False),
        "ImageType": (str, True),
    }


class LaunchTemplateSpecification(AWSProperty):
    """
    `LaunchTemplateSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html>`__
    """

    props: PropsDictType = {
        "LaunchTemplateId": (str, False),
        "LaunchTemplateName": (str, False),
        "Version": (str, False),
    }

    def validate(self):
        validate_launch_template_specification(self)


class ComputeResources(AWSProperty):
    """
    `ComputeResources <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html>`__
    """

    props: PropsDictType = {
        "AllocationStrategy": (validate_allocation_strategy, False),
        "BidPercentage": (integer, False),
        "DesiredvCpus": (integer, False),
        "Ec2Configuration": ([Ec2ConfigurationObject], False),
        "Ec2KeyPair": (str, False),
        "ImageId": (str, False),
        "InstanceRole": (str, False),
        "InstanceTypes": ([str], False),
        "LaunchTemplate": (LaunchTemplateSpecification, False),
        "MaxvCpus": (integer, True),
        "MinvCpus": (integer, False),
        "PlacementGroup": (str, False),
        "SecurityGroupIds": ([str], False),
        "SpotIamFleetRole": (str, False),
        "Subnets": ([str], True),
        "Tags": (dict, False),
        "Type": (str, True),
    }


class ComputeEnvironment(AWSObject):
    """
    `ComputeEnvironment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html>`__
    """

    resource_type = "AWS::Batch::ComputeEnvironment"

    props: PropsDictType = {
        "ComputeEnvironmentName": (str, False),
        "ComputeResources": (ComputeResources, False),
        "ServiceRole": (str, False),
        "State": (validate_environment_state, False),
        "Tags": (dict, False),
        "Type": (str, True),
        "UnmanagedvCpus": (integer, False),
    }


class Environment(AWSProperty):
    """
    `Environment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class FargatePlatformConfiguration(AWSProperty):
    """
    `FargatePlatformConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-fargateplatformconfiguration.html>`__
    """

    props: PropsDictType = {
        "PlatformVersion": (str, False),
    }


class Device(AWSProperty):
    """
    `Device <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html>`__
    """

    props: PropsDictType = {
        "ContainerPath": (str, False),
        "HostPath": (str, False),
        "Permissions": ([str], False),
    }


class Tmpfs(AWSProperty):
    """
    `Tmpfs <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html>`__
    """

    props: PropsDictType = {
        "ContainerPath": (str, True),
        "MountOptions": ([str], False),
        "Size": (integer, True),
    }


class LinuxParameters(AWSProperty):
    """
    `LinuxParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html>`__
    """

    props: PropsDictType = {
        "Devices": ([Device], False),
        "InitProcessEnabled": (boolean, False),
        "MaxSwap": (integer, False),
        "SharedMemorySize": (integer, False),
        "Swappiness": (integer, False),
        "Tmpfs": ([Tmpfs], False),
    }


class Secret(AWSProperty):
    """
    `Secret <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "ValueFrom": (str, True),
    }


class LogConfiguration(AWSProperty):
    """
    `LogConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html>`__
    """

    props: PropsDictType = {
        "LogDriver": (str, True),
        "Options": (dict, False),
        "SecretOptions": ([Secret], False),
    }


class MountPoints(AWSProperty):
    """
    `MountPoints <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html>`__
    """

    props: PropsDictType = {
        "ContainerPath": (str, False),
        "ReadOnly": (boolean, False),
        "SourceVolume": (str, False),
    }


class NetworkConfiguration(AWSProperty):
    """
    `NetworkConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-networkconfiguration.html>`__
    """

    props: PropsDictType = {
        "AssignPublicIp": (str, False),
    }


class ResourceRequirement(AWSProperty):
    """
    `ResourceRequirement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html>`__
    """

    props: PropsDictType = {
        "Type": (str, False),
        "Value": (str, False),
    }


class Ulimit(AWSProperty):
    """
    `Ulimit <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html>`__
    """

    props: PropsDictType = {
        "HardLimit": (integer, True),
        "Name": (str, True),
        "SoftLimit": (integer, True),
    }


class AuthorizationConfig(AWSProperty):
    """
    `AuthorizationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-authorizationconfig.html>`__
    """

    props: PropsDictType = {
        "AccessPointId": (str, False),
        "Iam": (str, False),
    }


class EfsVolumeConfiguration(AWSProperty):
    """
    `EfsVolumeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html>`__
    """

    props: PropsDictType = {
        "AuthorizationConfig": (AuthorizationConfig, False),
        "FileSystemId": (str, True),
        "RootDirectory": (str, False),
        "TransitEncryption": (str, False),
        "TransitEncryptionPort": (integer, False),
    }


class VolumesHost(AWSProperty):
    """
    `VolumesHost <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumeshost.html>`__
    """

    props: PropsDictType = {
        "SourcePath": (str, False),
    }


class Volumes(AWSProperty):
    """
    `Volumes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html>`__
    """

    props: PropsDictType = {
        "EfsVolumeConfiguration": (EfsVolumeConfiguration, False),
        "Host": (VolumesHost, False),
        "Name": (str, False),
    }


class ContainerProperties(AWSProperty):
    """
    `ContainerProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html>`__
    """

    props: PropsDictType = {
        "Command": ([str], False),
        "Environment": ([Environment], False),
        "ExecutionRoleArn": (str, False),
        "FargatePlatformConfiguration": (FargatePlatformConfiguration, False),
        "Image": (str, True),
        "InstanceType": (str, False),
        "JobRoleArn": (str, False),
        "LinuxParameters": (LinuxParameters, False),
        "LogConfiguration": (LogConfiguration, False),
        "Memory": (integer, False),
        "MountPoints": ([MountPoints], False),
        "NetworkConfiguration": (NetworkConfiguration, False),
        "Privileged": (boolean, False),
        "ReadonlyRootFilesystem": (boolean, False),
        "ResourceRequirements": ([ResourceRequirement], False),
        "Secrets": ([Secret], False),
        "Ulimits": ([Ulimit], False),
        "User": (str, False),
        "Vcpus": (integer, False),
        "Volumes": ([Volumes], False),
    }


class NodeRangeProperty(AWSProperty):
    """
    `NodeRangeProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html>`__
    """

    props: PropsDictType = {
        "Container": (ContainerProperties, False),
        "TargetNodes": (str, True),
    }


class NodeProperties(AWSProperty):
    """
    `NodeProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html>`__
    """

    props: PropsDictType = {
        "MainNode": (integer, True),
        "NodeRangeProperties": ([NodeRangeProperty], True),
        "NumNodes": (integer, True),
    }


class EvaluateOnExit(AWSProperty):
    """
    `EvaluateOnExit <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html>`__
    """

    props: PropsDictType = {
        "Action": (str, True),
        "OnExitCode": (str, False),
        "OnReason": (str, False),
        "OnStatusReason": (str, False),
    }


class RetryStrategy(AWSProperty):
    """
    `RetryStrategy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html>`__
    """

    props: PropsDictType = {
        "Attempts": (integer, False),
        "EvaluateOnExit": ([EvaluateOnExit], False),
    }


class Timeout(AWSProperty):
    """
    `Timeout <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-timeout.html>`__
    """

    props: PropsDictType = {
        "AttemptDurationSeconds": (integer, False),
    }


class JobDefinition(AWSObject):
    """
    `JobDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html>`__
    """

    resource_type = "AWS::Batch::JobDefinition"

    props: PropsDictType = {
        "ContainerProperties": (ContainerProperties, False),
        "JobDefinitionName": (str, False),
        "NodeProperties": (NodeProperties, False),
        "Parameters": (dict, False),
        "PlatformCapabilities": ([str], False),
        "PropagateTags": (boolean, False),
        "RetryStrategy": (RetryStrategy, False),
        "SchedulingPriority": (integer, False),
        "Tags": (dict, False),
        "Timeout": (Timeout, False),
        "Type": (str, True),
    }


class ComputeEnvironmentOrder(AWSProperty):
    """
    `ComputeEnvironmentOrder <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html>`__
    """

    props: PropsDictType = {
        "ComputeEnvironment": (str, True),
        "Order": (integer, True),
    }


class JobQueue(AWSObject):
    """
    `JobQueue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html>`__
    """

    resource_type = "AWS::Batch::JobQueue"

    props: PropsDictType = {
        "ComputeEnvironmentOrder": ([ComputeEnvironmentOrder], True),
        "JobQueueName": (str, False),
        "Priority": (integer, True),
        "SchedulingPolicyArn": (str, False),
        "State": (validate_queue_state, False),
        "Tags": (dict, False),
    }


class ShareAttributes(AWSProperty):
    """
    `ShareAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-shareattributes.html>`__
    """

    props: PropsDictType = {
        "ShareIdentifier": (str, False),
        "WeightFactor": (double, False),
    }


class FairsharePolicy(AWSProperty):
    """
    `FairsharePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html>`__
    """

    props: PropsDictType = {
        "ComputeReservation": (double, False),
        "ShareDecaySeconds": (double, False),
        "ShareDistribution": ([ShareAttributes], False),
    }


class SchedulingPolicy(AWSObject):
    """
    `SchedulingPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html>`__
    """

    resource_type = "AWS::Batch::SchedulingPolicy"

    props: PropsDictType = {
        "FairsharePolicy": (FairsharePolicy, False),
        "Name": (str, False),
        "Tags": (dict, False),
    }
