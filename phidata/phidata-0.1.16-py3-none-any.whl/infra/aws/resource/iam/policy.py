from typing import Optional, Any, List, Dict

from botocore.exceptions import ClientError

from phidata.infra.aws.api_client import AwsApiClient
from phidata.infra.aws.resource.base import AwsResource
from phidata.utils.cli_console import print_info, print_error, print_warning
from phidata.utils.log import logger


class IamPolicy(AwsResource):
    """
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#policy
    """

    resource_type = "IamPolicy"
    service_name = "iam"

    # PolicyName
    # The friendly name of the policy.
    name: str
    # The JSON policy document that you want to use as the content for the new policy.
    # You must provide policies in JSON format in IAM.
    # However, for CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format.
    # CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.
    policy_document: str
    # The path for the policy. This parameter is optional. If it is not included, it defaults to a slash (/).
    path: Optional[str] = None
    # A friendly description of the policy.
    description: Optional[str] = None
    # A list of tags that you want to attach to the new policy. Each tag consists of a key name and an associated value.
    tags: Optional[List[Dict[str, str]]] = None

    arn: Optional[str] = None
    skip_delete = False

    def _create(self, aws_client: AwsApiClient) -> bool:
        """Creates the IamPolicy

        Args:
            aws_client: The AwsApiClient for the current cluster
        """

        logger.debug(
            "Creating {} {}".format(self.get_resource_type(), self.get_resource_name())
        )
        try:
            service_resource = self.get_service_resource(aws_client)
            # logger.debug(f"ServiceResource: {service_resource}")
            # logger.debug(f"ServiceResource type: {type(service_resource)}")

            # create a dict of args which are not null, otherwise aws type validation fails
            non_null_args = {}
            if self.path:
                non_null_args["Path"] = self.path
            if self.description:
                non_null_args["Description"] = self.description
            if self.tags:
                non_null_args["Tags"] = self.tags

            ## Create Policy
            policy = service_resource.create_policy(
                PolicyName=self.name,
                PolicyDocument=self.policy_document,
                **non_null_args,
            )
            # logger.debug(f"Policy: {policy}")

            ## Validate Policy creation
            create_date = policy.create_date
            self.arn = policy.arn
            logger.debug(f"create_date: {create_date}")
            logger.debug(f"arn: {self.arn}")
            if create_date is not None:
                print_info(f"Policy created: {self.name}")
                self.active_resource = policy
                return True
            print_error("Policy could not be created")
        except Exception as e:
            print_error(
                "Policy could not be created, this operation is known to be buggy."
            )
            print_error("Please deploy the workspace again.")
            print_error(e)
        return False

    def post_create(self, aws_client: AwsApiClient) -> bool:
        ## Wait for Policy to be created
        if self.wait_for_completion:
            try:
                print_info("Waiting for Policy to be created")
                if self.arn is not None:
                    waiter = self.get_service_client(aws_client).get_waiter(
                        "policy_exists"
                    )
                    waiter.wait(
                        PolicyArn=self.arn,
                        WaiterConfig={
                            "Delay": self.waiter_delay,
                            "MaxAttempts": self.waiter_max_attempts,
                        },
                    )
                else:
                    print_warning("Skipping waiter, No Policy ARN found")
            except Exception as e:
                print_error(
                    f"Waiter PolicyExists {self.name} failed, downstream actions might fail."
                )
                print_error(e)
                print_error("---+---")
        return True

    def _read(self, aws_client: AwsApiClient) -> Optional[Any]:
        """Returns the IamPolicy

        Args:
            aws_client: The AwsApiClient for the current cluster
        """
        logger.debug(
            "Reading {} {}".format(self.get_resource_type(), self.get_resource_name())
        )
        try:
            service_resource = self.get_service_resource(aws_client)
            # logger.debug(f"ServiceResource: {service_resource}")
            # logger.debug(f"ServiceResource type: {type(service_resource)}")
            policy = None
            for _policy in service_resource.policies.all():
                if _policy.policy_name == self.name:
                    policy = _policy

            if policy is None:
                logger.debug("No Policy found")
                return None

            policy.load()
            create_date = policy.create_date
            self.arn = policy.arn
            logger.debug(f"create_date: {create_date}")
            logger.debug(f"arn: {self.arn}")
            if create_date is not None:
                logger.debug(f"Policy found: {policy.policy_name}")
                self.active_resource = policy
        except ClientError as ce:
            logger.debug(f"ClientError: {ce}")
            pass
        except Exception as e:
            print_error(e)
        return self.active_resource

    def _delete(self, aws_client: AwsApiClient) -> bool:
        """Deletes the IamPolicy

        Args:
            aws_client: The AwsApiClient for the current cluster
        """

        logger.debug(
            "Deleting {} {}".format(self.get_resource_type(), self.get_resource_name())
        )
        try:
            policy = self._read(aws_client)
            # logger.debug(f"Policy: {policy}")
            # logger.debug(f"Policy type: {type(policy)}")
            self.active_resource = None

            # Before you can delete a managed policy,
            # you must first detach the policy from all users, groups, and roles
            # that it is attached to. In addition, you must delete all
            # the policy's versions.

            # detach all roles
            roles = policy.attached_roles.all()
            for role in roles:
                print_info(f"Detaching policy from role: {role}")
                policy.detach_role(RoleName=role.name)

            # detach all users
            users = policy.attached_users.all()
            for user in users:
                print_info(f"Detaching policy from user: {user}")
                policy.detach_user(UserName=user.name)

            # detach all groups
            groups = policy.attached_groups.all()
            for group in groups:
                print_info(f"Detaching policy from group: {group}")
                policy.detach_group(GroupName=group.name)

            # delete all versions
            default_version = policy.default_version
            versions = policy.versions.all()
            for version in versions:
                if version.version_id == default_version.version_id:
                    print_info(f"Skipping deleting default PolicyVersion: {version}")
                    continue
                print_info(f"Deleting PolicyVersion: {version}")
                version.delete()

            # delete policy
            policy.delete()
            print_info(f"Policy deleted: {policy.policy_name}")
            return True
        except Exception as e:
            print_error(
                f"Received error while deleting {self.get_resource_type()}, this operation is known to be buggy."
            )
            print_error("Please try again or delete resources manually.")
            print_error(e)
        return False
