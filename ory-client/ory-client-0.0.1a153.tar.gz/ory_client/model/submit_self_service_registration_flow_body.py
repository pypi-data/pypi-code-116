"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.153
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ory_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from ory_client.exceptions import ApiAttributeError


def lazy_import():
    from ory_client.model.submit_self_service_registration_flow_with_oidc_method_body import SubmitSelfServiceRegistrationFlowWithOidcMethodBody
    from ory_client.model.submit_self_service_registration_flow_with_password_method_body import SubmitSelfServiceRegistrationFlowWithPasswordMethodBody
    from ory_client.model.submit_self_service_registration_flow_with_web_authn_method_body import SubmitSelfServiceRegistrationFlowWithWebAuthnMethodBody
    globals()['SubmitSelfServiceRegistrationFlowWithOidcMethodBody'] = SubmitSelfServiceRegistrationFlowWithOidcMethodBody
    globals()['SubmitSelfServiceRegistrationFlowWithPasswordMethodBody'] = SubmitSelfServiceRegistrationFlowWithPasswordMethodBody
    globals()['SubmitSelfServiceRegistrationFlowWithWebAuthnMethodBody'] = SubmitSelfServiceRegistrationFlowWithWebAuthnMethodBody


class SubmitSelfServiceRegistrationFlowBody(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'method': (str,),  # noqa: E501
            'csrf_token': (str,),  # noqa: E501
            'webauthn_register': (str,),  # noqa: E501
            'webauthn_register_displayname': (str,),  # noqa: E501
            'password': (str,),  # noqa: E501
            'traits': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'provider': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        lazy_import()
        val = {
            'oidc': SubmitSelfServiceRegistrationFlowWithOidcMethodBody,
            'password': SubmitSelfServiceRegistrationFlowWithPasswordMethodBody,
            'submitSelfServiceRegistrationFlowWithOidcMethodBody': SubmitSelfServiceRegistrationFlowWithOidcMethodBody,
            'submitSelfServiceRegistrationFlowWithPasswordMethodBody': SubmitSelfServiceRegistrationFlowWithPasswordMethodBody,
            'submitSelfServiceRegistrationFlowWithWebAuthnMethodBody': SubmitSelfServiceRegistrationFlowWithWebAuthnMethodBody,
            'webauthn': SubmitSelfServiceRegistrationFlowWithWebAuthnMethodBody,
        }
        if not val:
            return None
        return {'method': val}

    attribute_map = {
        'method': 'method',  # noqa: E501
        'csrf_token': 'csrf_token',  # noqa: E501
        'webauthn_register': 'webauthn_register',  # noqa: E501
        'webauthn_register_displayname': 'webauthn_register_displayname',  # noqa: E501
        'password': 'password',  # noqa: E501
        'traits': 'traits',  # noqa: E501
        'provider': 'provider',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """SubmitSelfServiceRegistrationFlowBody - a model defined in OpenAPI

        Keyword Args:
            method (str): Method  Should be set to \"webauthn\" when trying to add, update, or remove a webAuthn pairing.
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            csrf_token (str): CSRFToken is the anti-CSRF token. [optional]  # noqa: E501
            webauthn_register (str): Register a WebAuthn Security Key  It is expected that the JSON returned by the WebAuthn registration process is included here.. [optional]  # noqa: E501
            webauthn_register_displayname (str): Name of the WebAuthn Security Key to be Added  A human-readable name for the security key which will be added.. [optional]  # noqa: E501
            password (str): Password to sign the user up with. [optional]  # noqa: E501
            traits ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): The identity's traits. [optional]  # noqa: E501
            provider (str): The provider to register with. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """SubmitSelfServiceRegistrationFlowBody - a model defined in OpenAPI

        Keyword Args:
            method (str): Method  Should be set to \"webauthn\" when trying to add, update, or remove a webAuthn pairing.
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            csrf_token (str): CSRFToken is the anti-CSRF token. [optional]  # noqa: E501
            webauthn_register (str): Register a WebAuthn Security Key  It is expected that the JSON returned by the WebAuthn registration process is included here.. [optional]  # noqa: E501
            webauthn_register_displayname (str): Name of the WebAuthn Security Key to be Added  A human-readable name for the security key which will be added.. [optional]  # noqa: E501
            password (str): Password to sign the user up with. [optional]  # noqa: E501
            traits ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): The identity's traits. [optional]  # noqa: E501
            provider (str): The provider to register with. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
          ],
          'oneOf': [
              SubmitSelfServiceRegistrationFlowWithOidcMethodBody,
              SubmitSelfServiceRegistrationFlowWithPasswordMethodBody,
              SubmitSelfServiceRegistrationFlowWithWebAuthnMethodBody,
          ],
        }
