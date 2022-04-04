# coding: utf-8

"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from rockset.configuration import Configuration


class RedshiftIntegration(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'aws_access_key': 'AwsAccessKey',
        'host': 'str',
        'password': 'str',
        'port': 'int',
        's3_bucket_path': 'str',
        'username': 'str'
    }

    attribute_map = {
        'aws_access_key': 'aws_access_key',
        'host': 'host',
        'password': 'password',
        'port': 'port',
        's3_bucket_path': 's3_bucket_path',
        'username': 'username'
    }

    def __init__(self, aws_access_key=None, host=None, password=None, port=None, s3_bucket_path=None, username=None, local_vars_configuration=None):  # noqa: E501
        """RedshiftIntegration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._aws_access_key = None
        self._host = None
        self._password = None
        self._port = None
        self._s3_bucket_path = None
        self._username = None
        self.discriminator = None

        if aws_access_key is not None:
            self.aws_access_key = aws_access_key
        self.host = host
        self.password = password
        self.port = port
        self.s3_bucket_path = s3_bucket_path
        self.username = username

    @property
    def aws_access_key(self):
        """Gets the aws_access_key of this RedshiftIntegration.  # noqa: E501


        :return: The aws_access_key of this RedshiftIntegration.  # noqa: E501
        :rtype: AwsAccessKey
        """
        return self._aws_access_key

    @aws_access_key.setter
    def aws_access_key(self, aws_access_key):
        """Sets the aws_access_key of this RedshiftIntegration.


        :param aws_access_key: The aws_access_key of this RedshiftIntegration.  # noqa: E501
        :type aws_access_key: AwsAccessKey
        """

        self._aws_access_key = aws_access_key

    @property
    def host(self):
        """Gets the host of this RedshiftIntegration.  # noqa: E501

        Redshift Cluster host  # noqa: E501

        :return: The host of this RedshiftIntegration.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this RedshiftIntegration.

        Redshift Cluster host  # noqa: E501

        :param host: The host of this RedshiftIntegration.  # noqa: E501
        :type host: str
        """
        if self.local_vars_configuration.client_side_validation and host is None:  # noqa: E501
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def password(self):
        """Gets the password of this RedshiftIntegration.  # noqa: E501

        Password associated with Redshift cluster  # noqa: E501

        :return: The password of this RedshiftIntegration.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RedshiftIntegration.

        Password associated with Redshift cluster  # noqa: E501

        :param password: The password of this RedshiftIntegration.  # noqa: E501
        :type password: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def port(self):
        """Gets the port of this RedshiftIntegration.  # noqa: E501

        Redshift Cluster port  # noqa: E501

        :return: The port of this RedshiftIntegration.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this RedshiftIntegration.

        Redshift Cluster port  # noqa: E501

        :param port: The port of this RedshiftIntegration.  # noqa: E501
        :type port: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def s3_bucket_path(self):
        """Gets the s3_bucket_path of this RedshiftIntegration.  # noqa: E501

        unload S3 bucket path  # noqa: E501

        :return: The s3_bucket_path of this RedshiftIntegration.  # noqa: E501
        :rtype: str
        """
        return self._s3_bucket_path

    @s3_bucket_path.setter
    def s3_bucket_path(self, s3_bucket_path):
        """Sets the s3_bucket_path of this RedshiftIntegration.

        unload S3 bucket path  # noqa: E501

        :param s3_bucket_path: The s3_bucket_path of this RedshiftIntegration.  # noqa: E501
        :type s3_bucket_path: str
        """
        if self.local_vars_configuration.client_side_validation and s3_bucket_path is None:  # noqa: E501
            raise ValueError("Invalid value for `s3_bucket_path`, must not be `None`")  # noqa: E501

        self._s3_bucket_path = s3_bucket_path

    @property
    def username(self):
        """Gets the username of this RedshiftIntegration.  # noqa: E501

        Username associated with Redshift cluster  # noqa: E501

        :return: The username of this RedshiftIntegration.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RedshiftIntegration.

        Username associated with Redshift cluster  # noqa: E501

        :param username: The username of this RedshiftIntegration.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RedshiftIntegration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RedshiftIntegration):
            return True

        return self.to_dict() != other.to_dict()
