# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class AcknowledgeFlow(AWSProperty):
    """
    `AcknowledgeFlow <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-acknowledgeflow.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
    }


class InitializationConfiguration(AWSProperty):
    """
    `InitializationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-initializationconfiguration.html>`__
    """

    props: PropsDictType = {
        "DisabledOnInitialization": (boolean, True),
    }


class AlarmCapabilities(AWSProperty):
    """
    `AlarmCapabilities <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmcapabilities.html>`__
    """

    props: PropsDictType = {
        "AcknowledgeFlow": (AcknowledgeFlow, False),
        "InitializationConfiguration": (InitializationConfiguration, False),
    }


class Payload(AWSProperty):
    """
    `Payload <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html>`__
    """

    props: PropsDictType = {
        "ContentExpression": (str, True),
        "Type": (str, True),
    }


class DynamoDB(AWSProperty):
    """
    `DynamoDB <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html>`__
    """

    props: PropsDictType = {
        "HashKeyField": (str, True),
        "HashKeyType": (str, False),
        "HashKeyValue": (str, True),
        "Operation": (str, False),
        "Payload": (Payload, False),
        "PayloadField": (str, False),
        "RangeKeyField": (str, False),
        "RangeKeyType": (str, False),
        "RangeKeyValue": (str, False),
        "TableName": (str, True),
    }


class DynamoDBv2(AWSProperty):
    """
    `DynamoDBv2 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html>`__
    """

    props: PropsDictType = {
        "Payload": (Payload, False),
        "TableName": (str, True),
    }


class Firehose(AWSProperty):
    """
    `Firehose <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html>`__
    """

    props: PropsDictType = {
        "DeliveryStreamName": (str, True),
        "Payload": (Payload, False),
        "Separator": (str, False),
    }


class IotEvents(AWSProperty):
    """
    `IotEvents <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html>`__
    """

    props: PropsDictType = {
        "InputName": (str, True),
        "Payload": (Payload, False),
    }


class AssetPropertyTimestamp(AWSProperty):
    """
    `AssetPropertyTimestamp <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html>`__
    """

    props: PropsDictType = {
        "OffsetInNanos": (str, False),
        "TimeInSeconds": (str, True),
    }


class AssetPropertyVariant(AWSProperty):
    """
    `AssetPropertyVariant <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html>`__
    """

    props: PropsDictType = {
        "BooleanValue": (str, False),
        "DoubleValue": (str, False),
        "IntegerValue": (str, False),
        "StringValue": (str, False),
    }


class AssetPropertyValue(AWSProperty):
    """
    `AssetPropertyValue <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html>`__
    """

    props: PropsDictType = {
        "Quality": (str, False),
        "Timestamp": (AssetPropertyTimestamp, False),
        "Value": (AssetPropertyVariant, True),
    }


class IotSiteWise(AWSProperty):
    """
    `IotSiteWise <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html>`__
    """

    props: PropsDictType = {
        "AssetId": (str, False),
        "EntryId": (str, False),
        "PropertyAlias": (str, False),
        "PropertyId": (str, False),
        "PropertyValue": (AssetPropertyValue, True),
    }


class IotTopicPublish(AWSProperty):
    """
    `IotTopicPublish <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html>`__
    """

    props: PropsDictType = {
        "MqttTopic": (str, True),
        "Payload": (Payload, False),
    }


class Lambda(AWSProperty):
    """
    `Lambda <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html>`__
    """

    props: PropsDictType = {
        "FunctionArn": (str, True),
        "Payload": (Payload, False),
    }


class Sns(AWSProperty):
    """
    `Sns <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html>`__
    """

    props: PropsDictType = {
        "Payload": (Payload, False),
        "TargetArn": (str, True),
    }


class Sqs(AWSProperty):
    """
    `Sqs <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html>`__
    """

    props: PropsDictType = {
        "Payload": (Payload, False),
        "QueueUrl": (str, True),
        "UseBase64": (boolean, False),
    }


class AlarmAction(AWSProperty):
    """
    `AlarmAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html>`__
    """

    props: PropsDictType = {
        "DynamoDB": (DynamoDB, False),
        "DynamoDBv2": (DynamoDBv2, False),
        "Firehose": (Firehose, False),
        "IotEvents": (IotEvents, False),
        "IotSiteWise": (IotSiteWise, False),
        "IotTopicPublish": (IotTopicPublish, False),
        "Lambda": (Lambda, False),
        "Sns": (Sns, False),
        "Sqs": (Sqs, False),
    }


class AlarmEventActions(AWSProperty):
    """
    `AlarmEventActions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmeventactions.html>`__
    """

    props: PropsDictType = {
        "AlarmActions": ([AlarmAction], False),
    }


class SimpleRule(AWSProperty):
    """
    `SimpleRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-simplerule.html>`__
    """

    props: PropsDictType = {
        "ComparisonOperator": (str, True),
        "InputProperty": (str, True),
        "Threshold": (str, True),
    }


class AlarmRule(AWSProperty):
    """
    `AlarmRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmrule.html>`__
    """

    props: PropsDictType = {
        "SimpleRule": (SimpleRule, False),
    }


class AlarmModel(AWSObject):
    """
    `AlarmModel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html>`__
    """

    resource_type = "AWS::IoTEvents::AlarmModel"

    props: PropsDictType = {
        "AlarmCapabilities": (AlarmCapabilities, False),
        "AlarmEventActions": (AlarmEventActions, False),
        "AlarmModelDescription": (str, False),
        "AlarmModelName": (str, False),
        "AlarmRule": (AlarmRule, True),
        "Key": (str, False),
        "RoleArn": (str, True),
        "Severity": (integer, False),
        "Tags": (Tags, False),
    }


class ClearTimer(AWSProperty):
    """
    `ClearTimer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-cleartimer.html>`__
    """

    props: PropsDictType = {
        "TimerName": (str, True),
    }


class ResetTimer(AWSProperty):
    """
    `ResetTimer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-resettimer.html>`__
    """

    props: PropsDictType = {
        "TimerName": (str, True),
    }


class SetTimer(AWSProperty):
    """
    `SetTimer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html>`__
    """

    props: PropsDictType = {
        "DurationExpression": (str, False),
        "Seconds": (integer, False),
        "TimerName": (str, True),
    }


class SetVariable(AWSProperty):
    """
    `SetVariable <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html>`__
    """

    props: PropsDictType = {
        "Value": (str, True),
        "VariableName": (str, True),
    }


class Action(AWSProperty):
    """
    `Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html>`__
    """

    props: PropsDictType = {
        "ClearTimer": (ClearTimer, False),
        "DynamoDB": (DynamoDB, False),
        "DynamoDBv2": (DynamoDBv2, False),
        "Firehose": (Firehose, False),
        "IotEvents": (IotEvents, False),
        "IotSiteWise": (IotSiteWise, False),
        "IotTopicPublish": (IotTopicPublish, False),
        "Lambda": (Lambda, False),
        "ResetTimer": (ResetTimer, False),
        "SetTimer": (SetTimer, False),
        "SetVariable": (SetVariable, False),
        "Sns": (Sns, False),
        "Sqs": (Sqs, False),
    }


class Event(AWSProperty):
    """
    `Event <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html>`__
    """

    props: PropsDictType = {
        "Actions": ([Action], False),
        "Condition": (str, False),
        "EventName": (str, True),
    }


class OnEnter(AWSProperty):
    """
    `OnEnter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onenter.html>`__
    """

    props: PropsDictType = {
        "Events": ([Event], False),
    }


class OnExit(AWSProperty):
    """
    `OnExit <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onexit.html>`__
    """

    props: PropsDictType = {
        "Events": ([Event], False),
    }


class TransitionEvent(AWSProperty):
    """
    `TransitionEvent <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html>`__
    """

    props: PropsDictType = {
        "Actions": ([Action], False),
        "Condition": (str, True),
        "EventName": (str, True),
        "NextState": (str, True),
    }


class OnInput(AWSProperty):
    """
    `OnInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html>`__
    """

    props: PropsDictType = {
        "Events": ([Event], False),
        "TransitionEvents": ([TransitionEvent], False),
    }


class State(AWSProperty):
    """
    `State <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html>`__
    """

    props: PropsDictType = {
        "OnEnter": (OnEnter, False),
        "OnExit": (OnExit, False),
        "OnInput": (OnInput, False),
        "StateName": (str, True),
    }


class DetectorModelDefinition(AWSProperty):
    """
    `DetectorModelDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html>`__
    """

    props: PropsDictType = {
        "InitialStateName": (str, True),
        "States": ([State], True),
    }


class DetectorModel(AWSObject):
    """
    `DetectorModel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html>`__
    """

    resource_type = "AWS::IoTEvents::DetectorModel"

    props: PropsDictType = {
        "DetectorModelDefinition": (DetectorModelDefinition, True),
        "DetectorModelDescription": (str, False),
        "DetectorModelName": (str, False),
        "EvaluationMethod": (str, False),
        "Key": (str, False),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
    }


class Attribute(AWSProperty):
    """
    `Attribute <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-attribute.html>`__
    """

    props: PropsDictType = {
        "JsonPath": (str, True),
    }


class InputDefinition(AWSProperty):
    """
    `InputDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-inputdefinition.html>`__
    """

    props: PropsDictType = {
        "Attributes": ([Attribute], True),
    }


class Input(AWSObject):
    """
    `Input <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html>`__
    """

    resource_type = "AWS::IoTEvents::Input"

    props: PropsDictType = {
        "InputDefinition": (InputDefinition, True),
        "InputDescription": (str, False),
        "InputName": (str, False),
        "Tags": (Tags, False),
    }
