# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserAttributeProtocolMapperArgs', 'UserAttributeProtocolMapper']

@pulumi.input_type
class UserAttributeProtocolMapperArgs:
    def __init__(__self__, *,
                 realm_id: pulumi.Input[str],
                 saml_attribute_name: pulumi.Input[str],
                 saml_attribute_name_format: pulumi.Input[str],
                 user_attribute: pulumi.Input[str],
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_scope_id: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UserAttributeProtocolMapper resource.
        :param pulumi.Input[str] realm_id: The realm this protocol mapper exists within.
        :param pulumi.Input[str] saml_attribute_name: The name of the SAML attribute.
        :param pulumi.Input[str] saml_attribute_name_format: The SAML attribute Name Format. Can be one of `Unspecified`, `Basic`, or `URI Reference`.
        :param pulumi.Input[str] user_attribute: The custom user attribute to map.
        :param pulumi.Input[str] client_id: The client this protocol mapper should be attached to. Conflicts with `client_scope_id`. One of `client_id` or `client_scope_id` must be specified.
        :param pulumi.Input[str] client_scope_id: The client scope this protocol mapper should be attached to. Conflicts with `client_id`. One of `client_id` or `client_scope_id` must be specified.
        :param pulumi.Input[str] friendly_name: An optional human-friendly name for this attribute.
        :param pulumi.Input[str] name: The display name of this protocol mapper in the GUI.
        """
        pulumi.set(__self__, "realm_id", realm_id)
        pulumi.set(__self__, "saml_attribute_name", saml_attribute_name)
        pulumi.set(__self__, "saml_attribute_name_format", saml_attribute_name_format)
        pulumi.set(__self__, "user_attribute", user_attribute)
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_scope_id is not None:
            pulumi.set(__self__, "client_scope_id", client_scope_id)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Input[str]:
        """
        The realm this protocol mapper exists within.
        """
        return pulumi.get(self, "realm_id")

    @realm_id.setter
    def realm_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "realm_id", value)

    @property
    @pulumi.getter(name="samlAttributeName")
    def saml_attribute_name(self) -> pulumi.Input[str]:
        """
        The name of the SAML attribute.
        """
        return pulumi.get(self, "saml_attribute_name")

    @saml_attribute_name.setter
    def saml_attribute_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "saml_attribute_name", value)

    @property
    @pulumi.getter(name="samlAttributeNameFormat")
    def saml_attribute_name_format(self) -> pulumi.Input[str]:
        """
        The SAML attribute Name Format. Can be one of `Unspecified`, `Basic`, or `URI Reference`.
        """
        return pulumi.get(self, "saml_attribute_name_format")

    @saml_attribute_name_format.setter
    def saml_attribute_name_format(self, value: pulumi.Input[str]):
        pulumi.set(self, "saml_attribute_name_format", value)

    @property
    @pulumi.getter(name="userAttribute")
    def user_attribute(self) -> pulumi.Input[str]:
        """
        The custom user attribute to map.
        """
        return pulumi.get(self, "user_attribute")

    @user_attribute.setter
    def user_attribute(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_attribute", value)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        The client this protocol mapper should be attached to. Conflicts with `client_scope_id`. One of `client_id` or `client_scope_id` must be specified.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientScopeId")
    def client_scope_id(self) -> Optional[pulumi.Input[str]]:
        """
        The client scope this protocol mapper should be attached to. Conflicts with `client_id`. One of `client_id` or `client_scope_id` must be specified.
        """
        return pulumi.get(self, "client_scope_id")

    @client_scope_id.setter
    def client_scope_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_scope_id", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        An optional human-friendly name for this attribute.
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of this protocol mapper in the GUI.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _UserAttributeProtocolMapperState:
    def __init__(__self__, *,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_scope_id: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 saml_attribute_name: Optional[pulumi.Input[str]] = None,
                 saml_attribute_name_format: Optional[pulumi.Input[str]] = None,
                 user_attribute: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UserAttributeProtocolMapper resources.
        :param pulumi.Input[str] client_id: The client this protocol mapper should be attached to. Conflicts with `client_scope_id`. One of `client_id` or `client_scope_id` must be specified.
        :param pulumi.Input[str] client_scope_id: The client scope this protocol mapper should be attached to. Conflicts with `client_id`. One of `client_id` or `client_scope_id` must be specified.
        :param pulumi.Input[str] friendly_name: An optional human-friendly name for this attribute.
        :param pulumi.Input[str] name: The display name of this protocol mapper in the GUI.
        :param pulumi.Input[str] realm_id: The realm this protocol mapper exists within.
        :param pulumi.Input[str] saml_attribute_name: The name of the SAML attribute.
        :param pulumi.Input[str] saml_attribute_name_format: The SAML attribute Name Format. Can be one of `Unspecified`, `Basic`, or `URI Reference`.
        :param pulumi.Input[str] user_attribute: The custom user attribute to map.
        """
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_scope_id is not None:
            pulumi.set(__self__, "client_scope_id", client_scope_id)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if realm_id is not None:
            pulumi.set(__self__, "realm_id", realm_id)
        if saml_attribute_name is not None:
            pulumi.set(__self__, "saml_attribute_name", saml_attribute_name)
        if saml_attribute_name_format is not None:
            pulumi.set(__self__, "saml_attribute_name_format", saml_attribute_name_format)
        if user_attribute is not None:
            pulumi.set(__self__, "user_attribute", user_attribute)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        The client this protocol mapper should be attached to. Conflicts with `client_scope_id`. One of `client_id` or `client_scope_id` must be specified.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientScopeId")
    def client_scope_id(self) -> Optional[pulumi.Input[str]]:
        """
        The client scope this protocol mapper should be attached to. Conflicts with `client_id`. One of `client_id` or `client_scope_id` must be specified.
        """
        return pulumi.get(self, "client_scope_id")

    @client_scope_id.setter
    def client_scope_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_scope_id", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        An optional human-friendly name for this attribute.
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of this protocol mapper in the GUI.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> Optional[pulumi.Input[str]]:
        """
        The realm this protocol mapper exists within.
        """
        return pulumi.get(self, "realm_id")

    @realm_id.setter
    def realm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "realm_id", value)

    @property
    @pulumi.getter(name="samlAttributeName")
    def saml_attribute_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the SAML attribute.
        """
        return pulumi.get(self, "saml_attribute_name")

    @saml_attribute_name.setter
    def saml_attribute_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "saml_attribute_name", value)

    @property
    @pulumi.getter(name="samlAttributeNameFormat")
    def saml_attribute_name_format(self) -> Optional[pulumi.Input[str]]:
        """
        The SAML attribute Name Format. Can be one of `Unspecified`, `Basic`, or `URI Reference`.
        """
        return pulumi.get(self, "saml_attribute_name_format")

    @saml_attribute_name_format.setter
    def saml_attribute_name_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "saml_attribute_name_format", value)

    @property
    @pulumi.getter(name="userAttribute")
    def user_attribute(self) -> Optional[pulumi.Input[str]]:
        """
        The custom user attribute to map.
        """
        return pulumi.get(self, "user_attribute")

    @user_attribute.setter
    def user_attribute(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_attribute", value)


class UserAttributeProtocolMapper(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_scope_id: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 saml_attribute_name: Optional[pulumi.Input[str]] = None,
                 saml_attribute_name_format: Optional[pulumi.Input[str]] = None,
                 user_attribute: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Allows for creating and managing user attribute protocol mappers for SAML clients within Keycloak.

        SAML user attribute protocol mappers allow you to map custom attributes defined for a user within Keycloak to an attribute
        in a SAML assertion.

        Protocol mappers can be defined for a single client, or they can be defined for a client scope which can be shared between
        multiple different clients.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        saml_client = keycloak.saml.Client("samlClient",
            realm_id=realm.id,
            client_id="saml-client")
        saml_user_attribute_mapper = keycloak.saml.UserAttributeProtocolMapper("samlUserAttributeMapper",
            realm_id=realm.id,
            client_id=saml_client.id,
            user_attribute="displayName",
            saml_attribute_name="displayName",
            saml_attribute_name_format="Unspecified")
        ```

        ## Import

        Protocol mappers can be imported using one of the following formats- Client`{{realm_id}}/client/{{client_keycloak_id}}/{{protocol_mapper_id}}` - Client Scope`{{realm_id}}/client-scope/{{client_scope_keycloak_id}}/{{protocol_mapper_id}}` Examplebash

        ```sh
         $ pulumi import keycloak:saml/userAttributeProtocolMapper:UserAttributeProtocolMapper saml_user_attribute_mapper my-realm/client/a7202154-8793-4656-b655-1dd18c181e14/71602afa-f7d1-4788-8c49-ef8fd00af0f4
        ```

        ```sh
         $ pulumi import keycloak:saml/userAttributeProtocolMapper:UserAttributeProtocolMapper saml_user_attribute_mapper my-realm/client-scope/b799ea7e-73ee-4a73-990a-1eafebe8e20a/71602afa-f7d1-4788-8c49-ef8fd00af0f4
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: The client this protocol mapper should be attached to. Conflicts with `client_scope_id`. One of `client_id` or `client_scope_id` must be specified.
        :param pulumi.Input[str] client_scope_id: The client scope this protocol mapper should be attached to. Conflicts with `client_id`. One of `client_id` or `client_scope_id` must be specified.
        :param pulumi.Input[str] friendly_name: An optional human-friendly name for this attribute.
        :param pulumi.Input[str] name: The display name of this protocol mapper in the GUI.
        :param pulumi.Input[str] realm_id: The realm this protocol mapper exists within.
        :param pulumi.Input[str] saml_attribute_name: The name of the SAML attribute.
        :param pulumi.Input[str] saml_attribute_name_format: The SAML attribute Name Format. Can be one of `Unspecified`, `Basic`, or `URI Reference`.
        :param pulumi.Input[str] user_attribute: The custom user attribute to map.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserAttributeProtocolMapperArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Allows for creating and managing user attribute protocol mappers for SAML clients within Keycloak.

        SAML user attribute protocol mappers allow you to map custom attributes defined for a user within Keycloak to an attribute
        in a SAML assertion.

        Protocol mappers can be defined for a single client, or they can be defined for a client scope which can be shared between
        multiple different clients.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        saml_client = keycloak.saml.Client("samlClient",
            realm_id=realm.id,
            client_id="saml-client")
        saml_user_attribute_mapper = keycloak.saml.UserAttributeProtocolMapper("samlUserAttributeMapper",
            realm_id=realm.id,
            client_id=saml_client.id,
            user_attribute="displayName",
            saml_attribute_name="displayName",
            saml_attribute_name_format="Unspecified")
        ```

        ## Import

        Protocol mappers can be imported using one of the following formats- Client`{{realm_id}}/client/{{client_keycloak_id}}/{{protocol_mapper_id}}` - Client Scope`{{realm_id}}/client-scope/{{client_scope_keycloak_id}}/{{protocol_mapper_id}}` Examplebash

        ```sh
         $ pulumi import keycloak:saml/userAttributeProtocolMapper:UserAttributeProtocolMapper saml_user_attribute_mapper my-realm/client/a7202154-8793-4656-b655-1dd18c181e14/71602afa-f7d1-4788-8c49-ef8fd00af0f4
        ```

        ```sh
         $ pulumi import keycloak:saml/userAttributeProtocolMapper:UserAttributeProtocolMapper saml_user_attribute_mapper my-realm/client-scope/b799ea7e-73ee-4a73-990a-1eafebe8e20a/71602afa-f7d1-4788-8c49-ef8fd00af0f4
        ```

        :param str resource_name: The name of the resource.
        :param UserAttributeProtocolMapperArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserAttributeProtocolMapperArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_scope_id: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 saml_attribute_name: Optional[pulumi.Input[str]] = None,
                 saml_attribute_name_format: Optional[pulumi.Input[str]] = None,
                 user_attribute: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserAttributeProtocolMapperArgs.__new__(UserAttributeProtocolMapperArgs)

            __props__.__dict__["client_id"] = client_id
            __props__.__dict__["client_scope_id"] = client_scope_id
            __props__.__dict__["friendly_name"] = friendly_name
            __props__.__dict__["name"] = name
            if realm_id is None and not opts.urn:
                raise TypeError("Missing required property 'realm_id'")
            __props__.__dict__["realm_id"] = realm_id
            if saml_attribute_name is None and not opts.urn:
                raise TypeError("Missing required property 'saml_attribute_name'")
            __props__.__dict__["saml_attribute_name"] = saml_attribute_name
            if saml_attribute_name_format is None and not opts.urn:
                raise TypeError("Missing required property 'saml_attribute_name_format'")
            __props__.__dict__["saml_attribute_name_format"] = saml_attribute_name_format
            if user_attribute is None and not opts.urn:
                raise TypeError("Missing required property 'user_attribute'")
            __props__.__dict__["user_attribute"] = user_attribute
        super(UserAttributeProtocolMapper, __self__).__init__(
            'keycloak:saml/userAttributeProtocolMapper:UserAttributeProtocolMapper',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_id: Optional[pulumi.Input[str]] = None,
            client_scope_id: Optional[pulumi.Input[str]] = None,
            friendly_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            realm_id: Optional[pulumi.Input[str]] = None,
            saml_attribute_name: Optional[pulumi.Input[str]] = None,
            saml_attribute_name_format: Optional[pulumi.Input[str]] = None,
            user_attribute: Optional[pulumi.Input[str]] = None) -> 'UserAttributeProtocolMapper':
        """
        Get an existing UserAttributeProtocolMapper resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: The client this protocol mapper should be attached to. Conflicts with `client_scope_id`. One of `client_id` or `client_scope_id` must be specified.
        :param pulumi.Input[str] client_scope_id: The client scope this protocol mapper should be attached to. Conflicts with `client_id`. One of `client_id` or `client_scope_id` must be specified.
        :param pulumi.Input[str] friendly_name: An optional human-friendly name for this attribute.
        :param pulumi.Input[str] name: The display name of this protocol mapper in the GUI.
        :param pulumi.Input[str] realm_id: The realm this protocol mapper exists within.
        :param pulumi.Input[str] saml_attribute_name: The name of the SAML attribute.
        :param pulumi.Input[str] saml_attribute_name_format: The SAML attribute Name Format. Can be one of `Unspecified`, `Basic`, or `URI Reference`.
        :param pulumi.Input[str] user_attribute: The custom user attribute to map.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserAttributeProtocolMapperState.__new__(_UserAttributeProtocolMapperState)

        __props__.__dict__["client_id"] = client_id
        __props__.__dict__["client_scope_id"] = client_scope_id
        __props__.__dict__["friendly_name"] = friendly_name
        __props__.__dict__["name"] = name
        __props__.__dict__["realm_id"] = realm_id
        __props__.__dict__["saml_attribute_name"] = saml_attribute_name
        __props__.__dict__["saml_attribute_name_format"] = saml_attribute_name_format
        __props__.__dict__["user_attribute"] = user_attribute
        return UserAttributeProtocolMapper(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[Optional[str]]:
        """
        The client this protocol mapper should be attached to. Conflicts with `client_scope_id`. One of `client_id` or `client_scope_id` must be specified.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientScopeId")
    def client_scope_id(self) -> pulumi.Output[Optional[str]]:
        """
        The client scope this protocol mapper should be attached to. Conflicts with `client_id`. One of `client_id` or `client_scope_id` must be specified.
        """
        return pulumi.get(self, "client_scope_id")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[str]]:
        """
        An optional human-friendly name for this attribute.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The display name of this protocol mapper in the GUI.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Output[str]:
        """
        The realm this protocol mapper exists within.
        """
        return pulumi.get(self, "realm_id")

    @property
    @pulumi.getter(name="samlAttributeName")
    def saml_attribute_name(self) -> pulumi.Output[str]:
        """
        The name of the SAML attribute.
        """
        return pulumi.get(self, "saml_attribute_name")

    @property
    @pulumi.getter(name="samlAttributeNameFormat")
    def saml_attribute_name_format(self) -> pulumi.Output[str]:
        """
        The SAML attribute Name Format. Can be one of `Unspecified`, `Basic`, or `URI Reference`.
        """
        return pulumi.get(self, "saml_attribute_name_format")

    @property
    @pulumi.getter(name="userAttribute")
    def user_attribute(self) -> pulumi.Output[str]:
        """
        The custom user attribute to map.
        """
        return pulumi.get(self, "user_attribute")

