# coding: utf-8

"""
    Item Feed Service

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The Feed API provides the ability to download TSV_GZIP feed files containing eBay items and an hourly snapshot file of the items that have changed within an hour for a specific category, date and marketplace. <p>In addition to the API, there is an open source <a href=\"https://github.com/eBay/FeedSDK \" target=\"_blank\">Feed SDK</a> written in Java that downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.32.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ItemResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'items': 'list[Item]'
    }

    attribute_map = {
        'items': 'items'
    }

    def __init__(self, items=None):  # noqa: E501
        """ItemResponse - a model defined in Swagger"""  # noqa: E501
        self._items = None
        self.discriminator = None
        if items is not None:
            self.items = items

    @property
    def items(self):
        """Gets the items of this ItemResponse.  # noqa: E501

        The container for the array of items returned by the <b> getItemFeed</b> method. The data in the file is tab separated and the first row is the header, which labels the columns and indicates the order of the values on each line. The header labels match the fields that are described in the <a href=\"/api-docs/buy/feed/resources/item/methods/getItemFeed#h3-response-fields\">Response fields</a> section.  # noqa: E501

        :return: The items of this ItemResponse.  # noqa: E501
        :rtype: list[Item]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ItemResponse.

        The container for the array of items returned by the <b> getItemFeed</b> method. The data in the file is tab separated and the first row is the header, which labels the columns and indicates the order of the values on each line. The header labels match the fields that are described in the <a href=\"/api-docs/buy/feed/resources/item/methods/getItemFeed#h3-response-fields\">Response fields</a> section.  # noqa: E501

        :param items: The items of this ItemResponse.  # noqa: E501
        :type: list[Item]
        """

        self._items = items

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ItemResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
