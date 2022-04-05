from typing import Optional, Any, List, Dict

from botocore.exceptions import ClientError

from phidata.infra.aws.api_client import AwsApiClient
from phidata.infra.aws.resource.base import AwsResource
from phidata.infra.aws.resource.iam.policy import IamPolicy
from phidata.utils.cli_console import print_info, print_error
from phidata.utils.log import logger


class IamRole(AwsResource):
    """
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#service-resource
    """

    resource_type = "IamRole"
    service_name = "iam"

    # RoleName
    # The name of the role to create.
    name: str
    # The trust relationship policy document that grants an entity permission to assume the role.
    assume_role_policy_document: str
    # The path to the role. This parameter is optional. If it is not included, it defaults to a slash (/).
    path: Optional[str] = None
    # A description of the role.
    description: Optional[str] = None
    # The maximum session duration (in seconds) that you want to set for the specified role.
    # If you do not specify a value for this setting, the default maximum of one hour is applied.
    # This setting can have a value from 1 hour to 12 hours.
    max_session_duration: Optional[int] = None
    # The ARN of the policy that is used to set the permissions boundary for the role.
    permissions_boundary: Optional[str] = None
    # A list of tags that you want to attach to the new role. Each tag consists of a key name and an associated value.
    tags: Optional[List[Dict[str, str]]] = None

    # List of IAM policies to
    # attach to the role after it is created
    policies: Optional[List[IamPolicy]] = None
    # List of IAM policy ARNs (Amazon Resource Name) to
    # attach to the role after it is created
    policy_arns: Optional[List[str]] = None

    # The Amazon Resource Name (ARN) specifying the role.
    # To get the arn, use get_arn() function
    arn: Optional[str] = None
    skip_delete = False

    def _create(self, aws_client: AwsApiClient) -> bool:
        """Creates the IamRole

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
            if self.max_session_duration:
                non_null_args["MaxSessionDuration"] = self.max_session_duration
            if self.permissions_boundary:
                non_null_args["PermissionsBoundary"] = self.permissions_boundary
            if self.tags:
                non_null_args["Tags"] = self.tags

            ## Create Role
            role = service_resource.create_role(
                RoleName=self.name,
                AssumeRolePolicyDocument=self.assume_role_policy_document,
                **non_null_args,
            )
            # logger.debug(f"Role: {role}")

            ## Validate Role creation
            create_date = role.create_date
            self.arn = role.arn
            logger.debug(f"create_date: {create_date}")
            logger.debug(f"arn: {self.arn}")
            if create_date is not None:
                print_info(f"Role created: {self.name}")
                self.active_resource = role
                return True
            print_error("Role could not be created")
        except Exception as e:
            print_error(
                "Role could not be created, this operation is known to be buggy."
            )
            print_error("Please deploy the workspace again.")
            print_error(e)
        return False

    def post_create(self, aws_client: AwsApiClient) -> bool:
        ## Wait for Role to be created
        if self.wait_for_completion:
            try:
                print_info("Waiting for Role to be created")
                waiter = self.get_service_client(aws_client).get_waiter("role_exists")
                waiter.wait(
                    RoleName=self.name,
                    WaiterConfig={
                        "Delay": self.waiter_delay,
                        "MaxAttempts": self.waiter_max_attempts,
                    },
                )
            except Exception as e:
                print_error(
                    f"Waiter RoleExists {self.name} failed, downstream actions might fail."
                )
                print_error(e)
                print_error("---+---")

        # Attach policy arns to role
        if self.active_resource is not None and self.policy_arns is not None:
            self.attach_policy_arns(aws_client)
        # Attach policies to role
        if self.active_resource is not None and self.policies is not None:
            self.attach_policies(aws_client)
        return True

    def _read(self, aws_client: AwsApiClient) -> Optional[Any]:
        """Returns the IamRole

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
            role = service_resource.Role(name=self.name)
            role.load()
            create_date = role.create_date
            self.arn = role.arn
            logger.debug(f"create_date: {create_date}")
            logger.debug(f"arn: {self.arn}")
            if create_date is not None:
                logger.debug(f"Role found: {role.role_name}")
                self.active_resource = role
        except ClientError as ce:
            logger.debug(f"ClientError: {ce}")
            pass
        except Exception as e:
            print_error(e)
        return self.active_resource

    def _delete(self, aws_client: AwsApiClient) -> bool:
        """Deletes the IamRole

        Args:
            aws_client: The AwsApiClient for the current cluster
        """

        logger.debug(
            "Deleting {} {}".format(self.get_resource_type(), self.get_resource_name())
        )
        try:
            role = self._read(aws_client)
            # logger.debug(f"Role: {role}")
            # logger.debug(f"Role type: {type(role)}")
            self.active_resource = None

            # detach all policies
            policies = role.attached_policies.all()
            for policy in policies:
                print_info(f"Detaching policy: {policy}")
                role.detach_policy(PolicyArn=policy.arn)

            # detach all instance profiles
            profiles = role.instance_profiles.all()
            for profile in profiles:
                print_info(f"Removing role from profile: {profile}")
                profile.remove_role(RoleName=role.name)

            # delete role
            role.delete()
            print_info(f"Role deleted: {role.role_name}")
            return True
        except Exception as e:
            print_error(
                f"Received error while deleting {self.get_resource_type()}, this operation is known to be buggy."
            )
            print_error("Please try again or delete resources manually.")
            print_error(e)
        return False

    def attach_policy_arns(self, aws_client: AwsApiClient) -> bool:
        """
        Attaches the specified managed policy to the specified IAM role.
        When you attach a managed policy to a role, the managed policy becomes part of the
        role's permission (access) policy.

        Returns:
            True if operation was successful
        """
        role = self._read(aws_client)
        try:
            # logger.debug("Attaching managed policies to role")
            for arn in self.policy_arns:
                if isinstance(arn, str):
                    role.attach_policy(PolicyArn=arn)
                    print_info(f"Attaching policy to {role.role_name}: {arn}")
            return True
        except Exception as e:
            print_error(e)
        return False

    def attach_policies(self, aws_client: AwsApiClient) -> bool:
        """
        Returns:
            True if operation was successful
        """
        role = self._read(aws_client)
        try:
            logger.debug("Attaching managed policies to role")
            for policy in self.policies:
                if policy.arn is None:
                    policy.create(aws_client)
                if policy.arn is not None:
                    role.attach_policy(PolicyArn=policy.arn)
                    print_info(f"Attaching policy to {role.role_name}: {policy.arn}")
            return True
        except Exception as e:
            print_error(e)
        return False

    def get_arn(self, aws_client: AwsApiClient) -> Optional[str]:
        role = self._read(aws_client)
        self.arn = role.arn
        return self.arn
