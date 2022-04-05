# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br/><br/>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentsProgramOnboardingSteps(object):
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
        'name': 'str',
        'status': 'str',
        'web_url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'web_url': 'webUrl'
    }

    def __init__(self, name=None, status=None, web_url=None):  # noqa: E501
        """PaymentsProgramOnboardingSteps - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._status = None
        self._web_url = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if web_url is not None:
            self.web_url = web_url

    @property
    def name(self):
        """Gets the name of this PaymentsProgramOnboardingSteps.  # noqa: E501

        The name of the step in the steps array. Over time, these names are subject to change as processes change. The output sample contains example step names. Review an actual call response for updated step names.   # noqa: E501

        :return: The name of this PaymentsProgramOnboardingSteps.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentsProgramOnboardingSteps.

        The name of the step in the steps array. Over time, these names are subject to change as processes change. The output sample contains example step names. Review an actual call response for updated step names.   # noqa: E501

        :param name: The name of this PaymentsProgramOnboardingSteps.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this PaymentsProgramOnboardingSteps.  # noqa: E501

        This enumeration value indicates the status of the associated step. <p> <span class=\"tablenote\"><strong>Note:</strong> Only one step can be <code>IN_PROGRESS</code> at a time.</span></p> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:PaymentsProgramOnboardingStepStatus'>eBay API documentation</a>  # noqa: E501

        :return: The status of this PaymentsProgramOnboardingSteps.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentsProgramOnboardingSteps.

        This enumeration value indicates the status of the associated step. <p> <span class=\"tablenote\"><strong>Note:</strong> Only one step can be <code>IN_PROGRESS</code> at a time.</span></p> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:PaymentsProgramOnboardingStepStatus'>eBay API documentation</a>  # noqa: E501

        :param status: The status of this PaymentsProgramOnboardingSteps.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def web_url(self):
        """Gets the web_url of this PaymentsProgramOnboardingSteps.  # noqa: E501

        This URL provides access to the <code>IN_PROGRESS</code> step.  # noqa: E501

        :return: The web_url of this PaymentsProgramOnboardingSteps.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this PaymentsProgramOnboardingSteps.

        This URL provides access to the <code>IN_PROGRESS</code> step.  # noqa: E501

        :param web_url: The web_url of this PaymentsProgramOnboardingSteps.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

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
        if issubclass(PaymentsProgramOnboardingSteps, dict):
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
        if not isinstance(other, PaymentsProgramOnboardingSteps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
