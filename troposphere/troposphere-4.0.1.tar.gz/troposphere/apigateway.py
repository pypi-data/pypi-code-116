# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.apigateway import (
    dict_or_string,
    validate_authorizer_ttl,
    validate_gateway_response_type,
    validate_model,
    validate_tags_or_list,
    validate_timeout_in_millis,
)


class Account(AWSObject):
    """
    `Account <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-account.html>`__
    """

    resource_type = "AWS::ApiGateway::Account"

    props: PropsDictType = {
        "CloudWatchRoleArn": (str, False),
    }


class StageKey(AWSProperty):
    """
    `StageKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-apikey-stagekey.html>`__
    """

    props: PropsDictType = {
        "RestApiId": (str, False),
        "StageName": (str, False),
    }


class ApiKey(AWSObject):
    """
    `ApiKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.html>`__
    """

    resource_type = "AWS::ApiGateway::ApiKey"

    props: PropsDictType = {
        "CustomerId": (str, False),
        "Description": (str, False),
        "Enabled": (boolean, False),
        "GenerateDistinctId": (boolean, False),
        "Name": (str, False),
        "StageKeys": ([StageKey], False),
        "Tags": (Tags, False),
        "Value": (str, False),
    }


class Authorizer(AWSObject):
    """
    `Authorizer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html>`__
    """

    resource_type = "AWS::ApiGateway::Authorizer"

    props: PropsDictType = {
        "AuthType": (str, False),
        "AuthorizerCredentials": (str, False),
        "AuthorizerResultTtlInSeconds": (validate_authorizer_ttl, False),
        "AuthorizerUri": (str, False),
        "IdentitySource": (str, False),
        "IdentityValidationExpression": (str, False),
        "Name": (str, True),
        "ProviderARNs": ([str], False),
        "RestApiId": (str, True),
        "Type": (str, True),
    }


class BasePathMapping(AWSObject):
    """
    `BasePathMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-basepathmapping.html>`__
    """

    resource_type = "AWS::ApiGateway::BasePathMapping"

    props: PropsDictType = {
        "BasePath": (str, False),
        "DomainName": (str, True),
        "Id": (str, False),
        "RestApiId": (str, False),
        "Stage": (str, False),
    }


class ClientCertificate(AWSObject):
    """
    `ClientCertificate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-clientcertificate.html>`__
    """

    resource_type = "AWS::ApiGateway::ClientCertificate"

    props: PropsDictType = {
        "Description": (str, False),
        "Tags": (Tags, False),
    }


class DeploymentCanarySettings(AWSProperty):
    """
    `DeploymentCanarySettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-deploymentcanarysettings.html>`__
    """

    props: PropsDictType = {
        "PercentTraffic": (double, False),
        "StageVariableOverrides": (dict, False),
        "UseStageCache": (boolean, False),
    }


class AccessLogSetting(AWSProperty):
    """
    `AccessLogSetting <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-accesslogsetting.html>`__
    """

    props: PropsDictType = {
        "DestinationArn": (str, False),
        "Format": (str, False),
    }


class MethodSetting(AWSProperty):
    """
    `MethodSetting <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.html>`__
    """

    props: PropsDictType = {
        "CacheDataEncrypted": (boolean, False),
        "CacheTtlInSeconds": (integer, False),
        "CachingEnabled": (boolean, False),
        "DataTraceEnabled": (boolean, False),
        "HttpMethod": (str, False),
        "LoggingLevel": (str, False),
        "MetricsEnabled": (boolean, False),
        "ResourcePath": (str, False),
        "ThrottlingBurstLimit": (integer, False),
        "ThrottlingRateLimit": (double, False),
    }


class StageDescription(AWSProperty):
    """
    `StageDescription <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-stagedescription.html>`__
    """

    props: PropsDictType = {
        "AccessLogSetting": (AccessLogSetting, False),
        "CacheClusterEnabled": (boolean, False),
        "CacheClusterSize": (str, False),
        "CacheDataEncrypted": (boolean, False),
        "CacheTtlInSeconds": (integer, False),
        "CachingEnabled": (boolean, False),
        "CanarySetting": (DeploymentCanarySettings, False),
        "ClientCertificateId": (str, False),
        "DataTraceEnabled": (boolean, False),
        "Description": (str, False),
        "DocumentationVersion": (str, False),
        "LoggingLevel": (str, False),
        "MethodSettings": ([MethodSetting], False),
        "MetricsEnabled": (boolean, False),
        "Tags": (validate_tags_or_list, False),
        "ThrottlingBurstLimit": (integer, False),
        "ThrottlingRateLimit": (double, False),
        "TracingEnabled": (boolean, False),
        "Variables": (dict, False),
    }


class Deployment(AWSObject):
    """
    `Deployment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-deployment.html>`__
    """

    resource_type = "AWS::ApiGateway::Deployment"

    props: PropsDictType = {
        "DeploymentCanarySettings": (DeploymentCanarySettings, False),
        "Description": (str, False),
        "RestApiId": (str, True),
        "StageDescription": (StageDescription, False),
        "StageName": (str, False),
    }


class Location(AWSProperty):
    """
    `Location <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-documentationpart-location.html>`__
    """

    props: PropsDictType = {
        "Method": (str, False),
        "Name": (str, False),
        "Path": (str, False),
        "StatusCode": (str, False),
        "Type": (str, False),
    }


class DocumentationPart(AWSObject):
    """
    `DocumentationPart <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationpart.html>`__
    """

    resource_type = "AWS::ApiGateway::DocumentationPart"

    props: PropsDictType = {
        "Location": (Location, True),
        "Properties": (str, True),
        "RestApiId": (str, True),
    }


class DocumentationVersion(AWSObject):
    """
    `DocumentationVersion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationversion.html>`__
    """

    resource_type = "AWS::ApiGateway::DocumentationVersion"

    props: PropsDictType = {
        "Description": (str, False),
        "DocumentationVersion": (str, True),
        "RestApiId": (str, True),
    }


class EndpointConfiguration(AWSProperty):
    """
    `EndpointConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-restapi-endpointconfiguration.html>`__
    """

    props: PropsDictType = {
        "Types": ([str], False),
        "VpcEndpointIds": ([str], False),
    }


class MutualTlsAuthentication(AWSProperty):
    """
    `MutualTlsAuthentication <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-domainname-mutualtlsauthentication.html>`__
    """

    props: PropsDictType = {
        "TruststoreUri": (str, False),
        "TruststoreVersion": (str, False),
    }


class DomainName(AWSObject):
    """
    `DomainName <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html>`__
    """

    resource_type = "AWS::ApiGateway::DomainName"

    props: PropsDictType = {
        "CertificateArn": (str, False),
        "DomainName": (str, False),
        "EndpointConfiguration": (EndpointConfiguration, False),
        "MutualTlsAuthentication": (MutualTlsAuthentication, False),
        "OwnershipVerificationCertificateArn": (str, False),
        "RegionalCertificateArn": (str, False),
        "SecurityPolicy": (str, False),
        "Tags": (Tags, False),
    }


class GatewayResponse(AWSObject):
    """
    `GatewayResponse <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-gatewayresponse.html>`__
    """

    resource_type = "AWS::ApiGateway::GatewayResponse"

    props: PropsDictType = {
        "ResponseParameters": (dict, False),
        "ResponseTemplates": (dict, False),
        "ResponseType": (validate_gateway_response_type, True),
        "RestApiId": (str, True),
        "StatusCode": (str, False),
    }


class IntegrationResponse(AWSProperty):
    """
    `IntegrationResponse <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration-integrationresponse.html>`__
    """

    props: PropsDictType = {
        "ContentHandling": (str, False),
        "ResponseParameters": (dict, False),
        "ResponseTemplates": (dict, False),
        "SelectionPattern": (str, False),
        "StatusCode": (str, True),
    }


class Integration(AWSProperty):
    """
    `Integration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-integration.html>`__
    """

    props: PropsDictType = {
        "CacheKeyParameters": ([str], False),
        "CacheNamespace": (str, False),
        "ConnectionId": (str, False),
        "ConnectionType": (str, False),
        "ContentHandling": (str, False),
        "Credentials": (str, False),
        "IntegrationHttpMethod": (str, False),
        "IntegrationResponses": ([IntegrationResponse], False),
        "PassthroughBehavior": (str, False),
        "RequestParameters": (dict, False),
        "RequestTemplates": (dict, False),
        "TimeoutInMillis": (validate_timeout_in_millis, False),
        "Type": (str, False),
        "Uri": (str, False),
    }


class MethodResponse(AWSProperty):
    """
    `MethodResponse <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apitgateway-method-methodresponse.html>`__
    """

    props: PropsDictType = {
        "ResponseModels": (dict, False),
        "ResponseParameters": (dict, False),
        "StatusCode": (str, True),
    }


class Method(AWSObject):
    """
    `Method <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html>`__
    """

    resource_type = "AWS::ApiGateway::Method"

    props: PropsDictType = {
        "ApiKeyRequired": (boolean, False),
        "AuthorizationScopes": ([str], False),
        "AuthorizationType": (str, False),
        "AuthorizerId": (str, False),
        "HttpMethod": (str, True),
        "Integration": (Integration, False),
        "MethodResponses": ([MethodResponse], False),
        "OperationName": (str, False),
        "RequestModels": (dict, False),
        "RequestParameters": (dict, False),
        "RequestValidatorId": (str, False),
        "ResourceId": (str, True),
        "RestApiId": (str, True),
    }


class Model(AWSObject):
    """
    `Model <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-model.html>`__
    """

    resource_type = "AWS::ApiGateway::Model"

    props: PropsDictType = {
        "ContentType": (str, False),
        "Description": (str, False),
        "Name": (str, False),
        "RestApiId": (str, True),
        "Schema": (dict_or_string, False),
    }

    def validate(self):
        validate_model(self)


class RequestValidator(AWSObject):
    """
    `RequestValidator <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-requestvalidator.html>`__
    """

    resource_type = "AWS::ApiGateway::RequestValidator"

    props: PropsDictType = {
        "Name": (str, False),
        "RestApiId": (str, True),
        "ValidateRequestBody": (boolean, False),
        "ValidateRequestParameters": (boolean, False),
    }


class Resource(AWSObject):
    """
    `Resource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-resource.html>`__
    """

    resource_type = "AWS::ApiGateway::Resource"

    props: PropsDictType = {
        "ParentId": (str, True),
        "PathPart": (str, True),
        "RestApiId": (str, True),
    }


class S3Location(AWSProperty):
    """
    `S3Location <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-restapi-s3location.html>`__
    """

    props: PropsDictType = {
        "Bucket": (str, False),
        "ETag": (str, False),
        "Key": (str, False),
        "Version": (str, False),
    }


class RestApi(AWSObject):
    """
    `RestApi <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html>`__
    """

    resource_type = "AWS::ApiGateway::RestApi"

    props: PropsDictType = {
        "ApiKeySourceType": (str, False),
        "BinaryMediaTypes": ([str], False),
        "Body": (dict, False),
        "BodyS3Location": (S3Location, False),
        "CloneFrom": (str, False),
        "Description": (str, False),
        "DisableExecuteApiEndpoint": (boolean, False),
        "EndpointConfiguration": (EndpointConfiguration, False),
        "FailOnWarnings": (boolean, False),
        "MinimumCompressionSize": (integer, False),
        "Mode": (str, False),
        "Name": (str, False),
        "Parameters": (dict, False),
        "Policy": (dict, False),
        "Tags": (Tags, False),
    }


class StageCanarySetting(AWSProperty):
    """
    `StageCanarySetting <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-canarysetting.html>`__
    """

    props: PropsDictType = {
        "DeploymentId": (str, False),
        "PercentTraffic": (double, False),
        "StageVariableOverrides": (dict, False),
        "UseStageCache": (boolean, False),
    }


class Stage(AWSObject):
    """
    `Stage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html>`__
    """

    resource_type = "AWS::ApiGateway::Stage"

    props: PropsDictType = {
        "AccessLogSetting": (AccessLogSetting, False),
        "CacheClusterEnabled": (boolean, False),
        "CacheClusterSize": (str, False),
        "CanarySetting": (StageCanarySetting, False),
        "ClientCertificateId": (str, False),
        "DeploymentId": (str, False),
        "Description": (str, False),
        "DocumentationVersion": (str, False),
        "MethodSettings": ([MethodSetting], False),
        "RestApiId": (str, True),
        "StageName": (str, False),
        "Tags": (validate_tags_or_list, False),
        "TracingEnabled": (boolean, False),
        "Variables": (dict, False),
    }


class ThrottleSettings(AWSProperty):
    """
    `ThrottleSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-throttlesettings.html>`__
    """

    props: PropsDictType = {
        "BurstLimit": (integer, False),
        "RateLimit": (double, False),
    }


class ApiStage(AWSProperty):
    """
    `ApiStage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-apistage.html>`__
    """

    props: PropsDictType = {
        "ApiId": (str, False),
        "Stage": (str, False),
        "Throttle": (dict, False),
    }


class QuotaSettings(AWSProperty):
    """
    `QuotaSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-usageplan-quotasettings.html>`__
    """

    props: PropsDictType = {
        "Limit": (integer, False),
        "Offset": (integer, False),
        "Period": (str, False),
    }


class UsagePlan(AWSObject):
    """
    `UsagePlan <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html>`__
    """

    resource_type = "AWS::ApiGateway::UsagePlan"

    props: PropsDictType = {
        "ApiStages": ([ApiStage], False),
        "Description": (str, False),
        "Quota": (QuotaSettings, False),
        "Tags": (Tags, False),
        "Throttle": (ThrottleSettings, False),
        "UsagePlanName": (str, False),
    }


class UsagePlanKey(AWSObject):
    """
    `UsagePlanKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplankey.html>`__
    """

    resource_type = "AWS::ApiGateway::UsagePlanKey"

    props: PropsDictType = {
        "KeyId": (str, True),
        "KeyType": (str, True),
        "UsagePlanId": (str, True),
    }


class VpcLink(AWSObject):
    """
    `VpcLink <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-vpclink.html>`__
    """

    resource_type = "AWS::ApiGateway::VpcLink"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, True),
        "Tags": (Tags, False),
        "TargetArns": ([str], True),
    }


class CanarySetting(AWSProperty):
    """
    `CanarySetting <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-deployment-canarysetting.html>`__
    """

    props: PropsDictType = {
        "PercentTraffic": (double, False),
        "StageVariableOverrides": (dict, False),
        "UseStageCache": (boolean, False),
    }
