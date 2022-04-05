# coding: utf-8

"""
    Order API

    <span class=\"tablenote\"><b>Note:</b> This version of the Order API (v2) currently only supports the guest payment flow for eBay managed payments. To view the v1_beta version of the Order API, which includes both member and guest checkout payment flows, refer to the <a href=\"/api-docs/buy/order_v1/resources/methods\">Order_v1 API</a> documentation.</span><br /><br /><span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"><img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\"  alt=\"Limited Release\" title=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The Order API provides interfaces that let shoppers pay for items. It also returns payment and shipping status of the order.  # noqa: E501

    OpenAPI spec version: v2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShippingAddress(object):
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
        'address_line1': 'str',
        'address_line2': 'str',
        'city': 'str',
        'country': 'str',
        'county': 'str',
        'phone_number': 'str',
        'postal_code': 'str',
        'recipient': 'Recipient',
        'state_or_province': 'str'
    }

    attribute_map = {
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'city': 'city',
        'country': 'country',
        'county': 'county',
        'phone_number': 'phoneNumber',
        'postal_code': 'postalCode',
        'recipient': 'recipient',
        'state_or_province': 'stateOrProvince'
    }

    def __init__(self, address_line1=None, address_line2=None, city=None, country=None, county=None, phone_number=None, postal_code=None, recipient=None, state_or_province=None):  # noqa: E501
        """ShippingAddress - a model defined in Swagger"""  # noqa: E501
        self._address_line1 = None
        self._address_line2 = None
        self._city = None
        self._country = None
        self._county = None
        self._phone_number = None
        self._postal_code = None
        self._recipient = None
        self._state_or_province = None
        self.discriminator = None
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if county is not None:
            self.county = county
        if phone_number is not None:
            self.phone_number = phone_number
        if postal_code is not None:
            self.postal_code = postal_code
        if recipient is not None:
            self.recipient = recipient
        if state_or_province is not None:
            self.state_or_province = state_or_province

    @property
    def address_line1(self):
        """Gets the address_line1 of this ShippingAddress.  # noqa: E501

        The first line of the street address where the item is being shipped.<br /><br /><b>Maximum:</b><ul><li>40 characters for AU, CA, and US marketplaces</li><li>35 characters for DE and GB marketplaces</li><li>50 characters for all other marketplaces</li></ul>  # noqa: E501

        :return: The address_line1 of this ShippingAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this ShippingAddress.

        The first line of the street address where the item is being shipped.<br /><br /><b>Maximum:</b><ul><li>40 characters for AU, CA, and US marketplaces</li><li>35 characters for DE and GB marketplaces</li><li>50 characters for all other marketplaces</li></ul>  # noqa: E501

        :param address_line1: The address_line1 of this ShippingAddress.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this ShippingAddress.  # noqa: E501

        The second line of the street address where the item is being shipped. This optional field can be used for information such as 'Suite Number' or 'Apt Number'.<br /><br /><b>Maximum:</b><ul><li>40 characters for AU, CA, and US marketplaces</li><li>35 characters for DE and GB marketplaces</li><li>50 characters for all other marketplaces</li></ul>  # noqa: E501

        :return: The address_line2 of this ShippingAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this ShippingAddress.

        The second line of the street address where the item is being shipped. This optional field can be used for information such as 'Suite Number' or 'Apt Number'.<br /><br /><b>Maximum:</b><ul><li>40 characters for AU, CA, and US marketplaces</li><li>35 characters for DE and GB marketplaces</li><li>50 characters for all other marketplaces</li></ul>  # noqa: E501

        :param address_line2: The address_line2 of this ShippingAddress.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """Gets the city of this ShippingAddress.  # noqa: E501

        The city of the address where the item is being shipped.  # noqa: E501

        :return: The city of this ShippingAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ShippingAddress.

        The city of the address where the item is being shipped.  # noqa: E501

        :param city: The city of this ShippingAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this ShippingAddress.  # noqa: E501

        The two letter code representing the country of the address. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/order/types/bas:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The country of this ShippingAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ShippingAddress.

        The two letter code representing the country of the address. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/order/types/bas:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param country: The country of this ShippingAddress.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def county(self):
        """Gets the county of this ShippingAddress.  # noqa: E501

        The county of the address where the item is being shipped.  # noqa: E501

        :return: The county of this ShippingAddress.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this ShippingAddress.

        The county of the address where the item is being shipped.  # noqa: E501

        :param county: The county of this ShippingAddress.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def phone_number(self):
        """Gets the phone_number of this ShippingAddress.  # noqa: E501

        The phone number of the person receiving the package.<br /><br /><span class=\"tablenote\"><b>Note:</b> It is highly recommended that when entering the phone number you include the country code.<br /><br />For example, if a US phone number is <code>4********4</code>, you would enter <code>+14********4</code>. If you do not include this code, the service will use the country specified in the <b>country</b> field.<br /><br />You can find the country code at <a href=\"https://countrycode.org/\">https://countrycode.org</a>.</span>  # noqa: E501

        :return: The phone_number of this ShippingAddress.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ShippingAddress.

        The phone number of the person receiving the package.<br /><br /><span class=\"tablenote\"><b>Note:</b> It is highly recommended that when entering the phone number you include the country code.<br /><br />For example, if a US phone number is <code>4********4</code>, you would enter <code>+14********4</code>. If you do not include this code, the service will use the country specified in the <b>country</b> field.<br /><br />You can find the country code at <a href=\"https://countrycode.org/\">https://countrycode.org</a>.</span>  # noqa: E501

        :param phone_number: The phone_number of this ShippingAddress.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def postal_code(self):
        """Gets the postal_code of this ShippingAddress.  # noqa: E501

        The postal code of the address where the item is being shipped.<br /><br /><span class=\"tablenote\"><b>Note:</b> This is optional when shipping to EBAY_HK (Hong Kong).</span>  # noqa: E501

        :return: The postal_code of this ShippingAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ShippingAddress.

        The postal code of the address where the item is being shipped.<br /><br /><span class=\"tablenote\"><b>Note:</b> This is optional when shipping to EBAY_HK (Hong Kong).</span>  # noqa: E501

        :param postal_code: The postal_code of this ShippingAddress.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def recipient(self):
        """Gets the recipient of this ShippingAddress.  # noqa: E501


        :return: The recipient of this ShippingAddress.  # noqa: E501
        :rtype: Recipient
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this ShippingAddress.


        :param recipient: The recipient of this ShippingAddress.  # noqa: E501
        :type: Recipient
        """

        self._recipient = recipient

    @property
    def state_or_province(self):
        """Gets the state_or_province of this ShippingAddress.  # noqa: E501

        The state or province of the address.<br /><br /><span class=\"tablenote\"><b>Note:</b> For the US marketplace, this is a two-character value. For a list of valid values, see <a href=\"https://www.ups.com/worldshiphelp/WS15/ENU/AppHelp/Codes/State_Province_Codes.htm\">US State and Canada Province Codes</a>. </span>  # noqa: E501

        :return: The state_or_province of this ShippingAddress.  # noqa: E501
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province):
        """Sets the state_or_province of this ShippingAddress.

        The state or province of the address.<br /><br /><span class=\"tablenote\"><b>Note:</b> For the US marketplace, this is a two-character value. For a list of valid values, see <a href=\"https://www.ups.com/worldshiphelp/WS15/ENU/AppHelp/Codes/State_Province_Codes.htm\">US State and Canada Province Codes</a>. </span>  # noqa: E501

        :param state_or_province: The state_or_province of this ShippingAddress.  # noqa: E501
        :type: str
        """

        self._state_or_province = state_or_province

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
        if issubclass(ShippingAddress, dict):
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
        if not isinstance(other, ShippingAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
