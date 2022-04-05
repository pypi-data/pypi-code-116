# coding: utf-8

"""
    ARLAS Exploration API

    Explore the content of ARLAS collections  # noqa: E501

    OpenAPI spec version: 21.0.0
    Contact: contact@gisaia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CollectionReferenceDescriptionProperty(object):
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
        'type': 'str',
        'format': 'str',
        'properties': 'dict(str, CollectionReferenceDescriptionProperty)',
        'taggable': 'bool',
        'indexed': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'format': 'format',
        'properties': 'properties',
        'taggable': 'taggable',
        'indexed': 'indexed'
    }

    def __init__(self, type=None, format=None, properties=None, taggable=None, indexed=None):  # noqa: E501
        """CollectionReferenceDescriptionProperty - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._format = None
        self._properties = None
        self._taggable = None
        self._indexed = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if format is not None:
            self.format = format
        if properties is not None:
            self.properties = properties
        if taggable is not None:
            self.taggable = taggable
        if indexed is not None:
            self.indexed = indexed

    @property
    def type(self):
        """Gets the type of this CollectionReferenceDescriptionProperty.  # noqa: E501


        :return: The type of this CollectionReferenceDescriptionProperty.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CollectionReferenceDescriptionProperty.


        :param type: The type of this CollectionReferenceDescriptionProperty.  # noqa: E501
        :type: str
        """
        allowed_values = ["TEXT", "KEYWORD", "LONG", "INTEGER", "SHORT", "BYTE", "DOUBLE", "FLOAT", "DATE", "BOOLEAN", "BINARY", "INT_RANGE", "FLOAT_RANGE", "LONG_RANGE", "DOUBLE_RANGE", "DATE_RANGE", "OBJECT", "NESTED", "GEO_POINT", "GEO_SHAPE", "IP", "COMPLETION", "TOKEN_COUNT", "MAPPER_MURMUR3", "UNKNOWN", "VARCHAR", "CHAR", "CHARACTER", "BIT", "TINYINT", "SMALLINT", "INT", "BIGINT", "DECIMAL", "NUMERIC", "REAL", "DOUBLEPRECISION", "TIMESTAMP", "TIME", "INTERVAL", "GEOMETRY", "GEOGRAPHY", "POINT", "LINESTRING", "POLYGON", "MULTIPOINT", "MULTILINESTRING", "MULTIPOLYGON", "GEOMETRYCOLLECTION"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def format(self):
        """Gets the format of this CollectionReferenceDescriptionProperty.  # noqa: E501


        :return: The format of this CollectionReferenceDescriptionProperty.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this CollectionReferenceDescriptionProperty.


        :param format: The format of this CollectionReferenceDescriptionProperty.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def properties(self):
        """Gets the properties of this CollectionReferenceDescriptionProperty.  # noqa: E501


        :return: The properties of this CollectionReferenceDescriptionProperty.  # noqa: E501
        :rtype: dict(str, CollectionReferenceDescriptionProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CollectionReferenceDescriptionProperty.


        :param properties: The properties of this CollectionReferenceDescriptionProperty.  # noqa: E501
        :type: dict(str, CollectionReferenceDescriptionProperty)
        """

        self._properties = properties

    @property
    def taggable(self):
        """Gets the taggable of this CollectionReferenceDescriptionProperty.  # noqa: E501


        :return: The taggable of this CollectionReferenceDescriptionProperty.  # noqa: E501
        :rtype: bool
        """
        return self._taggable

    @taggable.setter
    def taggable(self, taggable):
        """Sets the taggable of this CollectionReferenceDescriptionProperty.


        :param taggable: The taggable of this CollectionReferenceDescriptionProperty.  # noqa: E501
        :type: bool
        """

        self._taggable = taggable

    @property
    def indexed(self):
        """Gets the indexed of this CollectionReferenceDescriptionProperty.  # noqa: E501


        :return: The indexed of this CollectionReferenceDescriptionProperty.  # noqa: E501
        :rtype: bool
        """
        return self._indexed

    @indexed.setter
    def indexed(self, indexed):
        """Sets the indexed of this CollectionReferenceDescriptionProperty.


        :param indexed: The indexed of this CollectionReferenceDescriptionProperty.  # noqa: E501
        :type: bool
        """

        self._indexed = indexed

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
        if issubclass(CollectionReferenceDescriptionProperty, dict):
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
        if not isinstance(other, CollectionReferenceDescriptionProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
