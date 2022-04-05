# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.16.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InventoryItemListing(object):
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
        'offer_id': 'str',
        'sku': 'str'
    }

    attribute_map = {
        'offer_id': 'offerId',
        'sku': 'sku'
    }

    def __init__(self, offer_id=None, sku=None):  # noqa: E501
        """InventoryItemListing - a model defined in Swagger"""  # noqa: E501
        self._offer_id = None
        self._sku = None
        self.discriminator = None
        if offer_id is not None:
            self.offer_id = offer_id
        if sku is not None:
            self.sku = sku

    @property
    def offer_id(self):
        """Gets the offer_id of this InventoryItemListing.  # noqa: E501

        Upon a successful migration of a listing, eBay auto-generates this unique identifier, and this offer ID value will be used to retrieve and manage the newly-created offer object. This value will only be generated and returned if the eBay listing is migrated successfully.  # noqa: E501

        :return: The offer_id of this InventoryItemListing.  # noqa: E501
        :rtype: str
        """
        return self._offer_id

    @offer_id.setter
    def offer_id(self, offer_id):
        """Sets the offer_id of this InventoryItemListing.

        Upon a successful migration of a listing, eBay auto-generates this unique identifier, and this offer ID value will be used to retrieve and manage the newly-created offer object. This value will only be generated and returned if the eBay listing is migrated successfully.  # noqa: E501

        :param offer_id: The offer_id of this InventoryItemListing.  # noqa: E501
        :type: str
        """

        self._offer_id = offer_id

    @property
    def sku(self):
        """Gets the sku of this InventoryItemListing.  # noqa: E501

        This is the seller-defined SKU value associated with the item(s) in a listing. This same SKU value will be used to retrieve and manage the newly-created inventory item object if the listing migration is successful. This SKU value will get returned even if the migration is not successful.  # noqa: E501

        :return: The sku of this InventoryItemListing.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this InventoryItemListing.

        This is the seller-defined SKU value associated with the item(s) in a listing. This same SKU value will be used to retrieve and manage the newly-created inventory item object if the listing migration is successful. This SKU value will get returned even if the migration is not successful.  # noqa: E501

        :param sku: The sku of this InventoryItemListing.  # noqa: E501
        :type: str
        """

        self._sku = sku

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
        if issubclass(InventoryItemListing, dict):
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
        if not isinstance(other, InventoryItemListing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
