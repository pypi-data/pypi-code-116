# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ScriptProtocolMapperArgs', 'ScriptProtocolMapper']

@pulumi.input_type
class ScriptProtocolMapperArgs:
    def __init__(__self__, *,
                 realm_id: pulumi.Input[str],
                 saml_attribute_name: pulumi.Input[str],
                 saml_attribute_name_format: pulumi.Input[str],
                 script: pulumi.Input[str],
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_scope_id: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 single_value_attribute: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a ScriptProtocolMapper resource.
        :param pulumi.Input[str] realm_id: The realm this protocol mapper exists within.
        :param pulumi.Input[str] saml_attribute_name: The name of the SAML attribute.
        :param pulumi.Input[str] saml_attribute_name_format: The SAML attribute Name Format. Can be one of `Unspecified`, `Basic`, or `URI Reference`.
        :param pulumi.Input[str] script: JavaScript code to compute the attribute value.
        :param pulumi.Input[str] client_id: The client this protocol mapper should be attached to. Conflicts with `client_scope_id`. One of `client_id` or `client_scope_id` must be specified.
        :param pulumi.Input[str] client_scope_id: The client scope this protocol mapper should be attached to. Conflicts with `client_id`. One of `client_id` or `client_scope_id` must be specified.
        :param pulumi.Input[str] friendly_name: An optional human-friendly name for this attribute.
        :param pulumi.Input[str] name: The display name of this protocol mapper in the GUI.
        :param pulumi.Input[bool] single_value_attribute: When `true`, all values will be stored under one attribute with multiple attribute values. Defaults to `true`.
        """
        pulumi.set(__self__, "realm_id", realm_id)
        pulumi.set(__self__, "saml_attribute_name", saml_attribute_name)
        pulumi.set(__self__, "saml_attribute_name_format", saml_attribute_name_format)
        pulumi.set(__self__, "script", script)
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_scope_id is not None:
            pulumi.set(__self__, "client_scope_id", client_scope_id)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if single_value_attribute is not None:
            pulumi.set(__self__, "single_value_attribute", single_value_attribute)

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
    @pulumi.getter
    def script(self) -> pulumi.Input[str]:
        """
        JavaScript code to compute the attribute value.
        """
        return pulumi.get(self, "script")

    @script.setter
    def script(self, value: pulumi.Input[str]):
        pulumi.set(self, "script", value)

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
    @pulumi.getter(name="singleValueAttribute")
    def single_value_attribute(self) -> Optional[pulumi.Input[bool]]:
        """
        When `true`, all values will be stored under one attribute with multiple attribute values. Defaults to `true`.
        """
        return pulumi.get(self, "single_value_attribute")

    @single_value_attribute.setter
    def single_value_attribute(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "single_value_attribute", value)


@pulumi.input_type
class _ScriptProtocolMapperState:
    def __init__(__self__, *,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_scope_id: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 saml_attribute_name: Optional[pulumi.Input[str]] = None,
                 saml_attribute_name_format: Optional[pulumi.Input[str]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 single_value_attribute: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering ScriptProtocolMapper resources.
        :param pulumi.Input[str] client_id: The client this protocol mapper should be attached to. Conflicts with `client_scope_id`. One of `client_id` or `client_scope_id` must be specified.
        :param pulumi.Input[str] client_scope_id: The client scope this protocol mapper should be attached to. Conflicts with `client_id`. One of `client_id` or `client_scope_id` must be specified.
        :param pulumi.Input[str] friendly_name: An optional human-friendly name for this attribute.
        :param pulumi.Input[str] name: The display name of this protocol mapper in the GUI.
        :param pulumi.Input[str] realm_id: The realm this protocol mapper exists within.
        :param pulumi.Input[str] saml_attribute_name: The name of the SAML attribute.
        :param pulumi.Input[str] saml_attribute_name_format: The SAML attribute Name Format. Can be one of `Unspecified`, `Basic`, or `URI Reference`.
        :param pulumi.Input[str] script: JavaScript code to compute the attribute value.
        :param pulumi.Input[bool] single_value_attribute: When `true`, all values will be stored under one attribute with multiple attribute values. Defaults to `true`.
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
        if script is not None:
            pulumi.set(__self__, "script", script)
        if single_value_attribute is not None:
            pulumi.set(__self__, "single_value_attribute", single_value_attribute)

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
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[str]]:
        """
        JavaScript code to compute the attribute value.
        """
        return pulumi.get(self, "script")

    @script.setter
    def script(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script", value)

    @property
    @pulumi.getter(name="singleValueAttribute")
    def single_value_attribute(self) -> Optional[pulumi.Input[bool]]:
        """
        When `true`, all values will be stored under one attribute with multiple attribute values. Defaults to `true`.
        """
        return pulumi.get(self, "single_value_attribute")

    @single_value_attribute.setter
    def single_value_attribute(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "single_value_attribute", value)


class ScriptProtocolMapper(pulumi.CustomResource):
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
                 script: Optional[pulumi.Input[str]] = None,
                 single_value_attribute: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Allows for creating and managing script protocol mappers for SAML clients within Keycloak.

        Script protocol mappers evaluate a JavaScript function to produce an attribute value based on context information.

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
        saml_script_mapper = keycloak.saml.ScriptProtocolMapper("samlScriptMapper",
            realm_id=realm.id,
            client_id=saml_client.id,
            script="exports = 'foo';",
            saml_attribute_name="displayName",
            saml_attribute_name_format="Unspecified")
        ```

        ## Import

        Protocol mappers can be imported using one of the following formats- Client`{{realm_id}}/client/{{client_keycloak_id}}/{{protocol_mapper_id}}` - Client Scope`{{realm_id}}/client-scope/{{client_scope_keycloak_id}}/{{protocol_mapper_id}}` Examplebash

        ```sh
         $ pulumi import keycloak:saml/scriptProtocolMapper:ScriptProtocolMapper saml_script_mapper my-realm/client/a7202154-8793-4656-b655-1dd18c181e14/71602afa-f7d1-4788-8c49-ef8fd00af0f4
        ```

        ```sh
         $ pulumi import keycloak:saml/scriptProtocolMapper:ScriptProtocolMapper saml_script_mapper my-realm/client-scope/b799ea7e-73ee-4a73-990a-1eafebe8e20a/71602afa-f7d1-4788-8c49-ef8fd00af0f4
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
        :param pulumi.Input[str] script: JavaScript code to compute the attribute value.
        :param pulumi.Input[bool] single_value_attribute: When `true`, all values will be stored under one attribute with multiple attribute values. Defaults to `true`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScriptProtocolMapperArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Allows for creating and managing script protocol mappers for SAML clients within Keycloak.

        Script protocol mappers evaluate a JavaScript function to produce an attribute value based on context information.

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
        saml_script_mapper = keycloak.saml.ScriptProtocolMapper("samlScriptMapper",
            realm_id=realm.id,
            client_id=saml_client.id,
            script="exports = 'foo';",
            saml_attribute_name="displayName",
            saml_attribute_name_format="Unspecified")
        ```

        ## Import

        Protocol mappers can be imported using one of the following formats- Client`{{realm_id}}/client/{{client_keycloak_id}}/{{protocol_mapper_id}}` - Client Scope`{{realm_id}}/client-scope/{{client_scope_keycloak_id}}/{{protocol_mapper_id}}` Examplebash

        ```sh
         $ pulumi import keycloak:saml/scriptProtocolMapper:ScriptProtocolMapper saml_script_mapper my-realm/client/a7202154-8793-4656-b655-1dd18c181e14/71602afa-f7d1-4788-8c49-ef8fd00af0f4
        ```

        ```sh
         $ pulumi import keycloak:saml/scriptProtocolMapper:ScriptProtocolMapper saml_script_mapper my-realm/client-scope/b799ea7e-73ee-4a73-990a-1eafebe8e20a/71602afa-f7d1-4788-8c49-ef8fd00af0f4
        ```

        :param str resource_name: The name of the resource.
        :param ScriptProtocolMapperArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScriptProtocolMapperArgs, pulumi.ResourceOptions, *args, **kwargs)
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
                 script: Optional[pulumi.Input[str]] = None,
                 single_value_attribute: Optional[pulumi.Input[bool]] = None,
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
            __props__ = ScriptProtocolMapperArgs.__new__(ScriptProtocolMapperArgs)

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
            if script is None and not opts.urn:
                raise TypeError("Missing required property 'script'")
            __props__.__dict__["script"] = script
            __props__.__dict__["single_value_attribute"] = single_value_attribute
        super(ScriptProtocolMapper, __self__).__init__(
            'keycloak:saml/scriptProtocolMapper:ScriptProtocolMapper',
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
            script: Optional[pulumi.Input[str]] = None,
            single_value_attribute: Optional[pulumi.Input[bool]] = None) -> 'ScriptProtocolMapper':
        """
        Get an existing ScriptProtocolMapper resource's state with the given name, id, and optional extra
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
        :param pulumi.Input[str] script: JavaScript code to compute the attribute value.
        :param pulumi.Input[bool] single_value_attribute: When `true`, all values will be stored under one attribute with multiple attribute values. Defaults to `true`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ScriptProtocolMapperState.__new__(_ScriptProtocolMapperState)

        __props__.__dict__["client_id"] = client_id
        __props__.__dict__["client_scope_id"] = client_scope_id
        __props__.__dict__["friendly_name"] = friendly_name
        __props__.__dict__["name"] = name
        __props__.__dict__["realm_id"] = realm_id
        __props__.__dict__["saml_attribute_name"] = saml_attribute_name
        __props__.__dict__["saml_attribute_name_format"] = saml_attribute_name_format
        __props__.__dict__["script"] = script
        __props__.__dict__["single_value_attribute"] = single_value_attribute
        return ScriptProtocolMapper(resource_name, opts=opts, __props__=__props__)

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
    @pulumi.getter
    def script(self) -> pulumi.Output[str]:
        """
        JavaScript code to compute the attribute value.
        """
        return pulumi.get(self, "script")

    @property
    @pulumi.getter(name="singleValueAttribute")
    def single_value_attribute(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, all values will be stored under one attribute with multiple attribute values. Defaults to `true`.
        """
        return pulumi.get(self, "single_value_attribute")

