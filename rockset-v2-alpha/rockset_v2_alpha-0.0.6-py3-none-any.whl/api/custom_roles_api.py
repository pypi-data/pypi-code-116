"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

import asyncio

from rockset.api_client import ApiClient, Endpoint as _Endpoint
from rockset.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from rockset.model.create_role_request import CreateRoleRequest
from rockset.model.error_model import ErrorModel
from rockset.model.list_roles_response import ListRolesResponse
from rockset.model.role_response import RoleResponse
from rockset.model.update_role_request import UpdateRoleRequest
from rockset.models import *


class CustomRolesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_role_endpoint = _Endpoint(
            settings={
                'response_type': (RoleResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/roles'.split('#')[0],
                'operation_id': 'create_role',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_role_request',
                ],
                'required': [
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'create_role_request':
                        (CreateRoleRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_role_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_role_endpoint = _Endpoint(
            settings={
                'response_type': (RoleResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/roles/{roleName}'.split('#')[0],
                'operation_id': 'delete_role',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'role_name',
                ],
                'required': [
                    'role_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'role_name':
                        (str,),
                },
                'attribute_map': {
                    'role_name': 'roleName',
                },
                'location_map': {
                    'role_name': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_role_endpoint = _Endpoint(
            settings={
                'response_type': (RoleResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/roles/{roleName}'.split('#')[0],
                'operation_id': 'get_role',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'role_name',
                ],
                'required': [
                    'role_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'role_name':
                        (str,),
                },
                'attribute_map': {
                    'role_name': 'roleName',
                },
                'location_map': {
                    'role_name': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_roles_endpoint = _Endpoint(
            settings={
                'response_type': (ListRolesResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/roles'.split('#')[0],
                'operation_id': 'list_roles',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_role_endpoint = _Endpoint(
            settings={
                'response_type': (RoleResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/roles/{roleName}'.split('#')[0],
                'operation_id': 'update_role',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'role_name',
                    'update_role_request',
                ],
                'required': [
                    'role_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'role_name':
                        (str,),
                    'update_role_request':
                        (UpdateRoleRequest,),
                },
                'attribute_map': {
                    'role_name': 'roleName',
                },
                'location_map': {
                    'role_name': 'path',
                    'update_role_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def create_role(
        self,
        *,
        description: str = None,
        privileges: typing.Sequence[Privilege] = None,
        role_name: str = None,
        **kwargs
    ) -> typing.Union[RoleResponse, asyncio.Future]:
        """Create a Role  # noqa: E501

        Create a role for your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(apikey=APIKEY)
        future = rs.CustomRolesApi.create_role(
            description="Role with read and write privileges to all collections.",
            privileges=[
                Privilege(
                    action="Create collection",
                    cluster="*ALL*",
                    resource_name="commons",
                ),
            ],
            role_name="read_write",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            description (str): Description for the role.. [optional]
            privileges ([Privilege]): List of privileges that will be associated with the role.. [optional]
            role_name (str): Unique identifier for the role.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is False.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            RoleResponse
                If the method is called asynchronously, returns an asyncio.Future which resolves to the response.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['create_role_request'] = \
            kwargs['create_role_request']
        return self.create_role_endpoint.call_with_http_info(**kwargs)

    def delete_role(
        self,
        *,
        role_name: str,
        **kwargs
    ) -> typing.Union[RoleResponse, asyncio.Future]:
        """Delete a Role  # noqa: E501

        Delete a role for your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(apikey=APIKEY)
        future = rs.CustomRolesApi.delete_role(
            role_name="roleName_example",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            role_name (str): [required]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is False.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            RoleResponse
                If the method is called asynchronously, returns an asyncio.Future which resolves to the response.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['role_name'] = \
            role_name
        return self.delete_role_endpoint.call_with_http_info(**kwargs)

    def get_role(
        self,
        *,
        role_name: str,
        **kwargs
    ) -> typing.Union[RoleResponse, asyncio.Future]:
        """Retrieve role  # noqa: E501

        Retrieve a role by name for your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(apikey=APIKEY)
        future = rs.CustomRolesApi.get_role(
            role_name="roleName_example",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            role_name (str): [required]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is False.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            RoleResponse
                If the method is called asynchronously, returns an asyncio.Future which resolves to the response.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['role_name'] = \
            role_name
        return self.get_role_endpoint.call_with_http_info(**kwargs)

    def list_roles(
        self,
        **kwargs
    ) -> typing.Union[ListRolesResponse, asyncio.Future]:
        """List Roles  # noqa: E501

        List all roles for your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(apikey=APIKEY)
        future = rs.CustomRolesApi.list_roles(
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is False.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ListRolesResponse
                If the method is called asynchronously, returns an asyncio.Future which resolves to the response.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_roles_endpoint.call_with_http_info(**kwargs)

    def update_role(
        self,
        *,
        role_name: str,
        description: str = None,
        privileges: typing.Sequence[Privilege] = None,
        **kwargs
    ) -> typing.Union[RoleResponse, asyncio.Future]:
        """Update a Role  # noqa: E501

        Update a role for your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(apikey=APIKEY)
        future = rs.CustomRolesApi.update_role(
            role_name="roleName_example",
            description="Role with read and write privileges to all collections.",
            privileges=[
                Privilege(
                    action="Create collection",
                    cluster="*ALL*",
                    resource_name="commons",
                ),
            ],
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            role_name (str): [required]
            description (str): Description for the role.. [optional]
            privileges ([Privilege]): List of privileges that will be associated with the role.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is False.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            RoleResponse
                If the method is called asynchronously, returns an asyncio.Future which resolves to the response.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['role_name'] = \
            role_name
        kwargs['update_role_request'] = \
            kwargs['update_role_request']
        return self.update_role_endpoint.call_with_http_info(**kwargs)


    body_params_dict = dict()
    return_types_dict = dict()
    body_params_dict['create_role'] = 'create_role_request'
    return_types_dict['create_role'] = CreateRoleRequest
    body_params_dict['update_role'] = 'update_role_request'
    return_types_dict['update_role'] = UpdateRoleRequest
