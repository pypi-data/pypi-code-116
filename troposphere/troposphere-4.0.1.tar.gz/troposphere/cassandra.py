# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.cassandra import (
    validate_billingmode_mode,
    validate_clusteringkeycolumn_orderby,
)


class Keyspace(AWSObject):
    """
    `Keyspace <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html>`__
    """

    resource_type = "AWS::Cassandra::Keyspace"

    props: PropsDictType = {
        "KeyspaceName": (str, False),
        "Tags": (Tags, False),
    }


class ProvisionedThroughput(AWSProperty):
    """
    `ProvisionedThroughput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html>`__
    """

    props: PropsDictType = {
        "ReadCapacityUnits": (integer, True),
        "WriteCapacityUnits": (integer, True),
    }


class BillingMode(AWSProperty):
    """
    `BillingMode <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html>`__
    """

    props: PropsDictType = {
        "Mode": (validate_billingmode_mode, True),
        "ProvisionedThroughput": (ProvisionedThroughput, False),
    }


class Column(AWSProperty):
    """
    `Column <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html>`__
    """

    props: PropsDictType = {
        "ColumnName": (str, True),
        "ColumnType": (str, True),
    }


class ClusteringKeyColumn(AWSProperty):
    """
    `ClusteringKeyColumn <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html>`__
    """

    props: PropsDictType = {
        "Column": (Column, True),
        "OrderBy": (validate_clusteringkeycolumn_orderby, False),
    }


class EncryptionSpecification(AWSProperty):
    """
    `EncryptionSpecification <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html>`__
    """

    props: PropsDictType = {
        "EncryptionType": (str, True),
        "KmsKeyIdentifier": (str, False),
    }


class Table(AWSObject):
    """
    `Table <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html>`__
    """

    resource_type = "AWS::Cassandra::Table"

    props: PropsDictType = {
        "BillingMode": (BillingMode, False),
        "ClusteringKeyColumns": ([ClusteringKeyColumn], False),
        "DefaultTimeToLive": (integer, False),
        "EncryptionSpecification": (EncryptionSpecification, False),
        "KeyspaceName": (str, True),
        "PartitionKeyColumns": ([Column], True),
        "PointInTimeRecoveryEnabled": (boolean, False),
        "RegularColumns": ([Column], False),
        "TableName": (str, False),
        "Tags": (Tags, False),
    }
