# coding: utf-8

"""
    Catalog API

    The Catalog API allows users to search for and locate an eBay catalog product that is a direct match for the product that they wish to sell. Listing against an eBay catalog product helps insure that all listings (based off of that catalog product) have complete and accurate information. In addition to helping to create high-quality listings, another benefit to the seller of using catalog information to create listings is that much of the details of the listing will be prefilled, including the listing title, the listing description, the item specifics, and a stock image for the product (if available). Sellers will not have to enter item specifics themselves, and the overall listing process is a lot faster and easier.  # noqa: E501

    OpenAPI spec version: v1_beta.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProductSearchResponse(object):
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
        'href': 'str',
        'limit': 'int',
        'next': 'str',
        'offset': 'int',
        'prev': 'str',
        'product_summaries': 'list[ProductSummary]',
        'refinement': 'Refinement',
        'total': 'int'
    }

    attribute_map = {
        'href': 'href',
        'limit': 'limit',
        'next': 'next',
        'offset': 'offset',
        'prev': 'prev',
        'product_summaries': 'productSummaries',
        'refinement': 'refinement',
        'total': 'total'
    }

    def __init__(self, href=None, limit=None, next=None, offset=None, prev=None, product_summaries=None, refinement=None, total=None):  # noqa: E501
        """ProductSearchResponse - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._limit = None
        self._next = None
        self._offset = None
        self._prev = None
        self._product_summaries = None
        self._refinement = None
        self._total = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if limit is not None:
            self.limit = limit
        if next is not None:
            self.next = next
        if offset is not None:
            self.offset = offset
        if prev is not None:
            self.prev = prev
        if product_summaries is not None:
            self.product_summaries = product_summaries
        if refinement is not None:
            self.refinement = refinement
        if total is not None:
            self.total = total

    @property
    def href(self):
        """Gets the href of this ProductSearchResponse.  # noqa: E501

        This field is reserved for internal or future use.  # noqa: E501

        :return: The href of this ProductSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ProductSearchResponse.

        This field is reserved for internal or future use.  # noqa: E501

        :param href: The href of this ProductSearchResponse.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def limit(self):
        """Gets the limit of this ProductSearchResponse.  # noqa: E501

        The number of product summaries returned in the response. This is the result set, a subset of the full collection of products that match the search or filter criteria of this call. If the limit query parameter was included in the request, this field will have the same value. Default: 50  # noqa: E501

        :return: The limit of this ProductSearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ProductSearchResponse.

        The number of product summaries returned in the response. This is the result set, a subset of the full collection of products that match the search or filter criteria of this call. If the limit query parameter was included in the request, this field will have the same value. Default: 50  # noqa: E501

        :param limit: The limit of this ProductSearchResponse.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """Gets the next of this ProductSearchResponse.  # noqa: E501

        This field is reserved for internal or future use.  # noqa: E501

        :return: The next of this ProductSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this ProductSearchResponse.

        This field is reserved for internal or future use.  # noqa: E501

        :param next: The next of this ProductSearchResponse.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def offset(self):
        """Gets the offset of this ProductSearchResponse.  # noqa: E501

        This field is reserved for internal or future use.  # noqa: E501

        :return: The offset of this ProductSearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ProductSearchResponse.

        This field is reserved for internal or future use.  # noqa: E501

        :param offset: The offset of this ProductSearchResponse.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def prev(self):
        """Gets the prev of this ProductSearchResponse.  # noqa: E501

        This field is reserved for internal or future use.  # noqa: E501

        :return: The prev of this ProductSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this ProductSearchResponse.

        This field is reserved for internal or future use.  # noqa: E501

        :param prev: The prev of this ProductSearchResponse.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def product_summaries(self):
        """Gets the product_summaries of this ProductSearchResponse.  # noqa: E501

        Returned if the fieldGroups query parameter was omitted from the request, or if it was included with a value of MATCHING_PRODUCTS or FULL. This container provides an array of product summaries in the current result set for products that match the combination of the q, category_ids, and aspect_filter parameters that were provided in the request. Each product summary includes information about the product's identifiers, product images, aspects, the product page URL, and the getProduct URL for retrieving the product details.  # noqa: E501

        :return: The product_summaries of this ProductSearchResponse.  # noqa: E501
        :rtype: list[ProductSummary]
        """
        return self._product_summaries

    @product_summaries.setter
    def product_summaries(self, product_summaries):
        """Sets the product_summaries of this ProductSearchResponse.

        Returned if the fieldGroups query parameter was omitted from the request, or if it was included with a value of MATCHING_PRODUCTS or FULL. This container provides an array of product summaries in the current result set for products that match the combination of the q, category_ids, and aspect_filter parameters that were provided in the request. Each product summary includes information about the product's identifiers, product images, aspects, the product page URL, and the getProduct URL for retrieving the product details.  # noqa: E501

        :param product_summaries: The product_summaries of this ProductSearchResponse.  # noqa: E501
        :type: list[ProductSummary]
        """

        self._product_summaries = product_summaries

    @property
    def refinement(self):
        """Gets the refinement of this ProductSearchResponse.  # noqa: E501


        :return: The refinement of this ProductSearchResponse.  # noqa: E501
        :rtype: Refinement
        """
        return self._refinement

    @refinement.setter
    def refinement(self, refinement):
        """Sets the refinement of this ProductSearchResponse.


        :param refinement: The refinement of this ProductSearchResponse.  # noqa: E501
        :type: Refinement
        """

        self._refinement = refinement

    @property
    def total(self):
        """Gets the total of this ProductSearchResponse.  # noqa: E501

        This field is reserved for internal or future use.  # noqa: E501

        :return: The total of this ProductSearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ProductSearchResponse.

        This field is reserved for internal or future use.  # noqa: E501

        :param total: The total of this ProductSearchResponse.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(ProductSearchResponse, dict):
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
        if not isinstance(other, ProductSearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
