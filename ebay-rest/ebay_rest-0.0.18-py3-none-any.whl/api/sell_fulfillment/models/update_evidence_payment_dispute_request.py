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

class UpdateEvidencePaymentDisputeRequest(object):
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
        'evidence_id': 'str',
        'evidence_type': 'str',
        'files': 'list[FileEvidence]',
        'line_items': 'list[OrderLineItems]'
    }

    attribute_map = {
        'evidence_id': 'evidenceId',
        'evidence_type': 'evidenceType',
        'files': 'files',
        'line_items': 'lineItems'
    }

    def __init__(self, evidence_id=None, evidence_type=None, files=None, line_items=None):  # noqa: E501
        """UpdateEvidencePaymentDisputeRequest - a model defined in Swagger"""  # noqa: E501
        self._evidence_id = None
        self._evidence_type = None
        self._files = None
        self._line_items = None
        self.discriminator = None
        if evidence_id is not None:
            self.evidence_id = evidence_id
        if evidence_type is not None:
            self.evidence_type = evidence_type
        if files is not None:
            self.files = files
        if line_items is not None:
            self.line_items = line_items

    @property
    def evidence_id(self):
        """Gets the evidence_id of this UpdateEvidencePaymentDisputeRequest.  # noqa: E501

        The unique identifier of the evidence set that is being updated with new evidence files.  # noqa: E501

        :return: The evidence_id of this UpdateEvidencePaymentDisputeRequest.  # noqa: E501
        :rtype: str
        """
        return self._evidence_id

    @evidence_id.setter
    def evidence_id(self, evidence_id):
        """Sets the evidence_id of this UpdateEvidencePaymentDisputeRequest.

        The unique identifier of the evidence set that is being updated with new evidence files.  # noqa: E501

        :param evidence_id: The evidence_id of this UpdateEvidencePaymentDisputeRequest.  # noqa: E501
        :type: str
        """

        self._evidence_id = evidence_id

    @property
    def evidence_type(self):
        """Gets the evidence_type of this UpdateEvidencePaymentDisputeRequest.  # noqa: E501

        This field is used to indicate the type of evidence being provided through one or more evidence files. All evidence files (if more than one) should be associated with the evidence type passed in this field. See the <strong>EvidenceTypeEnum</strong> type for the supported evidence types. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:EvidenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The evidence_type of this UpdateEvidencePaymentDisputeRequest.  # noqa: E501
        :rtype: str
        """
        return self._evidence_type

    @evidence_type.setter
    def evidence_type(self, evidence_type):
        """Sets the evidence_type of this UpdateEvidencePaymentDisputeRequest.

        This field is used to indicate the type of evidence being provided through one or more evidence files. All evidence files (if more than one) should be associated with the evidence type passed in this field. See the <strong>EvidenceTypeEnum</strong> type for the supported evidence types. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:EvidenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param evidence_type: The evidence_type of this UpdateEvidencePaymentDisputeRequest.  # noqa: E501
        :type: str
        """

        self._evidence_type = evidence_type

    @property
    def files(self):
        """Gets the files of this UpdateEvidencePaymentDisputeRequest.  # noqa: E501

        This array is used to specify one or more evidence files that will be added to the evidence set associated with a payment dispute. At least one evidence file must be specified in the <strong>files</strong> array.<br><br> The unique identifier of an evidence file is returned in the response payload of the <strong>uploadEvidence</strong> method.  # noqa: E501

        :return: The files of this UpdateEvidencePaymentDisputeRequest.  # noqa: E501
        :rtype: list[FileEvidence]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this UpdateEvidencePaymentDisputeRequest.

        This array is used to specify one or more evidence files that will be added to the evidence set associated with a payment dispute. At least one evidence file must be specified in the <strong>files</strong> array.<br><br> The unique identifier of an evidence file is returned in the response payload of the <strong>uploadEvidence</strong> method.  # noqa: E501

        :param files: The files of this UpdateEvidencePaymentDisputeRequest.  # noqa: E501
        :type: list[FileEvidence]
        """

        self._files = files

    @property
    def line_items(self):
        """Gets the line_items of this UpdateEvidencePaymentDisputeRequest.  # noqa: E501

        This required array identifies the order line item(s) for which the evidence file(s) will be applicable. Both the <strong>itemId</strong> and <strong>lineItemID</strong> fields are needed to identify each order line item, and both of these values are returned under the <strong>evidenceRequests.lineItems</strong> array in the <strong>getPaymentDispute</strong> response.  # noqa: E501

        :return: The line_items of this UpdateEvidencePaymentDisputeRequest.  # noqa: E501
        :rtype: list[OrderLineItems]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this UpdateEvidencePaymentDisputeRequest.

        This required array identifies the order line item(s) for which the evidence file(s) will be applicable. Both the <strong>itemId</strong> and <strong>lineItemID</strong> fields are needed to identify each order line item, and both of these values are returned under the <strong>evidenceRequests.lineItems</strong> array in the <strong>getPaymentDispute</strong> response.  # noqa: E501

        :param line_items: The line_items of this UpdateEvidencePaymentDisputeRequest.  # noqa: E501
        :type: list[OrderLineItems]
        """

        self._line_items = line_items

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
        if issubclass(UpdateEvidencePaymentDisputeRequest, dict):
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
        if not isinstance(other, UpdateEvidencePaymentDisputeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
