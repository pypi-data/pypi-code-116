# coding: utf-8

"""
    eBay Finances API

    This API is used to retrieve seller payouts and monetary transaction details related to those payouts.  # noqa: E501

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PayoutInstrument(object):
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
        'account_last_four_digits': 'str',
        'instrument_type': 'str',
        'nickname': 'str'
    }

    attribute_map = {
        'account_last_four_digits': 'accountLastFourDigits',
        'instrument_type': 'instrumentType',
        'nickname': 'nickname'
    }

    def __init__(self, account_last_four_digits=None, instrument_type=None, nickname=None):  # noqa: E501
        """PayoutInstrument - a model defined in Swagger"""  # noqa: E501
        self._account_last_four_digits = None
        self._instrument_type = None
        self._nickname = None
        self.discriminator = None
        if account_last_four_digits is not None:
            self.account_last_four_digits = account_last_four_digits
        if instrument_type is not None:
            self.instrument_type = instrument_type
        if nickname is not None:
            self.nickname = nickname

    @property
    def account_last_four_digits(self):
        """Gets the account_last_four_digits of this PayoutInstrument.  # noqa: E501

        This string value is the last four digits of the seller's account number.  # noqa: E501

        :return: The account_last_four_digits of this PayoutInstrument.  # noqa: E501
        :rtype: str
        """
        return self._account_last_four_digits

    @account_last_four_digits.setter
    def account_last_four_digits(self, account_last_four_digits):
        """Sets the account_last_four_digits of this PayoutInstrument.

        This string value is the last four digits of the seller's account number.  # noqa: E501

        :param account_last_four_digits: The account_last_four_digits of this PayoutInstrument.  # noqa: E501
        :type: str
        """

        self._account_last_four_digits = account_last_four_digits

    @property
    def instrument_type(self):
        """Gets the instrument_type of this PayoutInstrument.  # noqa: E501

        This string value indicates the type of account that received the payout. At this time, seller payouts can only be distributed to bank acounts, so the string value returned in this field will always be <code>BANK</code>.  # noqa: E501

        :return: The instrument_type of this PayoutInstrument.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this PayoutInstrument.

        This string value indicates the type of account that received the payout. At this time, seller payouts can only be distributed to bank acounts, so the string value returned in this field will always be <code>BANK</code>.  # noqa: E501

        :param instrument_type: The instrument_type of this PayoutInstrument.  # noqa: E501
        :type: str
        """

        self._instrument_type = instrument_type

    @property
    def nickname(self):
        """Gets the nickname of this PayoutInstrument.  # noqa: E501

        This string value is a seller-provided nickname that the seller uses to represent the bank account.  # noqa: E501

        :return: The nickname of this PayoutInstrument.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this PayoutInstrument.

        This string value is a seller-provided nickname that the seller uses to represent the bank account.  # noqa: E501

        :param nickname: The nickname of this PayoutInstrument.  # noqa: E501
        :type: str
        """

        self._nickname = nickname

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
        if issubclass(PayoutInstrument, dict):
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
        if not isinstance(other, PayoutInstrument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
