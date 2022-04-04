# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags


class Assignment(AWSObject):
    """
    `Assignment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html>`__
    """

    resource_type = "AWS::SSO::Assignment"

    props: PropsDictType = {
        "InstanceArn": (str, True),
        "PermissionSetArn": (str, True),
        "PrincipalId": (str, True),
        "PrincipalType": (str, True),
        "TargetId": (str, True),
        "TargetType": (str, True),
    }


class AccessControlAttributeValue(AWSProperty):
    """
    `AccessControlAttributeValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html>`__
    """

    props: PropsDictType = {
        "Source": ([str], True),
    }


class AccessControlAttribute(AWSProperty):
    """
    `AccessControlAttribute <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Value": (AccessControlAttributeValue, True),
    }


class InstanceAccessControlAttributeConfiguration(AWSObject):
    """
    `InstanceAccessControlAttributeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html>`__
    """

    resource_type = "AWS::SSO::InstanceAccessControlAttributeConfiguration"

    props: PropsDictType = {
        "AccessControlAttributes": ([AccessControlAttribute], False),
        "InstanceArn": (str, True),
    }


class PermissionSet(AWSObject):
    """
    `PermissionSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html>`__
    """

    resource_type = "AWS::SSO::PermissionSet"

    props: PropsDictType = {
        "Description": (str, False),
        "InlinePolicy": (dict, False),
        "InstanceArn": (str, True),
        "ManagedPolicies": ([str], False),
        "Name": (str, True),
        "RelayStateType": (str, False),
        "SessionDuration": (str, False),
        "Tags": (Tags, False),
    }
