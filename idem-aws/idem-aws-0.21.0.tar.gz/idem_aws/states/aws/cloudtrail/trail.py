"""
Autogenerated using `pop-create-idem <https://gitlab.com/saltstack/pop/pop-create-idem>`__

hub.exec.boto3.client.cloudtrail.create_trail
hub.exec.boto3.client.cloudtrail.delete_trail
hub.exec.boto3.client.cloudtrail.describe_trails
hub.exec.boto3.client.cloudtrail.get_trail
hub.exec.boto3.client.cloudtrail.list_trails
hub.exec.boto3.client.cloudtrail.update_trail
hub.exec.boto3.client.cloudtrail.start_logging
hub.exec.boto3.client.cloudtrail.stop_logging
hub.exec.boto3.client.cloudtrail.get_trail_status
hub.exec.boto3.client.cloudtrail.get_trail
hub.exec.boto3.client.cloudtrail.list_trails
"""
import copy
from typing import Any
from typing import Dict
from typing import List

__contracts__ = ["resource"]


async def present(
    hub,
    ctx,
    name: str,
    s3_bucket_name: str,
    resource_id: str = None,
    s3_key_prefix: str = None,
    sns_topic_name: str = None,
    include_global_service_events: bool = None,
    is_multi_region_trail: bool = None,
    enable_logfile_validation: bool = None,
    cloud_watch_logs_loggroup_arn: str = None,
    cloud_watch_logs_role_arn: str = None,
    kms_key_id: str = None,
    is_organization_trail: bool = None,
    tags: List = None,
    is_logging: bool = None,
    insight_selectors: List = None,
    event_selectors: List = None,
    advanced_event_selectors: List = None,
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket.

    Args:
        name (Text): An Idem name of the resource
            Specifies the name of the trail. The name must meet the following requirements: Contain only ASCII letters
            (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-) Start with a letter or number, and
            end with a letter or number Be between 3 and 128 characters
            Have no adjacent periods, underscores or dashes. Names like my-_namespace and my--namespace are not valid.
            Not be in IP address format (for example, 192.168.5.4)

        resource_id (Text, Optional): Trail name to identify the resource

        s3_bucket_name (Text):
            Specifies the name of the Amazon S3 bucket designated for publishing log files. See Amazon S3 Bucket
            Naming Requirements .

        s3_key_prefix (Text, Optional): Specifies the Amazon S3 key prefix that comes after the name of the bucket you have
            designated for log file delivery. For more information, see Finding Your CloudTrail Log Files .
             The maximum length is 200 characters.

        sns_topic_name (Text, Optional) : Specifies the name of the Amazon SNS topic defined for notification of log file
            delivery. The maximum length is 256 characters.

        include_global_service_events (boolean, Optional): Specifies whether the trail is publishing events from global services
            such as IAM to the log files.

        is_multi_region_trail (boolean, Optional) : Specifies whether the trail is created in the current region or in all regions.
            The default is false, which creates a trail only in the region where you are signed in. As a best practice,
            consider creating trails that log events in all regions.

        enable_logfile_validation (boolean, Optional): Specifies whether log file integrity validation is enabled.
            The default is false.

        cloud_watch_logs_loggroup_arn (Text, Optional) : Specifies a log group name using an Amazon Resource Name (ARN), a unique
            identifier that represents the log group to which CloudTrail logs will be delivered. Not required unless you
            specify CloudWatchLogsRoleArn .

        cloud_watch_logs_role_arn (Text, Optional) : Specifies the role for the CloudWatch Logs endpoint to assume to write to a
            user's log group.

        kms_key_id (Text, Optional): Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can
            be an alias name prefixed by "alias/", a fully specified ARN to an alias, a fully specified ARN to a key, or
            a globally unique identifier.

            CloudTrail also supports KMS multi-Region keys. For more information about multi-Region keys, see Using
            multi-Region keys in the Key Management Service Developer Guide .

            Examples:

            alias/MyAliasName
            arn:aws:kms:us-east-2:123456789012:alias/MyAliasName
            arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012
            12345678-1234-1234-1234-123456789012

        is_organization_trail (boolean, Optional): Specifies whether the trail is created for all accounts in an organization in
             Organizations, or only for the current Amazon Web Services account. The default is false, and cannot be true
             unless the call is made on behalf of an Amazon Web Services account that is the management account for an
             organization in Organizations.

        TagsList (list, Optional): A list of tags.
            (dict): A custom key-value pair associated with a resource such as a CloudTrail trail.
            Key (Text):
                The key in a key-value pair. The key must be no longer than 128 Unicode characters.
                The key must be unique for the resource to which it applies.

            Value (Text): The value in a key-value pair of a tag. The value must be no longer than 256
                Unicode characters.

        is_logging (boolean, Optional) : Start and Stop the logging of CloudTrail

        insight-selectors (List, Optional):
            Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing trail.
            You also use PutInsightSelectors to turn off Insights event logging, by passing an empty list of insight types.
            The valid Insights event types in this release are ApiErrorRateInsight and ApiCallRateInsight.

        event_selectors (List, Optional):
        advanced_event_selectors (List, Optional):
        Configures an event selector or advanced event selectors for your trail. Use event selectors or advanced event selectors to specify management and
        data event settings for your trail.
        By default, trails created without specific event selectors are configured to log all read and write management events, and no data events.
        When an event occurs in your account, CloudTrail evaluates the event selectors or advanced event selectors in all trails.
        For each trail, if the event matches any event selector, the trail processes and logs the event.
        If the event doesn't match any event selector, the trail doesn't log the event.

    Examples:

        .. code-block:: sls

        [trail_name]:
          aws.cloudtrail.trail.present:
          - resource_id: 'string
          - s3_bucket_name: 'string'
          - s3_key_prefix: 'string'
          - sns_topic_name: 'string',
          - include_global_service_events: boolean
          - is_multi_region_trail: boolean
          - enable_log_file_validation: boolean
          - cloud_watch_logs_loggroup_arn: 'string'
          - cloud_watch_logs_role_arn: 'string'
          - kms_key_id: 'string'
          - is_organization_trail: boolean
          - tags:
             - Key: 'string'
              Value: 'string'

        test-trail:
          aws.cloudtrail.trail.present:
          - name: test-trail
          - resource_id: test-trail
          - enable_logfile_validation: false
          - s3_bucket_name: test-bucket1
          - s3_key_prefix: test-bucket
          - sns_topic_name: arn:aws:sns:us-east-2:123456789012:MyTopic
          - include_global_service_events: true
          - is_multi_region_trail: true
          - cloud_watch_logs_loggroup_arn: arn:aws:logs:us-east-2:123456789012:log-group:aws-cloudtrail-logs-123456789012:*
          - cloud_watch_logs_role_arn: arn:aws:iam::123456789012:role/service-role/cloudtrailrole
          - kms_key_id: arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012
          - is_organization_trail: false
          - trail_arn: arn:aws:cloudtrail:us-east-2:123456789012:trail/test-trail
          - tags:
            - Key: trail
              Value: 'test-trail'
          - is_logging: true
          - event_selectors: null
          - advanced_event_selectors:
            - FieldSelectors:
              - Field: eventCategory
                Equals:
                 - Data
              - Field: resources.type
                Equals:
                 - AWS::S3::Object
            - Name: 'Management events selector'
              FieldSelectors:
              - Field: eventCategory
                Equals:
                - Management
          - insight_selectors:
            - InsightType: ApiCallRateInsight
            - InsightType: ApiErrorRateInsight
    """
    result = dict(comment=(), old_state=None, new_state=None, name=name, result=True)
    resource_updated = False
    before = None
    if resource_id:
        try:
            before = await hub.exec.boto3.client.cloudtrail.get_trail(
                ctx, Name=resource_id
            )
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = f"{e.__class__.__name__}: {e}"
            result["result"] = False
            return result
    if before:
        try:
            result[
                "old_state"
            ] = await hub.tool.aws.cloudtrail.conversion_utils.convert_raw_cloudtrail_to_present(
                ctx, raw_resource=before["ret"]["Trail"], idem_resource_name=name
            )
            plan_state = copy.deepcopy(result["old_state"])

            update_ret = await hub.exec.aws.cloudtrail.trail.update_trail(
                ctx,
                before=before["ret"]["Trail"],
                s3_bucket_name=s3_bucket_name,
                s3_key_prefix=s3_key_prefix,
                sns_topic_name=sns_topic_name,
                include_global_service_events=include_global_service_events,
                is_multi_region_trail=is_multi_region_trail,
                enable_logfile_validation=enable_logfile_validation,
                cloud_watch_logs_loggroup_arn=cloud_watch_logs_loggroup_arn,
                cloud_watch_logs_role_arn=cloud_watch_logs_role_arn,
                kms_key_id=kms_key_id,
                is_organization_trail=is_organization_trail,
            )
            result["comment"] = result["comment"] + update_ret["comment"]
            result["result"] = update_ret["result"]
            resource_updated = resource_updated or bool(update_ret["ret"])
            if update_ret["ret"] and ctx.get("test", False):
                plan_state = hub.tool.aws.cloudtrail.conversion_utils.update_plan_state(
                    plan_state=plan_state, update_ret=update_ret
                )

            if tags is not None:
                try:
                    ret_tag = await hub.exec.boto3.client.cloudtrail.list_tags(
                        ctx, ResourceIdList=[before["ret"]["Trail"]["TrailARN"]]
                    )
                    if ret_tag["result"]:
                        old_tags = (
                            ret_tag.get("ret").get("ResourceTagList")[0].get("TagsList")
                        )

                    if not (
                        hub.tool.aws.state_comparison_utils.are_lists_identical(
                            tags, old_tags
                        )
                    ):
                        # Update tags
                        update_ret = await hub.exec.aws.cloudtrail.trail.update_tags(
                            ctx,
                            resource_id=before["ret"]["Trail"]["TrailARN"],
                            old_tags=old_tags,
                            new_tags=tags,
                        )
                        result["result"] = result["result"] and update_ret["result"]
                        result["comment"] = result["comment"] + update_ret["comment"]
                        resource_updated = resource_updated or bool(update_ret["ret"])
                        if ctx.get("test", False) and update_ret["ret"] is not None:
                            plan_state["tags"] = update_ret["ret"].get("tags")
                except hub.tool.boto3.exception.ClientError as e:
                    result["comment"] = result["comment"] + (
                        f"{e.__class__.__name__}: {e}"
                    )
            if not resource_updated:
                result["comment"] = result["comment"] + (f"{name} already exists",)
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = result["comment"] + (f"{e.__class__.__name__}: {e}")
            result["result"] = False
    else:
        if ctx.get("test", False):
            result["new_state"] = hub.tool.aws.test_state_utils.generate_test_state(
                enforced_state={},
                desired_state={
                    "name": name,
                    "s3_bucket_name": s3_bucket_name,
                    "s3_key_prefix": s3_key_prefix,
                    "sns_topic_name": sns_topic_name,
                    "include_global_service_events": include_global_service_events,
                    "is_multi_region_trail": is_multi_region_trail,
                    "enable_logfile_validation": enable_logfile_validation,
                    "cloud_watch_logs_loggroup_arn": cloud_watch_logs_loggroup_arn,
                    "cloud_watch_logs_role_arn": cloud_watch_logs_role_arn,
                    "kms_key_id": kms_key_id,
                    "is_organization_trail": is_organization_trail,
                    "tags": tags,
                    "is_logging": is_logging,
                    "insight_selectors": insight_selectors,
                    "event_selectors": event_selectors,
                    "advanced_event_selectors": advanced_event_selectors,
                },
            )
            result["comment"] = f"Would create aws.cloudtrail.trail {name}"
            return result

        try:
            ret = await hub.exec.boto3.client.cloudtrail.create_trail(
                ctx,
                Name=name,
                S3BucketName=s3_bucket_name,
                S3KeyPrefix=s3_key_prefix,
                SnsTopicName=sns_topic_name,
                IncludeGlobalServiceEvents=include_global_service_events,
                IsMultiRegionTrail=is_multi_region_trail,
                EnableLogFileValidation=enable_logfile_validation,
                CloudWatchLogsLogGroupArn=cloud_watch_logs_loggroup_arn,
                CloudWatchLogsRoleArn=cloud_watch_logs_role_arn,
                KmsKeyId=kms_key_id,
                IsOrganizationTrail=is_organization_trail,
                TagsList=tags,
            )
            result["result"] = ret["result"]
            if not result["result"]:
                result["comment"] = ret["comment"]
                return result
            result["comment"] = result["comment"] + (f"Created '{name}'",)
            resource_id = ret["ret"]["Name"]
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = result["comment"] + (f"{e.__class__.__name__}: {e}")
            result["result"] = False
            return result

    ##Update Scenarios for Logging, event selector and insights
    try:
        if before:
            resource = before
        else:
            resource = await hub.exec.boto3.client.cloudtrail.get_trail(
                ctx, Name=resource_id
            )
        update_trail_attr = await hub.exec.aws.cloudtrail.trail.update_trail_attributes(
            ctx,
            before=resource["ret"]["Trail"],
            resource_id=resource["ret"]["Trail"]["TrailARN"],
            is_logging=is_logging,
            update_insight_selectors=insight_selectors,
            update_event_selectors=event_selectors,
            update_advanced_event_selectors=advanced_event_selectors,
        )
        result["comment"] = result["comment"] + update_trail_attr["comment"]
        result["result"] = result["result"] and update_trail_attr["result"]
        resource_updated = resource_updated or bool(update_trail_attr["ret"])
        if update_trail_attr["ret"] and ctx.get("test", False):
            plan_state = hub.tool.aws.cloudtrail.conversion_utils.update_plan_state(
                plan_state=plan_state, update_ret=update_trail_attr
            )

    except hub.tool.boto3.exception.ClientError as e:
        result["comment"] = result["comment"] + (f"{e.__class__.__name__}: {e}")
        result["result"] = False
        return result

    try:
        if ctx.get("test", False):
            result["new_state"] = plan_state
        elif (not before) or resource_updated:
            after = await hub.exec.boto3.client.cloudtrail.get_trail(
                ctx, Name=resource_id
            )

            result[
                "new_state"
            ] = await hub.tool.aws.cloudtrail.conversion_utils.convert_raw_cloudtrail_to_present(
                ctx, raw_resource=after["ret"]["Trail"], idem_resource_name=name
            )
        else:
            result["new_state"] = copy.deepcopy(result["old_state"])
    except Exception as e:
        result["comment"] = result["comment"] + (str(e),)
        result["result"] = False
    return result


async def absent(
    hub,
    ctx,
    name: str,
    resource_id: str,
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Deletes a trail. This operation must be called from the region in which the trail was created. DeleteTrail
    cannot be called on the shadow trails (replicated trails in other regions) of a trail that is enabled in all
    regions.

    Args:
        name(Text): An Idem name of the resource.
        resource_id(Text): Trail name to identify the resource

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            resource_is_absent:
              aws.cloudtrail.trail.absent:
                - name: value
                - resource_id: value
    """

    result = dict(comment=(), old_state=None, new_state=None, name=name, result=True)
    try:
        before = await hub.exec.boto3.client.cloudtrail.get_trail(ctx, Name=resource_id)

        if not before:
            result["comment"] = (f"'{name}' already absent",)
        elif ctx.get("test", False):
            result[
                "old_state"
            ] = await hub.tool.aws.cloudtrail.conversion_utils.convert_raw_cloudtrail_to_present(
                ctx, raw_resource=before["ret"]["Trail"], idem_resource_name=name
            )
            result["comment"] = (f"Would delete aws.cloudtrail.trail {name}",)
            return result
        else:
            result[
                "old_state"
            ] = await hub.tool.aws.cloudtrail.conversion_utils.convert_raw_cloudtrail_to_present(
                ctx, raw_resource=before["ret"]["Trail"], idem_resource_name=name
            )
            ret = await hub.exec.boto3.client.cloudtrail.delete_trail(
                ctx, Name=resource_id
            )
            result["result"] = ret["result"]
            if not result["result"]:
                result["comment"] = ret["comment"]
                result["result"] = False
                return result
            result["comment"] = (f"Deleted '{name}'",)

    except hub.tool.boto3.exception.ClientError as e:
        result["comment"] = (f"{e.__class__.__name__}: {e}",)
    return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    r"""
    **Autogenerated function**

    Describe the resource in a way that can be recreated/managed with the corresponding "present" function


    Lists trails that are in the current account including Logging Status, Event Selectors and Insight Selectors as well.


    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: bash

            $ idem describe aws.cloudtrail.trail
    """

    result = {}

    try:
        ret = await hub.exec.boto3.client.cloudtrail.list_trails(ctx)

        if not ret["result"]:
            hub.log.debug(f"Could not describe trail {ret['comment']}")
            return {}

        trail_list = [trail["TrailARN"] for trail in ret["ret"]["Trails"]]
        key_details = await hub.exec.boto3.client.cloudtrail.describe_trails(
            ctx, trailNameList=trail_list, includeShadowTrails=True
        )

        for trail in key_details["ret"]["trailList"]:
            trail_name = trail["Name"]

            resource_translated = await hub.tool.aws.cloudtrail.conversion_utils.convert_raw_cloudtrail_to_present(
                ctx, raw_resource=trail, idem_resource_name=trail_name
            )
            result[trail_name] = {
                "aws.cloudtrail.trail.present": [
                    {parameter_key: parameter_value}
                    for parameter_key, parameter_value in resource_translated.items()
                ]
            }
    except hub.tool.boto3.exception.ClientError as e:
        result["comment"] = (f"{e.__class__.__name__}: {e}",)

    return result
