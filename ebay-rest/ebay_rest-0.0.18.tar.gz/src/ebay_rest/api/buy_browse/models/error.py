# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Error(object):
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
        'category': 'str',
        'domain': 'str',
        'error_id': 'int',
        'input_ref_ids': 'list[str]',
        'long_message': 'str',
        'message': 'str',
        'output_ref_ids': 'list[str]',
        'parameters': 'list[ErrorParameter]',
        'subdomain': 'str'
    }

    attribute_map = {
        'category': 'category',
        'domain': 'domain',
        'error_id': 'errorId',
        'input_ref_ids': 'inputRefIds',
        'long_message': 'longMessage',
        'message': 'message',
        'output_ref_ids': 'outputRefIds',
        'parameters': 'parameters',
        'subdomain': 'subdomain'
    }

    def __init__(self, category=None, domain=None, error_id=None, input_ref_ids=None, long_message=None, message=None, output_ref_ids=None, parameters=None, subdomain=None):  # noqa: E501
        """Error - a model defined in Swagger"""  # noqa: E501
        self._category = None
        self._domain = None
        self._error_id = None
        self._input_ref_ids = None
        self._long_message = None
        self._message = None
        self._output_ref_ids = None
        self._parameters = None
        self._subdomain = None
        self.discriminator = None
        if category is not None:
            self.category = category
        if domain is not None:
            self.domain = domain
        if error_id is not None:
            self.error_id = error_id
        if input_ref_ids is not None:
            self.input_ref_ids = input_ref_ids
        if long_message is not None:
            self.long_message = long_message
        if message is not None:
            self.message = message
        if output_ref_ids is not None:
            self.output_ref_ids = output_ref_ids
        if parameters is not None:
            self.parameters = parameters
        if subdomain is not None:
            self.subdomain = subdomain

    @property
    def category(self):
        """Gets the category of this Error.  # noqa: E501

        This string value indicates the error category. There are three categories of errors: request errors, application errors, and system errors.   # noqa: E501

        :return: The category of this Error.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Error.

        This string value indicates the error category. There are three categories of errors: request errors, application errors, and system errors.   # noqa: E501

        :param category: The category of this Error.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def domain(self):
        """Gets the domain of this Error.  # noqa: E501

        The name of the primary system where the error occurred. This is relevant for application errors.  # noqa: E501

        :return: The domain of this Error.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Error.

        The name of the primary system where the error occurred. This is relevant for application errors.  # noqa: E501

        :param domain: The domain of this Error.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def error_id(self):
        """Gets the error_id of this Error.  # noqa: E501

        A unique code that identifies the particular error or warning that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms.  # noqa: E501

        :return: The error_id of this Error.  # noqa: E501
        :rtype: int
        """
        return self._error_id

    @error_id.setter
    def error_id(self, error_id):
        """Sets the error_id of this Error.

        A unique code that identifies the particular error or warning that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms.  # noqa: E501

        :param error_id: The error_id of this Error.  # noqa: E501
        :type: int
        """

        self._error_id = error_id

    @property
    def input_ref_ids(self):
        """Gets the input_ref_ids of this Error.  # noqa: E501

        An array of reference IDs that identify the specific request elements most closely associated to the error or warning, if any.  # noqa: E501

        :return: The input_ref_ids of this Error.  # noqa: E501
        :rtype: list[str]
        """
        return self._input_ref_ids

    @input_ref_ids.setter
    def input_ref_ids(self, input_ref_ids):
        """Sets the input_ref_ids of this Error.

        An array of reference IDs that identify the specific request elements most closely associated to the error or warning, if any.  # noqa: E501

        :param input_ref_ids: The input_ref_ids of this Error.  # noqa: E501
        :type: list[str]
        """

        self._input_ref_ids = input_ref_ids

    @property
    def long_message(self):
        """Gets the long_message of this Error.  # noqa: E501

        A detailed description of the condition that caused the error or warning, and information on what to do to correct the problem.  # noqa: E501

        :return: The long_message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._long_message

    @long_message.setter
    def long_message(self, long_message):
        """Sets the long_message of this Error.

        A detailed description of the condition that caused the error or warning, and information on what to do to correct the problem.  # noqa: E501

        :param long_message: The long_message of this Error.  # noqa: E501
        :type: str
        """

        self._long_message = long_message

    @property
    def message(self):
        """Gets the message of this Error.  # noqa: E501

        A description of the condition that caused the error or warning.  # noqa: E501

        :return: The message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Error.

        A description of the condition that caused the error or warning.  # noqa: E501

        :param message: The message of this Error.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def output_ref_ids(self):
        """Gets the output_ref_ids of this Error.  # noqa: E501

        An array of reference IDs that identify the specific response elements most closely associated to the error or warning, if any.  # noqa: E501

        :return: The output_ref_ids of this Error.  # noqa: E501
        :rtype: list[str]
        """
        return self._output_ref_ids

    @output_ref_ids.setter
    def output_ref_ids(self, output_ref_ids):
        """Sets the output_ref_ids of this Error.

        An array of reference IDs that identify the specific response elements most closely associated to the error or warning, if any.  # noqa: E501

        :param output_ref_ids: The output_ref_ids of this Error.  # noqa: E501
        :type: list[str]
        """

        self._output_ref_ids = output_ref_ids

    @property
    def parameters(self):
        """Gets the parameters of this Error.  # noqa: E501

        An array of warning and error messages that return one or more variables contextual information about the error or warning. This is often the field or value that triggered the error or warning.  # noqa: E501

        :return: The parameters of this Error.  # noqa: E501
        :rtype: list[ErrorParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Error.

        An array of warning and error messages that return one or more variables contextual information about the error or warning. This is often the field or value that triggered the error or warning.  # noqa: E501

        :param parameters: The parameters of this Error.  # noqa: E501
        :type: list[ErrorParameter]
        """

        self._parameters = parameters

    @property
    def subdomain(self):
        """Gets the subdomain of this Error.  # noqa: E501

        The name of the subdomain in which the error or warning occurred.  # noqa: E501

        :return: The subdomain of this Error.  # noqa: E501
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """Sets the subdomain of this Error.

        The name of the subdomain in which the error or warning occurred.  # noqa: E501

        :param subdomain: The subdomain of this Error.  # noqa: E501
        :type: str
        """

        self._subdomain = subdomain

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
        if issubclass(Error, dict):
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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
