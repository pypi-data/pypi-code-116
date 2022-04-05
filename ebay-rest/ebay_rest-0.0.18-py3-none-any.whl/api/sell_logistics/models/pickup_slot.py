# coding: utf-8

"""
    Logistics API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The <b>Logistics API</b> resources offer the following capabilities: <ul><li><b>shipping_quote</b> &ndash; Consolidates into a list a set of live shipping rates, or quotes, from which you can select a rate to ship a package.</li> <li><b>shipment</b> &ndash; Creates a \"shipment\" for the selected shipping rate.</li></ul> Call <b>createShippingQuote</b> to get a list of live shipping rates. The rates returned are all valid for a specific time window and all quoted prices are at eBay-negotiated rates. <br><br>Select one of the live rates and using its associated <b>rateId</b>, create a \"shipment\" for the package by calling <b>createFromShippingQuote</b>. Creating a shipment completes an agreement, and the cost of the base service and any added shipping options are summed into the returned <b>totalShippingCost</b> value. This action also generates a shipping label that you can use to ship the package.  The total cost of the shipment is incurred when the package is shipped using the supplied shipping label.  <p class=\"tablenote\"><b>Important!</b> Sellers must set up a payment method via their eBay account before they can use the methods in this API to create a shipment and the associated shipping label.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PickupSlot(object):
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
        'pickup_slot_end_time': 'str',
        'pickup_slot_id': 'str',
        'pickup_slot_start_time': 'str',
        'pickup_slot_time_zone': 'str'
    }

    attribute_map = {
        'pickup_slot_end_time': 'pickupSlotEndTime',
        'pickup_slot_id': 'pickupSlotId',
        'pickup_slot_start_time': 'pickupSlotStartTime',
        'pickup_slot_time_zone': 'pickupSlotTimeZone'
    }

    def __init__(self, pickup_slot_end_time=None, pickup_slot_id=None, pickup_slot_start_time=None, pickup_slot_time_zone=None):  # noqa: E501
        """PickupSlot - a model defined in Swagger"""  # noqa: E501
        self._pickup_slot_end_time = None
        self._pickup_slot_id = None
        self._pickup_slot_start_time = None
        self._pickup_slot_time_zone = None
        self.discriminator = None
        if pickup_slot_end_time is not None:
            self.pickup_slot_end_time = pickup_slot_end_time
        if pickup_slot_id is not None:
            self.pickup_slot_id = pickup_slot_id
        if pickup_slot_start_time is not None:
            self.pickup_slot_start_time = pickup_slot_start_time
        if pickup_slot_time_zone is not None:
            self.pickup_slot_time_zone = pickup_slot_time_zone

    @property
    def pickup_slot_end_time(self):
        """Gets the pickup_slot_end_time of this PickupSlot.  # noqa: E501

        The date and time the pickup slot ends, formatted as an ISO 8601 string, which is based on the 24-hour Coordinated Universal Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS].[SSS]Z Example: 2018-08-20T07:09:00.000Z  # noqa: E501

        :return: The pickup_slot_end_time of this PickupSlot.  # noqa: E501
        :rtype: str
        """
        return self._pickup_slot_end_time

    @pickup_slot_end_time.setter
    def pickup_slot_end_time(self, pickup_slot_end_time):
        """Sets the pickup_slot_end_time of this PickupSlot.

        The date and time the pickup slot ends, formatted as an ISO 8601 string, which is based on the 24-hour Coordinated Universal Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS].[SSS]Z Example: 2018-08-20T07:09:00.000Z  # noqa: E501

        :param pickup_slot_end_time: The pickup_slot_end_time of this PickupSlot.  # noqa: E501
        :type: str
        """

        self._pickup_slot_end_time = pickup_slot_end_time

    @property
    def pickup_slot_id(self):
        """Gets the pickup_slot_id of this PickupSlot.  # noqa: E501

        Seller-defined name for the pickup slot.  # noqa: E501

        :return: The pickup_slot_id of this PickupSlot.  # noqa: E501
        :rtype: str
        """
        return self._pickup_slot_id

    @pickup_slot_id.setter
    def pickup_slot_id(self, pickup_slot_id):
        """Sets the pickup_slot_id of this PickupSlot.

        Seller-defined name for the pickup slot.  # noqa: E501

        :param pickup_slot_id: The pickup_slot_id of this PickupSlot.  # noqa: E501
        :type: str
        """

        self._pickup_slot_id = pickup_slot_id

    @property
    def pickup_slot_start_time(self):
        """Gets the pickup_slot_start_time of this PickupSlot.  # noqa: E501

        The date and time the pickup slot begins, formatted as an ISO 8601 UTC string.  # noqa: E501

        :return: The pickup_slot_start_time of this PickupSlot.  # noqa: E501
        :rtype: str
        """
        return self._pickup_slot_start_time

    @pickup_slot_start_time.setter
    def pickup_slot_start_time(self, pickup_slot_start_time):
        """Sets the pickup_slot_start_time of this PickupSlot.

        The date and time the pickup slot begins, formatted as an ISO 8601 UTC string.  # noqa: E501

        :param pickup_slot_start_time: The pickup_slot_start_time of this PickupSlot.  # noqa: E501
        :type: str
        """

        self._pickup_slot_start_time = pickup_slot_start_time

    @property
    def pickup_slot_time_zone(self):
        """Gets the pickup_slot_time_zone of this PickupSlot.  # noqa: E501

        The time zone of the pickup location, returned as Time Zone Database ID (also know as an Olson time zone ID).  # noqa: E501

        :return: The pickup_slot_time_zone of this PickupSlot.  # noqa: E501
        :rtype: str
        """
        return self._pickup_slot_time_zone

    @pickup_slot_time_zone.setter
    def pickup_slot_time_zone(self, pickup_slot_time_zone):
        """Sets the pickup_slot_time_zone of this PickupSlot.

        The time zone of the pickup location, returned as Time Zone Database ID (also know as an Olson time zone ID).  # noqa: E501

        :param pickup_slot_time_zone: The pickup_slot_time_zone of this PickupSlot.  # noqa: E501
        :type: str
        """

        self._pickup_slot_time_zone = pickup_slot_time_zone

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
        if issubclass(PickupSlot, dict):
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
        if not isinstance(other, PickupSlot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
