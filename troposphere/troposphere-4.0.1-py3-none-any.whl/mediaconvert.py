# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import integer


class AccelerationSettings(AWSProperty):
    """
    `AccelerationSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-accelerationsettings.html>`__
    """

    props: PropsDictType = {
        "Mode": (str, True),
    }


class HopDestination(AWSProperty):
    """
    `HopDestination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html>`__
    """

    props: PropsDictType = {
        "Priority": (integer, False),
        "Queue": (str, False),
        "WaitMinutes": (integer, False),
    }


class JobTemplate(AWSObject):
    """
    `JobTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html>`__
    """

    resource_type = "AWS::MediaConvert::JobTemplate"

    props: PropsDictType = {
        "AccelerationSettings": (AccelerationSettings, False),
        "Category": (str, False),
        "Description": (str, False),
        "HopDestinations": ([HopDestination], False),
        "Name": (str, False),
        "Priority": (integer, False),
        "Queue": (str, False),
        "SettingsJson": (dict, True),
        "StatusUpdateInterval": (str, False),
        "Tags": (dict, False),
    }


class Preset(AWSObject):
    """
    `Preset <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html>`__
    """

    resource_type = "AWS::MediaConvert::Preset"

    props: PropsDictType = {
        "Category": (str, False),
        "Description": (str, False),
        "Name": (str, False),
        "SettingsJson": (dict, True),
        "Tags": (dict, False),
    }


class Queue(AWSObject):
    """
    `Queue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html>`__
    """

    resource_type = "AWS::MediaConvert::Queue"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, False),
        "PricingPlan": (str, False),
        "Status": (str, False),
        "Tags": (dict, False),
    }
