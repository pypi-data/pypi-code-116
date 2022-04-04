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
from rockset.model.error_model import ErrorModel
from rockset.model.query_request import QueryRequest
from rockset.model.query_response import QueryResponse
from rockset.model.validate_query_response import ValidateQueryResponse
from rockset.models import *


class QueriesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.query_endpoint = _Endpoint(
            settings={
                'response_type': (QueryResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/queries'.split('#')[0],
                'operation_id': 'query',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'query_request',
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
                    'query_request':
                        (QueryRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'query_request': 'body',
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
        self.validate_endpoint = _Endpoint(
            settings={
                'response_type': (ValidateQueryResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/queries/validations'.split('#')[0],
                'operation_id': 'validate',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'query_request',
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
                    'query_request':
                        (QueryRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'query_request': 'body',
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

    def query(
        self,
        *,
        sql: QueryRequestSql,
        **kwargs
    ) -> typing.Union[QueryResponse, asyncio.Future]:
        """Query  # noqa: E501

        Make a SQL query to Rockset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(apikey=APIKEY)
        future = rs.QueriesApi.query(
            sql=QueryRequestSql(
                default_row_limit=1,
                generate_warnings=True,
                initial_paginate_response_doc_count=1,
                paginate=True,
                parameters=[
                    QueryParameter(
                        name="_id",
                        type="string",
                        value="85beb391",
                    ),
                ],
                query="SELECT * FROM foo where _id = :_id",
            ),
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            sql (QueryRequestSql): [required]
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
            QueryResponse
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
        kwargs['query_request'] = \
            kwargs['query_request']
        return self.query_endpoint.call_with_http_info(**kwargs)

    def validate(
        self,
        *,
        sql: QueryRequestSql,
        **kwargs
    ) -> typing.Union[ValidateQueryResponse, asyncio.Future]:
        """Validate Query  # noqa: E501

        Validate a SQL query with Rockset's parser and planner.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(apikey=APIKEY)
        future = rs.QueriesApi.validate(
            sql=QueryRequestSql(
                default_row_limit=1,
                generate_warnings=True,
                initial_paginate_response_doc_count=1,
                paginate=True,
                parameters=[
                    QueryParameter(
                        name="_id",
                        type="string",
                        value="85beb391",
                    ),
                ],
                query="SELECT * FROM foo where _id = :_id",
            ),
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            sql (QueryRequestSql): [required]
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
            ValidateQueryResponse
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
        kwargs['query_request'] = \
            kwargs['query_request']
        return self.validate_endpoint.call_with_http_info(**kwargs)


    body_params_dict = dict()
    return_types_dict = dict()
    body_params_dict['query'] = 'query_request'
    return_types_dict['query'] = QueryRequest
    body_params_dict['validate'] = 'query_request'
    return_types_dict['validate'] = QueryRequest
