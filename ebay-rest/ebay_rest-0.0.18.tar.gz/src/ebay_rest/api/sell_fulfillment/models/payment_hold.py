# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentHold(object):
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
        'expected_release_date': 'str',
        'hold_amount': 'Amount',
        'hold_reason': 'str',
        'hold_state': 'str',
        'release_date': 'str',
        'seller_actions_to_release': 'list[SellerActionsToRelease]'
    }

    attribute_map = {
        'expected_release_date': 'expectedReleaseDate',
        'hold_amount': 'holdAmount',
        'hold_reason': 'holdReason',
        'hold_state': 'holdState',
        'release_date': 'releaseDate',
        'seller_actions_to_release': 'sellerActionsToRelease'
    }

    def __init__(self, expected_release_date=None, hold_amount=None, hold_reason=None, hold_state=None, release_date=None, seller_actions_to_release=None):  # noqa: E501
        """PaymentHold - a model defined in Swagger"""  # noqa: E501
        self._expected_release_date = None
        self._hold_amount = None
        self._hold_reason = None
        self._hold_state = None
        self._release_date = None
        self._seller_actions_to_release = None
        self.discriminator = None
        if expected_release_date is not None:
            self.expected_release_date = expected_release_date
        if hold_amount is not None:
            self.hold_amount = hold_amount
        if hold_reason is not None:
            self.hold_reason = hold_reason
        if hold_state is not None:
            self.hold_state = hold_state
        if release_date is not None:
            self.release_date = release_date
        if seller_actions_to_release is not None:
            self.seller_actions_to_release = seller_actions_to_release

    @property
    def expected_release_date(self):
        """Gets the expected_release_date of this PaymentHold.  # noqa: E501

        The date and time that the payment being held is expected to be released to the seller. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field will be returned if known by eBay. <br /><br /><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br /><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :return: The expected_release_date of this PaymentHold.  # noqa: E501
        :rtype: str
        """
        return self._expected_release_date

    @expected_release_date.setter
    def expected_release_date(self, expected_release_date):
        """Sets the expected_release_date of this PaymentHold.

        The date and time that the payment being held is expected to be released to the seller. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field will be returned if known by eBay. <br /><br /><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br /><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :param expected_release_date: The expected_release_date of this PaymentHold.  # noqa: E501
        :type: str
        """

        self._expected_release_date = expected_release_date

    @property
    def hold_amount(self):
        """Gets the hold_amount of this PaymentHold.  # noqa: E501


        :return: The hold_amount of this PaymentHold.  # noqa: E501
        :rtype: Amount
        """
        return self._hold_amount

    @hold_amount.setter
    def hold_amount(self, hold_amount):
        """Sets the hold_amount of this PaymentHold.


        :param hold_amount: The hold_amount of this PaymentHold.  # noqa: E501
        :type: Amount
        """

        self._hold_amount = hold_amount

    @property
    def hold_reason(self):
        """Gets the hold_reason of this PaymentHold.  # noqa: E501

        The reason that the payment is being held. A seller's payment may be held for a number of reasons, including when the seller is new, the seller's level is below standard, or if a return case or 'Significantly not as described' case is pending against the seller. This field is always returned with the <strong>paymentHolds</strong> array.  # noqa: E501

        :return: The hold_reason of this PaymentHold.  # noqa: E501
        :rtype: str
        """
        return self._hold_reason

    @hold_reason.setter
    def hold_reason(self, hold_reason):
        """Sets the hold_reason of this PaymentHold.

        The reason that the payment is being held. A seller's payment may be held for a number of reasons, including when the seller is new, the seller's level is below standard, or if a return case or 'Significantly not as described' case is pending against the seller. This field is always returned with the <strong>paymentHolds</strong> array.  # noqa: E501

        :param hold_reason: The hold_reason of this PaymentHold.  # noqa: E501
        :type: str
        """

        self._hold_reason = hold_reason

    @property
    def hold_state(self):
        """Gets the hold_state of this PaymentHold.  # noqa: E501

        The current stage or condition of the hold. This field is always returned with the <strong>paymentHolds</strong> array.<br /><br /><b>Applicable values:</b><ul><li><code>HELD</code></li><li><code>HELD_PENDING</code></li><li><code>NOT_HELD</code></li><li><code>RELEASE_CONFIRMED</code></li><li><code>RELEASE_FAILED</code></li><li><code>RELEASE_PENDING</code></li><li><code>RELEASED</code></li></ul>  # noqa: E501

        :return: The hold_state of this PaymentHold.  # noqa: E501
        :rtype: str
        """
        return self._hold_state

    @hold_state.setter
    def hold_state(self, hold_state):
        """Sets the hold_state of this PaymentHold.

        The current stage or condition of the hold. This field is always returned with the <strong>paymentHolds</strong> array.<br /><br /><b>Applicable values:</b><ul><li><code>HELD</code></li><li><code>HELD_PENDING</code></li><li><code>NOT_HELD</code></li><li><code>RELEASE_CONFIRMED</code></li><li><code>RELEASE_FAILED</code></li><li><code>RELEASE_PENDING</code></li><li><code>RELEASED</code></li></ul>  # noqa: E501

        :param hold_state: The hold_state of this PaymentHold.  # noqa: E501
        :type: str
        """

        self._hold_state = hold_state

    @property
    def release_date(self):
        """Gets the release_date of this PaymentHold.  # noqa: E501

        The date and time that the payment being held was actually released to the seller. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is not returned until the seller's payment is actually released into the seller's account.<br /><br /><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br /><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :return: The release_date of this PaymentHold.  # noqa: E501
        :rtype: str
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this PaymentHold.

        The date and time that the payment being held was actually released to the seller. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is not returned until the seller's payment is actually released into the seller's account.<br /><br /><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br /><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :param release_date: The release_date of this PaymentHold.  # noqa: E501
        :type: str
        """

        self._release_date = release_date

    @property
    def seller_actions_to_release(self):
        """Gets the seller_actions_to_release of this PaymentHold.  # noqa: E501

        A list of one or more possible actions that the seller can take to expedite the release of the payment hold.  # noqa: E501

        :return: The seller_actions_to_release of this PaymentHold.  # noqa: E501
        :rtype: list[SellerActionsToRelease]
        """
        return self._seller_actions_to_release

    @seller_actions_to_release.setter
    def seller_actions_to_release(self, seller_actions_to_release):
        """Sets the seller_actions_to_release of this PaymentHold.

        A list of one or more possible actions that the seller can take to expedite the release of the payment hold.  # noqa: E501

        :param seller_actions_to_release: The seller_actions_to_release of this PaymentHold.  # noqa: E501
        :type: list[SellerActionsToRelease]
        """

        self._seller_actions_to_release = seller_actions_to_release

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
        if issubclass(PaymentHold, dict):
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
        if not isinstance(other, PaymentHold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
