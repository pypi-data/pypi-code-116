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

class AvailabilityDistribution(object):
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
        'fulfillment_time': 'TimeDuration',
        'merchant_location_key': 'str',
        'quantity': 'int'
    }

    attribute_map = {
        'fulfillment_time': 'fulfillmentTime',
        'merchant_location_key': 'merchantLocationKey',
        'quantity': 'quantity'
    }

    def __init__(self, fulfillment_time=None, merchant_location_key=None, quantity=None):  # noqa: E501
        """AvailabilityDistribution - a model defined in Swagger"""  # noqa: E501
        self._fulfillment_time = None
        self._merchant_location_key = None
        self._quantity = None
        self.discriminator = None
        if fulfillment_time is not None:
            self.fulfillment_time = fulfillment_time
        if merchant_location_key is not None:
            self.merchant_location_key = merchant_location_key
        if quantity is not None:
            self.quantity = quantity

    @property
    def fulfillment_time(self):
        """Gets the fulfillment_time of this AvailabilityDistribution.  # noqa: E501


        :return: The fulfillment_time of this AvailabilityDistribution.  # noqa: E501
        :rtype: TimeDuration
        """
        return self._fulfillment_time

    @fulfillment_time.setter
    def fulfillment_time(self, fulfillment_time):
        """Sets the fulfillment_time of this AvailabilityDistribution.


        :param fulfillment_time: The fulfillment_time of this AvailabilityDistribution.  # noqa: E501
        :type: TimeDuration
        """

        self._fulfillment_time = fulfillment_time

    @property
    def merchant_location_key(self):
        """Gets the merchant_location_key of this AvailabilityDistribution.  # noqa: E501

        The unique identifier of an inventory location where quantity is available for the inventory item. This field is conditionally required to identify the inventory location that has quantity of the inventory item.  # noqa: E501

        :return: The merchant_location_key of this AvailabilityDistribution.  # noqa: E501
        :rtype: str
        """
        return self._merchant_location_key

    @merchant_location_key.setter
    def merchant_location_key(self, merchant_location_key):
        """Sets the merchant_location_key of this AvailabilityDistribution.

        The unique identifier of an inventory location where quantity is available for the inventory item. This field is conditionally required to identify the inventory location that has quantity of the inventory item.  # noqa: E501

        :param merchant_location_key: The merchant_location_key of this AvailabilityDistribution.  # noqa: E501
        :type: str
        """

        self._merchant_location_key = merchant_location_key

    @property
    def quantity(self):
        """Gets the quantity of this AvailabilityDistribution.  # noqa: E501

        The integer value passed into this field indicates the quantity of the inventory item that is available at this inventory location. This field is conditionally required.  # noqa: E501

        :return: The quantity of this AvailabilityDistribution.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this AvailabilityDistribution.

        The integer value passed into this field indicates the quantity of the inventory item that is available at this inventory location. This field is conditionally required.  # noqa: E501

        :param quantity: The quantity of this AvailabilityDistribution.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

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
        if issubclass(AvailabilityDistribution, dict):
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
        if not isinstance(other, AvailabilityDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
