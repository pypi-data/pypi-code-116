"""
Autogenerated using `pop-create-idem <https://gitlab.com/saltstack/pop/pop-create-idem>`__

hub.exec.boto3.client.organizations.deregister_delegated_administrator
hub.exec.boto3.client.organizations.list_delegated_administrators
hub.exec.boto3.client.organizations.register_delegated_administrator
"""
import copy
from typing import Any
from typing import Dict
from typing import List

__contracts__ = ["resource"]
SERVICE = "organizations"


TREQ = {
    "absent": {
        "require": [
            "aws.organizations.policy_attachment.absent",
            "aws.organizations.policy.absent",
        ],
    },
    "present": {
        "require": [
            "aws.organizations.organization_unit.present",
        ],
    },
}


async def present(
    hub,
    ctx,
    name: str,
    email: str,
    role_name: str,
    iam_user_access_to_billing: str = "ALLOW",
    resource_id: str = None,
    parent_id: str = None,
    tags: List = None,
) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Creates an AWS account that is automatically a member of the organization whose credentials made the request.
    This is an asynchronous request that AWS performs in the background. Because CreateAccount operates asynchronously,
    it can return a successful completion message even though account initialization might still be in progress.
     You might need to wait a few minutes before you can successfully access the account

    Args:
        name(Text): The friendly name of the member account.
        email(Text): The email address of the owner to assign to the new member account. This email
                              address must not already be associated with another AWS account
        role_name(Text,Optional): The name of an IAM role that AWS Organizations automatically preconfigures in the
                                new member account. This role trusts the management account, allowing users in the
                                management account to assume the role, as permitted by the management account
                                administrator. The role has administrator permissions in the new member account.
                                If you don't specify this parameter, the role name defaults to OrganizationAccountAccessRole.
        iam_user_access_to_billing(Text,Optional,Default:'ALLOW'): If set to ALLOW , the new account enables IAM users to access account
                                                              billing information if they have the required permissions. If set to DENY ,
                                                              only the root user of the new account can access account billing information.
        resource_id(Text,Optional): AWS account ID to identify the resource
        parent_id(Text,Optional): Parent Organizational Unit ID or Root ID for the account. Defaults to the Organization default Root ID
        tags(List,Optional) : A list of tags that you want to attach to the newly created account


    Request Syntax:
        [account-id]:
          aws.organizations.account.present:
          - name: 'string'
          - resource_id: 'string'
          - email: 'string'
          - role_name: 'string'
          - iam_user_access_to_billing: 'string'
          - parent_id: 'string'
          - tags:
            - Key: 'string'
              Value: 'string'

    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            764144542382:
                aws.organizations.account.present:
                    - name: name_of_new_account
                    - resource_id: new-account_id
                    - email: xyz@email.com
                    - role_name: role_name1
                    - iam_user_access_to_billing: ALLOW
                    - parent_id : ou108811
                    - tags:
                        - Key: test-key
                          Value: test-value
                        - Key: test-key-1
                          Value: test-key-1
    """

    result = dict(comment=(), name=name, result=True, old_state=None, new_state=None)
    before = None
    update_tag = False
    update_parent = False

    if resource_id:
        before = await hub.exec.boto3.client.organizations.describe_account(
            ctx, AccountId=resource_id
        )

    if before:
        # Account exists , update
        try:
            old_tags = await hub.exec.boto3.client.organizations.list_tags_for_resource(
                ctx, ResourceId=resource_id
            )
            result["result"] = result["result"] and old_tags["result"]
            if not result["result"]:
                result["comment"] = result["comment"] + old_tags["comment"]
                return result
            # we need to list parents to check if move is required in case the new_parent_id is not equal to current_
            # parent_id
            parents = await hub.exec.boto3.client.organizations.list_parents(
                ctx, ChildId=resource_id
            )
            result["result"] = result["result"] and parents["result"]
            if not result["result"]:
                result["comment"] = result["comment"] + parents["comment"]
                return result
            if parents:
                current_parent_id = parents["ret"]["Parents"][0]["Id"]
                if parent_id is not None and current_parent_id != parent_id:
                    if not ctx.get("test", False):
                        move_account_result = await move_account(
                            hub, ctx, resource_id, result, parent_id
                        )
                        if move_account_result and not move_account_result["result"]:
                            result["comment"] = result["comment"] + (
                                f"Could not update parent for aws.organizations.account {name}",
                            )
                            result["result"] = False
                            return result
                    update_parent = True
            result[
                "old_state"
            ] = hub.tool.aws.organization.conversion_utils.convert_raw_account_to_present(
                current_parent_id if parents else None,
                before["ret"]["Account"],
                old_tags["ret"].get("Tags", []) if old_tags else None,
            )
            plan_state = copy.deepcopy(result["old_state"])
            if update_parent:
                plan_state["parent_id"] = parent_id
                result["comment"] = result["comment"] + (
                    f"Would update parent for aws.organizations.account {name}",
                )

            if tags is not None and old_tags["result"]:
                update_tags_ret = (
                    await hub.exec.aws.organizations.organization.update_tags(
                        ctx, resource_id, old_tags["ret"].get("Tags", []), tags
                    )
                )
                if not update_tags_ret["result"]:
                    result["comment"] = result["comment"] + update_tags_ret["comment"]
                    result["result"] = update_tags_ret["result"]
                    return result

                if update_tags_ret["ret"] is not None:
                    result["comment"] = result["comment"] + (
                        f"Updated tags on aws.organizations.account '{name}'.",
                    )
                    update_tag = True
                if ctx.get("test", False):
                    if update_tags_ret["ret"]:
                        plan_state["tags"] = update_tags_ret["ret"]
                    else:
                        plan_state["tags"] = result["old_state"]["tags"]

        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = result["comment"] + (f"{e.__class__.__name__}: {e}",)
            result["result"] = False

    else:
        # Account not present , create
        if ctx.get("test", False):
            result["new_state"] = hub.tool.aws.test_state_utils.generate_test_state(
                enforced_state={},
                desired_state={
                    "email": email,
                    "name": name,
                    "parent_id": parent_id,
                    "role_name": role_name,
                    "iam_user_access_to_billing": iam_user_access_to_billing,
                    "tags": tags,
                },
            )
            result["comment"] = (f"Would create aws.organizations.account {name}",)
            return result

        try:
            create_account_ret = (
                await hub.exec.boto3.client.organizations.create_account(
                    ctx,
                    Email=email,
                    AccountName=name,
                    RoleName=role_name,
                    IamUserAccessToBilling=iam_user_access_to_billing,
                    Tags=tags,
                )
            )

            result["result"] = create_account_ret["result"]
            if not result["result"]:
                result["comment"] = result["comment"] + create_account_ret["comment"]
                return result

            account_status_id = create_account_ret["ret"]["CreateAccountStatus"]["Id"]

            # Call a custom waiter to wait on account's creation.

            acceptors = [
                {
                    "matcher": "path",
                    "expected": "SUCCEEDED",
                    "state": "success",
                    "argument": "CreateAccountStatus.State",
                },
                {
                    "matcher": "path",
                    "expected": "IN_PROGRESS",
                    "state": "retry",
                    "argument": "CreateAccountStatus.State",
                },
                {
                    "matcher": "path",
                    "expected": "FAILED",
                    # Failure is also mapped with success to catch the error message
                    "state": "success",
                    "argument": "CreateAccountStatus.State",
                },
            ]
            account_waiter = hub.tool.boto3.custom_waiter.waiter_wrapper(
                name="AccountCreated",
                operation="DescribeCreateAccountStatus",
                argument=["CreateAccountStatus.State"],
                acceptors=acceptors,
                client=hub.tool.boto3.client.get_client(ctx, SERVICE),
                matcher="path",
                delay=10,
                max_tries=10,
            )
            await hub.tool.boto3.client.wait(
                ctx,
                SERVICE,
                "AccountCreated",
                account_waiter,
                CreateAccountRequestId=account_status_id,
            )

            account_status = await hub.exec.boto3.client.organizations.describe_create_account_status(
                ctx, CreateAccountRequestId=account_status_id
            )
            if account_status["result"]:
                create_account_status = account_status["ret"]["CreateAccountStatus"]
                account_state = create_account_status["State"]
                if account_state == "FAILED":
                    result["result"] = False
                    result["comment"] = result["comment"] + (
                        create_account_status["FailureReason"],
                    )
                    return result
                elif account_state == "SUCCEEDED":
                    resource_id = create_account_status["AccountId"]
                    result["comment"] = (f"Created aws.organizations.account {name}.",)
                    if resource_id is not None and parent_id is not None:
                        parents = (
                            await hub.exec.boto3.client.organizations.list_parents(
                                ctx, ChildId=resource_id
                            )
                        )
                        result["result"] = result["result"] and parents["result"]
                        if not result["result"]:
                            result["comment"] = result["comment"] + parents["comment"]
                            return result
                        if parents:
                            current_parent_id = parents["ret"]["Parents"][0]["Id"]

                            if current_parent_id != parent_id:
                                move_account_result = await move_account(
                                    hub, ctx, resource_id, result, parent_id
                                )
                                if (
                                    move_account_result
                                    and not move_account_result["result"]
                                ):
                                    result["comment"] = result["comment"] + (
                                        f"Could not update parent for aws.organizations.account {name}",
                                    )
                                    result["result"] = False
                                    return result
            else:
                result["result"] = False
                result["comment"] = result["comment"] + account_status["comment"]
                return result

        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = result["comment"] + (f"{e.__class__.__name__}: {e}",)
            result["result"] = False

    if ctx.get("test", False):
        result["new_state"] = plan_state
    elif not before or update_parent or update_tag and resource_id:
        try:
            after = await hub.exec.boto3.client.organizations.describe_account(
                ctx, AccountId=resource_id
            )
            if after and after.get("ret"):

                parents = await hub.exec.boto3.client.organizations.list_parents(
                    ctx, ChildId=resource_id
                )
                result["result"] = result["result"] and parents["result"]
                if not result["result"]:
                    result["comment"] = result["comment"] + parents["comment"]
                    return result
                if parents:
                    current_parent_id = parents["ret"]["Parents"][0]["Id"]

                new_tags = (
                    await hub.exec.boto3.client.organizations.list_tags_for_resource(
                        ctx, ResourceId=resource_id
                    )
                )
                result["result"] = result["result"] and new_tags["result"]
                if not result["result"]:
                    result["comment"] = result["comment"] + new_tags["comment"]
                    return result
                result[
                    "new_state"
                ] = hub.tool.aws.organization.conversion_utils.convert_raw_account_to_present(
                    current_parent_id if parents else None,
                    after["ret"]["Account"],
                    new_tags["ret"].get("Tags", []) if new_tags else None,
                )
            else:
                result["result"] = result["result"] and after["result"]
                if not result["result"]:
                    result["comment"] = result["comment"] + after["comment"]
                    return result

        except Exception as e:
            result["comment"] = result["comment"] + (str(e),)
            result["result"] = False

    else:
        result["new_state"] = copy.deepcopy(result["old_state"])

    return result


async def absent(hub, ctx, name: str, resource_id: str) -> Dict[str, Any]:
    r"""
    **Autogenerated function**

    Removes the specified account from the organization.The removed account becomes a standalone
    account that isn't a member of any organization. It's no longer subject to any policies and
    is responsible for its own bill payments. The organization's management account is no longer
    charged for any expenses accrued by the member account after it's removed from the organization.
    This operation can be called only from the organization's management account. Member accounts
    can remove themselves with LeaveOrganization instead.

    Args:
        name(Text): Name of the member account
        resource_id(Text): AWS account ID to identify the resource


    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: sls

            [account_id]:
              aws.organizations.organization.absent:
                - name: value
    """

    result = dict(comment=(), old_state=None, new_state=None, name=name, result=True)

    before = await hub.exec.boto3.client.organizations.describe_account(
        ctx, AccountId=resource_id
    )

    if not before:
        result["comment"] = (f"aws.organizations.account {name} already absent",)
    elif ctx.get("test", False):
        result["comment"] = (f"Would delete aws.organizations.account {name}.",)
    else:

        try:
            ret = await hub.exec.boto3.client.organizations.remove_account_from_organization(
                ctx, AccountId=resource_id
            )

            result["result"] = ret["result"]

            if not result["result"]:
                result["comment"] = result["comment"] + ret["comment"]
                return result
            result["comment"] = result["comment"] + (
                f"aws.organizations.account {name} deleted.",
            )
        except hub.tool.boto3.exception.ClientError as e:
            result["comment"] = result["comment"] + (f"{e.__class__.__name__}: {e}",)
            result["result"] = False

    if before:
        result[
            "old_state"
        ] = hub.tool.aws.organization.conversion_utils.convert_raw_account_to_present(
            None, before["ret"]["Account"], None
        )

    return result


async def describe(hub, ctx) -> Dict[str, Dict[str, Any]]:
    r"""
    **Autogenerated function**

    Lists all the accounts in the organization. To request only the accounts in a specified root or organizational
    unit (OU), use the ListAccountsForParent operation instead.


    Returns:
        Dict[str, Any]

    Examples:

        .. code-block:: bash

            $ idem describe aws.organizations.account
    """

    result = {}

    describe_ret = await hub.exec.boto3.client.organizations.list_accounts(ctx)
    if not describe_ret:
        hub.log.debug(f"Could not describe account {describe_ret['comment']}")
        return {}

    accounts = describe_ret["ret"]["Accounts"]

    for account in accounts:
        parent = await hub.exec.boto3.client.organizations.list_parents(
            ctx, ChildId=account["Id"]
        )
        if parent and not parent["result"]:
            hub.log.debug(
                f"Unable to list parent for account: {account['Id']} Error:  {describe_ret['comment']}"
            )
            continue

        tags = await hub.exec.boto3.client.organizations.list_tags_for_resource(
            ctx, ResourceId=account["Id"]
        )
        if tags and not tags["result"]:
            hub.log.debug(
                f"Unable to list tags for account: {account['Id']} Error:  {tags['comment']}"
            )
            continue
        translated_resource = (
            hub.tool.aws.organization.conversion_utils.convert_raw_account_to_present(
                parent["ret"]["Parents"][0]["Id"]
                if parent and parent["ret"].get("Parents")
                else None,
                account,
                tags["ret"].get("Tags") if tags and tags["ret"].get("Tags") else None,
            )
        )

        result[account["Id"]] = {
            "aws.organizations.account.present": [
                {parameter_key: parameter_value}
                for parameter_key, parameter_value in translated_resource.items()
            ]
        }
    return result


async def move_account(
    hub, ctx, account_id, result: Dict[str, Any], destination_parent_id
) -> Dict[str, Any]:
    if destination_parent_id is not None:

        parents = await hub.exec.boto3.client.organizations.list_parents(
            ctx, ChildId=account_id
        )
        result["result"] = result["result"] and parents["result"]
        if not result["result"]:
            result["comment"] = result["comment"] + parents["comment"]
            return result

        if parents:
            parent_id = parents["ret"]["Parents"][0]["Id"]

            if parent_id == destination_parent_id:
                result["comment"] = result["comment"] + (
                    f"aws.organizations.account {account_id} already at {destination_parent_id}",
                )
                return result
            else:

                account_move_ret = (
                    await hub.exec.boto3.client.organizations.move_account(
                        ctx,
                        AccountId=account_id,
                        SourceParentId=parent_id,
                        DestinationParentId=destination_parent_id,
                    )
                )
                if not account_move_ret:
                    result["comment"] = result["comment"] + (
                        f"Could not move aws.organizations.account {account_id} to {destination_parent_id} Error: {account_move_ret['comment']}",
                    )

                    result["result"] = False

                    return result
                result["comment"] = result["comment"] + (
                    f"Successfully moved aws.organizations.account {account_id} under {destination_parent_id}",
                )
                return result
