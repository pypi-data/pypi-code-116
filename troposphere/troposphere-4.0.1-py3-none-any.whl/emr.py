# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.emr import CHANGE_IN_CAPACITY  # noqa: F401
from .validators.emr import EXACT_CAPACITY  # noqa: F401
from .validators.emr import PERCENT_CHANGE_IN_CAPACITY  # noqa: F401
from .validators.emr import KeyValue  # noqa: F401
from .validators.emr import MetricDimension  # noqa: F401
from .validators.emr import (
    action_on_failure_validator,
    additional_info_validator,
    market_validator,
    properties_validator,
    validate_configurations,
    validate_defer,
    validate_on_demand_provisioning_specification,
    validate_simple_scaling_policy_configuration,
    validate_spot_provisioning_specification,
    volume_type_validator,
)


class Application(AWSProperty):
    """
    `Application <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-application.html>`__
    """

    props: PropsDictType = {
        "AdditionalInfo": (additional_info_validator, False),
        "Args": ([str], False),
        "Name": (str, False),
        "Version": (str, False),
    }


class ScriptBootstrapActionConfig(AWSProperty):
    """
    `ScriptBootstrapActionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scriptbootstrapactionconfig.html>`__
    """

    props: PropsDictType = {
        "Args": ([str], False),
        "Path": (str, True),
    }


class BootstrapActionConfig(AWSProperty):
    """
    `BootstrapActionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-bootstrapactionconfig.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "ScriptBootstrapAction": (ScriptBootstrapActionConfig, True),
    }


class Configuration(AWSProperty):
    """
    `Configuration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-configuration.html>`__
    """

    props: PropsDictType = {
        "Classification": (str, False),
        "ConfigurationProperties": (properties_validator, False),
        "Configurations": (validate_configurations, False),
    }


class OnDemandProvisioningSpecification(AWSProperty):
    """
    `OnDemandProvisioningSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ondemandprovisioningspecification.html>`__
    """

    props: PropsDictType = {
        "AllocationStrategy": (str, True),
    }

    def validate(self):
        validate_on_demand_provisioning_specification(self)


class SpotProvisioningSpecification(AWSProperty):
    """
    `SpotProvisioningSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-spotprovisioningspecification.html>`__
    """

    props: PropsDictType = {
        "AllocationStrategy": (str, False),
        "BlockDurationMinutes": (integer, False),
        "TimeoutAction": (str, True),
        "TimeoutDurationMinutes": (integer, True),
    }

    def validate(self):
        validate_spot_provisioning_specification(self)


class InstanceFleetProvisioningSpecifications(AWSProperty):
    """
    `InstanceFleetProvisioningSpecifications <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancefleetprovisioningspecifications.html>`__
    """

    props: PropsDictType = {
        "OnDemandSpecification": (OnDemandProvisioningSpecification, False),
        "SpotSpecification": (SpotProvisioningSpecification, False),
    }


class VolumeSpecification(AWSProperty):
    """
    `VolumeSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification.html>`__
    """

    props: PropsDictType = {
        "Iops": (integer, False),
        "SizeInGB": (integer, True),
        "VolumeType": (volume_type_validator, True),
    }


class EbsBlockDeviceConfigs(AWSProperty):
    """
    `EbsBlockDeviceConfigs <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ebsblockdeviceconfig.html>`__
    """

    props: PropsDictType = {
        "VolumeSpecification": (VolumeSpecification, True),
        "VolumesPerInstance": (integer, False),
    }


class EbsConfiguration(AWSProperty):
    """
    `EbsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration.html>`__
    """

    props: PropsDictType = {
        "EbsBlockDeviceConfigs": ([EbsBlockDeviceConfigs], False),
        "EbsOptimized": (boolean, False),
    }


class InstanceTypeConfig(AWSProperty):
    """
    `InstanceTypeConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html>`__
    """

    props: PropsDictType = {
        "BidPrice": (str, False),
        "BidPriceAsPercentageOfOnDemandPrice": (double, False),
        "Configurations": ([Configuration], False),
        "CustomAmiId": (str, False),
        "EbsConfiguration": (EbsConfiguration, False),
        "InstanceType": (str, True),
        "WeightedCapacity": (integer, False),
    }


class InstanceFleetConfigProperty(AWSProperty):
    """
    `InstanceFleetConfigProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetconfig.html>`__
    """

    props: PropsDictType = {
        "InstanceTypeConfigs": ([InstanceTypeConfig], False),
        "LaunchSpecifications": (InstanceFleetProvisioningSpecifications, False),
        "Name": (str, False),
        "TargetOnDemandCapacity": (integer, False),
        "TargetSpotCapacity": (integer, False),
    }


class ScalingConstraints(AWSProperty):
    """
    `ScalingConstraints <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingconstraints.html>`__
    """

    props: PropsDictType = {
        "MaxCapacity": (integer, True),
        "MinCapacity": (integer, True),
    }


class SimpleScalingPolicyConfiguration(AWSProperty):
    """
    `SimpleScalingPolicyConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration.html>`__
    """

    props: PropsDictType = {
        "AdjustmentType": (str, False),
        "CoolDown": (integer, False),
        "ScalingAdjustment": (validate_defer, True),
    }

    def validate(self):
        validate_simple_scaling_policy_configuration(self)


class ScalingAction(AWSProperty):
    """
    `ScalingAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingaction.html>`__
    """

    props: PropsDictType = {
        "Market": (market_validator, False),
        "SimpleScalingPolicyConfiguration": (SimpleScalingPolicyConfiguration, True),
    }


class CloudWatchAlarmDefinition(AWSProperty):
    """
    `CloudWatchAlarmDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html>`__
    """

    props: PropsDictType = {
        "ComparisonOperator": (str, True),
        "Dimensions": ([MetricDimension], False),
        "EvaluationPeriods": (integer, False),
        "MetricName": (str, True),
        "Namespace": (str, False),
        "Period": (integer, True),
        "Statistic": (str, False),
        "Threshold": (double, True),
        "Unit": (str, False),
    }


class ScalingTrigger(AWSProperty):
    """
    `ScalingTrigger <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingtrigger.html>`__
    """

    props: PropsDictType = {
        "CloudWatchAlarmDefinition": (CloudWatchAlarmDefinition, True),
    }


class ScalingRule(AWSProperty):
    """
    `ScalingRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingrule.html>`__
    """

    props: PropsDictType = {
        "Action": (ScalingAction, True),
        "Description": (str, False),
        "Name": (str, True),
        "Trigger": (ScalingTrigger, True),
    }


class AutoScalingPolicy(AWSProperty):
    """
    `AutoScalingPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-autoscalingpolicy.html>`__
    """

    props: PropsDictType = {
        "Constraints": (ScalingConstraints, True),
        "Rules": ([ScalingRule], True),
    }


class InstanceGroupConfigProperty(AWSProperty):
    """
    `InstanceGroupConfigProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html>`__
    """

    props: PropsDictType = {
        "AutoScalingPolicy": (AutoScalingPolicy, False),
        "BidPrice": (str, False),
        "Configurations": ([Configuration], False),
        "CustomAmiId": (str, False),
        "EbsConfiguration": (EbsConfiguration, False),
        "InstanceCount": (integer, True),
        "InstanceType": (str, True),
        "Market": (market_validator, False),
        "Name": (str, False),
    }


class PlacementType(AWSProperty):
    """
    `PlacementType <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-placementtype.html>`__
    """

    props: PropsDictType = {
        "AvailabilityZone": (str, True),
    }


class JobFlowInstancesConfig(AWSProperty):
    """
    `JobFlowInstancesConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html>`__
    """

    props: PropsDictType = {
        "AdditionalMasterSecurityGroups": ([str], False),
        "AdditionalSlaveSecurityGroups": ([str], False),
        "CoreInstanceFleet": (InstanceFleetConfigProperty, False),
        "CoreInstanceGroup": (InstanceGroupConfigProperty, False),
        "Ec2KeyName": (str, False),
        "Ec2SubnetId": (str, False),
        "Ec2SubnetIds": ([str], False),
        "EmrManagedMasterSecurityGroup": (str, False),
        "EmrManagedSlaveSecurityGroup": (str, False),
        "HadoopVersion": (str, False),
        "KeepJobFlowAliveWhenNoSteps": (boolean, False),
        "MasterInstanceFleet": (InstanceFleetConfigProperty, False),
        "MasterInstanceGroup": (InstanceGroupConfigProperty, False),
        "Placement": (PlacementType, False),
        "ServiceAccessSecurityGroup": (str, False),
        "TaskInstanceFleets": ([InstanceFleetConfigProperty], False),
        "TaskInstanceGroup": ([InstanceGroupConfigProperty], False),
        "TerminationProtected": (boolean, False),
    }


class KerberosAttributes(AWSProperty):
    """
    `KerberosAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-kerberosattributes.html>`__
    """

    props: PropsDictType = {
        "ADDomainJoinPassword": (str, False),
        "ADDomainJoinUser": (str, False),
        "CrossRealmTrustPrincipalPassword": (str, False),
        "KdcAdminPassword": (str, True),
        "Realm": (str, True),
    }


class ComputeLimits(AWSProperty):
    """
    `ComputeLimits <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-computelimits.html>`__
    """

    props: PropsDictType = {
        "MaximumCapacityUnits": (integer, True),
        "MaximumCoreCapacityUnits": (integer, False),
        "MaximumOnDemandCapacityUnits": (integer, False),
        "MinimumCapacityUnits": (integer, True),
        "UnitType": (str, True),
    }


class ManagedScalingPolicy(AWSProperty):
    """
    `ManagedScalingPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-managedscalingpolicy.html>`__
    """

    props: PropsDictType = {
        "ComputeLimits": (ComputeLimits, False),
    }


class HadoopJarStepConfig(AWSProperty):
    """
    `HadoopJarStepConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-step-hadoopjarstepconfig.html>`__
    """

    props: PropsDictType = {
        "Args": ([str], False),
        "Jar": (str, True),
        "MainClass": (str, False),
        "StepProperties": ([KeyValue], False),
    }


class StepConfig(AWSProperty):
    """
    `StepConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-stepconfig.html>`__
    """

    props: PropsDictType = {
        "ActionOnFailure": (str, False),
        "HadoopJarStep": (HadoopJarStepConfig, True),
        "Name": (str, True),
    }


class Cluster(AWSObject):
    """
    `Cluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html>`__
    """

    resource_type = "AWS::EMR::Cluster"

    props: PropsDictType = {
        "AdditionalInfo": (dict, False),
        "Applications": ([Application], False),
        "AutoScalingRole": (str, False),
        "BootstrapActions": ([BootstrapActionConfig], False),
        "Configurations": ([Configuration], False),
        "CustomAmiId": (str, False),
        "EbsRootVolumeSize": (integer, False),
        "Instances": (JobFlowInstancesConfig, True),
        "JobFlowRole": (str, True),
        "KerberosAttributes": (KerberosAttributes, False),
        "LogEncryptionKmsKeyId": (str, False),
        "LogUri": (str, False),
        "ManagedScalingPolicy": (ManagedScalingPolicy, False),
        "Name": (str, True),
        "ReleaseLabel": (str, False),
        "ScaleDownBehavior": (str, False),
        "SecurityConfiguration": (str, False),
        "ServiceRole": (str, True),
        "StepConcurrencyLevel": (integer, False),
        "Steps": ([StepConfig], False),
        "Tags": (Tags, False),
        "VisibleToAllUsers": (boolean, False),
    }


class InstanceFleetConfig(AWSObject):
    """
    `InstanceFleetConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html>`__
    """

    resource_type = "AWS::EMR::InstanceFleetConfig"

    props: PropsDictType = {
        "ClusterId": (str, True),
        "InstanceFleetType": (str, True),
        "InstanceTypeConfigs": ([InstanceTypeConfig], False),
        "LaunchSpecifications": (InstanceFleetProvisioningSpecifications, False),
        "Name": (str, False),
        "TargetOnDemandCapacity": (integer, False),
        "TargetSpotCapacity": (integer, False),
    }


class InstanceGroupConfig(AWSObject):
    """
    `InstanceGroupConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html>`__
    """

    resource_type = "AWS::EMR::InstanceGroupConfig"

    props: PropsDictType = {
        "AutoScalingPolicy": (AutoScalingPolicy, False),
        "BidPrice": (str, False),
        "Configurations": ([Configuration], False),
        "CustomAmiId": (str, False),
        "EbsConfiguration": (EbsConfiguration, False),
        "InstanceCount": (integer, True),
        "InstanceRole": (str, True),
        "InstanceType": (str, True),
        "JobFlowId": (str, True),
        "Market": (market_validator, False),
        "Name": (str, False),
    }


class SecurityConfiguration(AWSObject):
    """
    `SecurityConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html>`__
    """

    resource_type = "AWS::EMR::SecurityConfiguration"

    props: PropsDictType = {
        "Name": (str, False),
        "SecurityConfiguration": (dict, True),
    }


class Step(AWSObject):
    """
    `Step <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html>`__
    """

    resource_type = "AWS::EMR::Step"

    props: PropsDictType = {
        "ActionOnFailure": (action_on_failure_validator, True),
        "HadoopJarStep": (HadoopJarStepConfig, True),
        "JobFlowId": (str, True),
        "Name": (str, True),
    }


class Studio(AWSObject):
    """
    `Studio <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html>`__
    """

    resource_type = "AWS::EMR::Studio"

    props: PropsDictType = {
        "AuthMode": (str, True),
        "DefaultS3Location": (str, True),
        "Description": (str, False),
        "EngineSecurityGroupId": (str, True),
        "IdpAuthUrl": (str, False),
        "IdpRelayStateParameterName": (str, False),
        "Name": (str, True),
        "ServiceRole": (str, True),
        "SubnetIds": ([str], True),
        "Tags": (Tags, False),
        "UserRole": (str, False),
        "VpcId": (str, True),
        "WorkspaceSecurityGroupId": (str, True),
    }


class StudioSessionMapping(AWSObject):
    """
    `StudioSessionMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html>`__
    """

    resource_type = "AWS::EMR::StudioSessionMapping"

    props: PropsDictType = {
        "IdentityName": (str, True),
        "IdentityType": (str, True),
        "SessionPolicyArn": (str, True),
        "StudioId": (str, True),
    }
