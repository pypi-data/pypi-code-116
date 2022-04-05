# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, see <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\">Promoted Listings</a>.</li>  <li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReportMetadata(object):
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
        'dimension_metadata': 'list[DimensionMetadata]',
        'max_number_of_dimensions_to_request': 'int',
        'max_number_of_metrics_to_request': 'int',
        'metric_metadata': 'list[MetricMetadata]',
        'report_type': 'str'
    }

    attribute_map = {
        'dimension_metadata': 'dimensionMetadata',
        'max_number_of_dimensions_to_request': 'maxNumberOfDimensionsToRequest',
        'max_number_of_metrics_to_request': 'maxNumberOfMetricsToRequest',
        'metric_metadata': 'metricMetadata',
        'report_type': 'reportType'
    }

    def __init__(self, dimension_metadata=None, max_number_of_dimensions_to_request=None, max_number_of_metrics_to_request=None, metric_metadata=None, report_type=None):  # noqa: E501
        """ReportMetadata - a model defined in Swagger"""  # noqa: E501
        self._dimension_metadata = None
        self._max_number_of_dimensions_to_request = None
        self._max_number_of_metrics_to_request = None
        self._metric_metadata = None
        self._report_type = None
        self.discriminator = None
        if dimension_metadata is not None:
            self.dimension_metadata = dimension_metadata
        if max_number_of_dimensions_to_request is not None:
            self.max_number_of_dimensions_to_request = max_number_of_dimensions_to_request
        if max_number_of_metrics_to_request is not None:
            self.max_number_of_metrics_to_request = max_number_of_metrics_to_request
        if metric_metadata is not None:
            self.metric_metadata = metric_metadata
        if report_type is not None:
            self.report_type = report_type

    @property
    def dimension_metadata(self):
        """Gets the dimension_metadata of this ReportMetadata.  # noqa: E501

        A list containing the metadata for the dimension used in the report.  # noqa: E501

        :return: The dimension_metadata of this ReportMetadata.  # noqa: E501
        :rtype: list[DimensionMetadata]
        """
        return self._dimension_metadata

    @dimension_metadata.setter
    def dimension_metadata(self, dimension_metadata):
        """Sets the dimension_metadata of this ReportMetadata.

        A list containing the metadata for the dimension used in the report.  # noqa: E501

        :param dimension_metadata: The dimension_metadata of this ReportMetadata.  # noqa: E501
        :type: list[DimensionMetadata]
        """

        self._dimension_metadata = dimension_metadata

    @property
    def max_number_of_dimensions_to_request(self):
        """Gets the max_number_of_dimensions_to_request of this ReportMetadata.  # noqa: E501

        The maximum number of dimensions that can be requested for the specified report type.  # noqa: E501

        :return: The max_number_of_dimensions_to_request of this ReportMetadata.  # noqa: E501
        :rtype: int
        """
        return self._max_number_of_dimensions_to_request

    @max_number_of_dimensions_to_request.setter
    def max_number_of_dimensions_to_request(self, max_number_of_dimensions_to_request):
        """Sets the max_number_of_dimensions_to_request of this ReportMetadata.

        The maximum number of dimensions that can be requested for the specified report type.  # noqa: E501

        :param max_number_of_dimensions_to_request: The max_number_of_dimensions_to_request of this ReportMetadata.  # noqa: E501
        :type: int
        """

        self._max_number_of_dimensions_to_request = max_number_of_dimensions_to_request

    @property
    def max_number_of_metrics_to_request(self):
        """Gets the max_number_of_metrics_to_request of this ReportMetadata.  # noqa: E501

        The maximum number of metrics that can be requested for the specified report type.  # noqa: E501

        :return: The max_number_of_metrics_to_request of this ReportMetadata.  # noqa: E501
        :rtype: int
        """
        return self._max_number_of_metrics_to_request

    @max_number_of_metrics_to_request.setter
    def max_number_of_metrics_to_request(self, max_number_of_metrics_to_request):
        """Sets the max_number_of_metrics_to_request of this ReportMetadata.

        The maximum number of metrics that can be requested for the specified report type.  # noqa: E501

        :param max_number_of_metrics_to_request: The max_number_of_metrics_to_request of this ReportMetadata.  # noqa: E501
        :type: int
        """

        self._max_number_of_metrics_to_request = max_number_of_metrics_to_request

    @property
    def metric_metadata(self):
        """Gets the metric_metadata of this ReportMetadata.  # noqa: E501

        A list containing the metadata for the metrics in the report.  # noqa: E501

        :return: The metric_metadata of this ReportMetadata.  # noqa: E501
        :rtype: list[MetricMetadata]
        """
        return self._metric_metadata

    @metric_metadata.setter
    def metric_metadata(self, metric_metadata):
        """Sets the metric_metadata of this ReportMetadata.

        A list containing the metadata for the metrics in the report.  # noqa: E501

        :param metric_metadata: The metric_metadata of this ReportMetadata.  # noqa: E501
        :type: list[MetricMetadata]
        """

        self._metric_metadata = metric_metadata

    @property
    def report_type(self):
        """Gets the report_type of this ReportMetadata.  # noqa: E501

        The <b>report_type</b>, as specified in the request to create the report task. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/plr:ReportTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The report_type of this ReportMetadata.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this ReportMetadata.

        The <b>report_type</b>, as specified in the request to create the report task. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/plr:ReportTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param report_type: The report_type of this ReportMetadata.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

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
        if issubclass(ReportMetadata, dict):
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
        if not isinstance(other, ReportMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
