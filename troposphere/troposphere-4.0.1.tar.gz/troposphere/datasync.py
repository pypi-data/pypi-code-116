# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import integer


class Agent(AWSObject):
    """
    `Agent <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html>`__
    """

    resource_type = "AWS::DataSync::Agent"

    props: PropsDictType = {
        "ActivationKey": (str, True),
        "AgentName": (str, False),
        "SecurityGroupArns": ([str], False),
        "SubnetArns": ([str], False),
        "Tags": (Tags, False),
        "VpcEndpointId": (str, False),
    }


class Ec2Config(AWSProperty):
    """
    `Ec2Config <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupArns": ([str], True),
        "SubnetArn": (str, True),
    }


class LocationEFS(AWSObject):
    """
    `LocationEFS <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html>`__
    """

    resource_type = "AWS::DataSync::LocationEFS"

    props: PropsDictType = {
        "Ec2Config": (Ec2Config, True),
        "EfsFilesystemArn": (str, True),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class LocationFSxLustre(AWSObject):
    """
    `LocationFSxLustre <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html>`__
    """

    resource_type = "AWS::DataSync::LocationFSxLustre"

    props: PropsDictType = {
        "FsxFilesystemArn": (str, True),
        "SecurityGroupArns": ([str], True),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class LocationFSxWindows(AWSObject):
    """
    `LocationFSxWindows <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html>`__
    """

    resource_type = "AWS::DataSync::LocationFSxWindows"

    props: PropsDictType = {
        "Domain": (str, False),
        "FsxFilesystemArn": (str, True),
        "Password": (str, True),
        "SecurityGroupArns": ([str], True),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
        "User": (str, True),
    }


class NameNode(AWSProperty):
    """
    `NameNode <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-namenode.html>`__
    """

    props: PropsDictType = {
        "Hostname": (str, True),
        "Port": (integer, True),
    }


class QopConfiguration(AWSProperty):
    """
    `QopConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-qopconfiguration.html>`__
    """

    props: PropsDictType = {
        "DataTransferProtection": (str, False),
        "RpcProtection": (str, False),
    }


class LocationHDFS(AWSObject):
    """
    `LocationHDFS <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html>`__
    """

    resource_type = "AWS::DataSync::LocationHDFS"

    props: PropsDictType = {
        "AgentArns": ([str], True),
        "AuthenticationType": (str, True),
        "BlockSize": (integer, False),
        "KerberosKeytab": (str, False),
        "KerberosKrb5Conf": (str, False),
        "KerberosPrincipal": (str, False),
        "KmsKeyProviderUri": (str, False),
        "NameNodes": ([NameNode], True),
        "QopConfiguration": (QopConfiguration, False),
        "ReplicationFactor": (integer, False),
        "SimpleUser": (str, False),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class MountOptions(AWSProperty):
    """
    `MountOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationsmb-mountoptions.html>`__
    """

    props: PropsDictType = {
        "Version": (str, False),
    }


class OnPremConfig(AWSProperty):
    """
    `OnPremConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-onpremconfig.html>`__
    """

    props: PropsDictType = {
        "AgentArns": ([str], True),
    }


class LocationNFS(AWSObject):
    """
    `LocationNFS <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html>`__
    """

    resource_type = "AWS::DataSync::LocationNFS"

    props: PropsDictType = {
        "MountOptions": (MountOptions, False),
        "OnPremConfig": (OnPremConfig, True),
        "ServerHostname": (str, True),
        "Subdirectory": (str, True),
        "Tags": (Tags, False),
    }


class LocationObjectStorage(AWSObject):
    """
    `LocationObjectStorage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html>`__
    """

    resource_type = "AWS::DataSync::LocationObjectStorage"

    props: PropsDictType = {
        "AccessKey": (str, False),
        "AgentArns": ([str], True),
        "BucketName": (str, True),
        "SecretKey": (str, False),
        "ServerHostname": (str, True),
        "ServerPort": (integer, False),
        "ServerProtocol": (str, False),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class S3Config(AWSProperty):
    """
    `S3Config <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locations3-s3config.html>`__
    """

    props: PropsDictType = {
        "BucketAccessRoleArn": (str, True),
    }


class LocationS3(AWSObject):
    """
    `LocationS3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html>`__
    """

    resource_type = "AWS::DataSync::LocationS3"

    props: PropsDictType = {
        "S3BucketArn": (str, True),
        "S3Config": (S3Config, True),
        "S3StorageClass": (str, False),
        "Subdirectory": (str, False),
        "Tags": (Tags, False),
    }


class LocationSMB(AWSObject):
    """
    `LocationSMB <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html>`__
    """

    resource_type = "AWS::DataSync::LocationSMB"

    props: PropsDictType = {
        "AgentArns": ([str], True),
        "Domain": (str, False),
        "MountOptions": (MountOptions, False),
        "Password": (str, True),
        "ServerHostname": (str, True),
        "Subdirectory": (str, True),
        "Tags": (Tags, False),
        "User": (str, True),
    }


class FilterRule(AWSProperty):
    """
    `FilterRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html>`__
    """

    props: PropsDictType = {
        "FilterType": (str, False),
        "Value": (str, False),
    }


class Options(AWSProperty):
    """
    `Options <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html>`__
    """

    props: PropsDictType = {
        "Atime": (str, False),
        "BytesPerSecond": (integer, False),
        "Gid": (str, False),
        "LogLevel": (str, False),
        "Mtime": (str, False),
        "OverwriteMode": (str, False),
        "PosixPermissions": (str, False),
        "PreserveDeletedFiles": (str, False),
        "PreserveDevices": (str, False),
        "SecurityDescriptorCopyFlags": (str, False),
        "TaskQueueing": (str, False),
        "TransferMode": (str, False),
        "Uid": (str, False),
        "VerifyMode": (str, False),
    }


class TaskSchedule(AWSProperty):
    """
    `TaskSchedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskschedule.html>`__
    """

    props: PropsDictType = {
        "ScheduleExpression": (str, True),
    }


class Task(AWSObject):
    """
    `Task <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html>`__
    """

    resource_type = "AWS::DataSync::Task"

    props: PropsDictType = {
        "CloudWatchLogGroupArn": (str, False),
        "DestinationLocationArn": (str, True),
        "Excludes": ([FilterRule], False),
        "Includes": ([FilterRule], False),
        "Name": (str, False),
        "Options": (Options, False),
        "Schedule": (TaskSchedule, False),
        "SourceLocationArn": (str, True),
        "Tags": (Tags, False),
    }
