# coding: utf-8

"""
    Deal API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />This API allows third-party developers to search for and retrieve details about eBay deals and events, as well as the items associated with those deals and events.  # noqa: E501

    OpenAPI spec version: v1.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ...buy_deal.api_client import ApiClient


class EventItemApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_event_items(self, event_ids, x_ebay_c_marketplace_id, **kwargs):  # noqa: E501
        """get_event_items  # noqa: E501

        This method returns a paginated set of event items. The result set contains all event items associated with the specified search criteria and marketplace ID. Request headers This method uses the X-EBAY-C-ENDUSERCTX request header to support revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and delivery time estimations. For details see, Request headers in the Buying Integration Guide. Restrictions This method can return a maximum of 10,000 items. For a list of supported sites and other restrictions, see API Restrictions. eBay Partner Network: In order to receive a commission for your sales, you must use the URL returned in the itemAffiliateWebUrl field to forward your buyer to the ebay.com site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event_items(event_ids, x_ebay_c_marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_ids: The unique identifiers for the eBay events. Maximum Value: 1 (required)
        :param str x_ebay_c_marketplace_id: A header used to specify the eBay marketplace ID. (required)
        :param str category_ids: The unique identifier of the eBay category for the search. Maximum Value: 1
        :param str delivery_country: A filter for items that can be shipped to the specified country.
        :param str limit: The maximum number of items, from the current result set, returned on a single page. Default: 20
        :param str offset: The number of items that will be skipped in the result set. This is used with the limit field to control the pagination of the output. For example, if the offset is set to 0 and the limit is set to 10, the method will retrieve items 1 through 10 from the list of items returned. If the offset is set to 10 and the limit is set to 10, the method will retrieve items 11 through 20 from the list of items returned. Default: 0
        :return: EventItemSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_event_items_with_http_info(event_ids, x_ebay_c_marketplace_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_event_items_with_http_info(event_ids, x_ebay_c_marketplace_id, **kwargs)  # noqa: E501
            return data

    def get_event_items_with_http_info(self, event_ids, x_ebay_c_marketplace_id, **kwargs):  # noqa: E501
        """get_event_items  # noqa: E501

        This method returns a paginated set of event items. The result set contains all event items associated with the specified search criteria and marketplace ID. Request headers This method uses the X-EBAY-C-ENDUSERCTX request header to support revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and delivery time estimations. For details see, Request headers in the Buying Integration Guide. Restrictions This method can return a maximum of 10,000 items. For a list of supported sites and other restrictions, see API Restrictions. eBay Partner Network: In order to receive a commission for your sales, you must use the URL returned in the itemAffiliateWebUrl field to forward your buyer to the ebay.com site.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event_items_with_http_info(event_ids, x_ebay_c_marketplace_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_ids: The unique identifiers for the eBay events. Maximum Value: 1 (required)
        :param str x_ebay_c_marketplace_id: A header used to specify the eBay marketplace ID. (required)
        :param str category_ids: The unique identifier of the eBay category for the search. Maximum Value: 1
        :param str delivery_country: A filter for items that can be shipped to the specified country.
        :param str limit: The maximum number of items, from the current result set, returned on a single page. Default: 20
        :param str offset: The number of items that will be skipped in the result set. This is used with the limit field to control the pagination of the output. For example, if the offset is set to 0 and the limit is set to 10, the method will retrieve items 1 through 10 from the list of items returned. If the offset is set to 10 and the limit is set to 10, the method will retrieve items 11 through 20 from the list of items returned. Default: 0
        :return: EventItemSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_ids', 'x_ebay_c_marketplace_id', 'category_ids', 'delivery_country', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_event_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_ids' is set
        if ('event_ids' not in params or
                params['event_ids'] is None):
            raise ValueError("Missing the required parameter `event_ids` when calling `get_event_items`")  # noqa: E501
        # verify the required parameter 'x_ebay_c_marketplace_id' is set
        if ('x_ebay_c_marketplace_id' not in params or
                params['x_ebay_c_marketplace_id'] is None):
            raise ValueError("Missing the required parameter `x_ebay_c_marketplace_id` when calling `get_event_items`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category_ids' in params:
            query_params.append(('category_ids', params['category_ids']))  # noqa: E501
        if 'delivery_country' in params:
            query_params.append(('delivery_country', params['delivery_country']))  # noqa: E501
        if 'event_ids' in params:
            query_params.append(('event_ids', params['event_ids']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}
        if 'x_ebay_c_marketplace_id' in params:
            header_params['X-EBAY-C-MARKETPLACE-ID'] = params['x_ebay_c_marketplace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_auth']  # noqa: E501

        return self.api_client.call_api(
            '/event_item', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventItemSearchResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
