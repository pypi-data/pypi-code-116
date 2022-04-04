# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.elasticache import (
    validate_cache_cluster,
    validate_network_port,
    validate_node_group_id,
    validate_replication_group,
)


class CloudWatchLogsDestinationDetails(AWSProperty):
    """
    `CloudWatchLogsDestinationDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-cloudwatchlogsdestinationdetails.html>`__
    """

    props: PropsDictType = {
        "LogGroup": (str, True),
    }


class KinesisFirehoseDestinationDetails(AWSProperty):
    """
    `KinesisFirehoseDestinationDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-kinesisfirehosedestinationdetails.html>`__
    """

    props: PropsDictType = {
        "DeliveryStream": (str, True),
    }


class DestinationDetails(AWSProperty):
    """
    `DestinationDetails <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-destinationdetails.html>`__
    """

    props: PropsDictType = {
        "CloudWatchLogsDetails": (CloudWatchLogsDestinationDetails, False),
        "KinesisFirehoseDetails": (KinesisFirehoseDestinationDetails, False),
    }


class LogDeliveryConfigurationRequest(AWSProperty):
    """
    `LogDeliveryConfigurationRequest <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html>`__
    """

    props: PropsDictType = {
        "DestinationDetails": (DestinationDetails, True),
        "DestinationType": (str, True),
        "LogFormat": (str, True),
        "LogType": (str, True),
    }


class CacheCluster(AWSObject):
    """
    `CacheCluster <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html>`__
    """

    resource_type = "AWS::ElastiCache::CacheCluster"

    props: PropsDictType = {
        "AZMode": (str, False),
        "AutoMinorVersionUpgrade": (boolean, False),
        "CacheNodeType": (str, True),
        "CacheParameterGroupName": (str, False),
        "CacheSecurityGroupNames": ([str], False),
        "CacheSubnetGroupName": (str, False),
        "ClusterName": (str, False),
        "Engine": (str, True),
        "EngineVersion": (str, False),
        "LogDeliveryConfigurations": ([LogDeliveryConfigurationRequest], False),
        "NotificationTopicArn": (str, False),
        "NumCacheNodes": (integer, True),
        "Port": (integer, False),
        "PreferredAvailabilityZone": (str, False),
        "PreferredAvailabilityZones": ([str], False),
        "PreferredMaintenanceWindow": (str, False),
        "SnapshotArns": ([str], False),
        "SnapshotName": (str, False),
        "SnapshotRetentionLimit": (integer, False),
        "SnapshotWindow": (str, False),
        "Tags": (Tags, False),
        "VpcSecurityGroupIds": ([str], False),
    }

    def validate(self):
        validate_cache_cluster(self)


class GlobalReplicationGroupMember(AWSProperty):
    """
    `GlobalReplicationGroupMember <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html>`__
    """

    props: PropsDictType = {
        "ReplicationGroupId": (str, False),
        "ReplicationGroupRegion": (str, False),
        "Role": (str, False),
    }


class ReshardingConfiguration(AWSProperty):
    """
    `ReshardingConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration.html>`__
    """

    props: PropsDictType = {
        "NodeGroupId": (str, False),
        "PreferredAvailabilityZones": ([str], False),
    }


class RegionalConfiguration(AWSProperty):
    """
    `RegionalConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html>`__
    """

    props: PropsDictType = {
        "ReplicationGroupId": (str, False),
        "ReplicationGroupRegion": (str, False),
        "ReshardingConfigurations": ([ReshardingConfiguration], False),
    }


class GlobalReplicationGroup(AWSObject):
    """
    `GlobalReplicationGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html>`__
    """

    resource_type = "AWS::ElastiCache::GlobalReplicationGroup"

    props: PropsDictType = {
        "AutomaticFailoverEnabled": (boolean, False),
        "CacheNodeType": (str, False),
        "CacheParameterGroupName": (str, False),
        "EngineVersion": (str, False),
        "GlobalNodeGroupCount": (integer, False),
        "GlobalReplicationGroupDescription": (str, False),
        "GlobalReplicationGroupIdSuffix": (str, False),
        "Members": ([GlobalReplicationGroupMember], True),
        "RegionalConfigurations": ([RegionalConfiguration], False),
    }


class ParameterGroup(AWSObject):
    """
    `ParameterGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html>`__
    """

    resource_type = "AWS::ElastiCache::ParameterGroup"

    props: PropsDictType = {
        "CacheParameterGroupFamily": (str, True),
        "Description": (str, True),
        "Properties": (dict, False),
        "Tags": (Tags, False),
    }


class NodeGroupConfiguration(AWSProperty):
    """
    `NodeGroupConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html>`__
    """

    props: PropsDictType = {
        "NodeGroupId": (validate_node_group_id, False),
        "PrimaryAvailabilityZone": (str, False),
        "ReplicaAvailabilityZones": ([str], False),
        "ReplicaCount": (integer, False),
        "Slots": (str, False),
    }


class ReplicationGroup(AWSObject):
    """
    `ReplicationGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html>`__
    """

    resource_type = "AWS::ElastiCache::ReplicationGroup"

    props: PropsDictType = {
        "AtRestEncryptionEnabled": (boolean, False),
        "AuthToken": (str, False),
        "AutoMinorVersionUpgrade": (boolean, False),
        "AutomaticFailoverEnabled": (boolean, False),
        "CacheNodeType": (str, False),
        "CacheParameterGroupName": (str, False),
        "CacheSecurityGroupNames": ([str], False),
        "CacheSubnetGroupName": (str, False),
        "DataTieringEnabled": (boolean, False),
        "Engine": (str, False),
        "EngineVersion": (str, False),
        "GlobalReplicationGroupId": (str, False),
        "KmsKeyId": (str, False),
        "LogDeliveryConfigurations": ([LogDeliveryConfigurationRequest], False),
        "MultiAZEnabled": (boolean, False),
        "NodeGroupConfiguration": ([NodeGroupConfiguration], False),
        "NotificationTopicArn": (str, False),
        "NumCacheClusters": (integer, False),
        "NumNodeGroups": (integer, False),
        "Port": (validate_network_port, False),
        "PreferredCacheClusterAZs": ([str], False),
        "PreferredMaintenanceWindow": (str, False),
        "PrimaryClusterId": (str, False),
        "ReplicasPerNodeGroup": (integer, False),
        "ReplicationGroupDescription": (str, True),
        "ReplicationGroupId": (str, False),
        "SecurityGroupIds": ([str], False),
        "SnapshotArns": ([str], False),
        "SnapshotName": (str, False),
        "SnapshotRetentionLimit": (integer, False),
        "SnapshotWindow": (str, False),
        "SnapshottingClusterId": (str, False),
        "Tags": (Tags, False),
        "TransitEncryptionEnabled": (boolean, False),
        "UserGroupIds": ([str], False),
    }

    def validate(self):
        validate_replication_group(self)


class SecurityGroup(AWSObject):
    """
    `SecurityGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group.html>`__
    """

    resource_type = "AWS::ElastiCache::SecurityGroup"

    props: PropsDictType = {
        "Description": (str, True),
        "Tags": (Tags, False),
    }


class SecurityGroupIngress(AWSObject):
    """
    `SecurityGroupIngress <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html>`__
    """

    resource_type = "AWS::ElastiCache::SecurityGroupIngress"

    props: PropsDictType = {
        "CacheSecurityGroupName": (str, True),
        "EC2SecurityGroupName": (str, True),
        "EC2SecurityGroupOwnerId": (str, False),
    }


class SubnetGroup(AWSObject):
    """
    `SubnetGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html>`__
    """

    resource_type = "AWS::ElastiCache::SubnetGroup"

    props: PropsDictType = {
        "CacheSubnetGroupName": (str, False),
        "Description": (str, True),
        "SubnetIds": ([str], True),
        "Tags": (Tags, False),
    }


class User(AWSObject):
    """
    `User <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html>`__
    """

    resource_type = "AWS::ElastiCache::User"

    props: PropsDictType = {
        "AccessString": (str, False),
        "Engine": (str, True),
        "NoPasswordRequired": (boolean, False),
        "Passwords": ([str], False),
        "UserId": (str, True),
        "UserName": (str, True),
    }


class UserGroup(AWSObject):
    """
    `UserGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html>`__
    """

    resource_type = "AWS::ElastiCache::UserGroup"

    props: PropsDictType = {
        "Engine": (str, True),
        "UserGroupId": (str, True),
        "UserIds": ([str], False),
    }
