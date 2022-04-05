# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities  # noqa: E501

    OpenAPI spec version: 0.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from client.configuration import Configuration


class PredictionJob(object):
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
        'id': 'int',
        'name': 'str',
        'version_id': 'int',
        'model_id': 'int',
        'project_id': 'int',
        'environment_name': 'str',
        'environment': 'Environment',
        'config': 'Config',
        'status': 'str',
        'error': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'version_id': 'version_id',
        'model_id': 'model_id',
        'project_id': 'project_id',
        'environment_name': 'environment_name',
        'environment': 'environment',
        'config': 'config',
        'status': 'status',
        'error': 'error',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, version_id=None, model_id=None, project_id=None, environment_name=None, environment=None, config=None, status=None, error=None, created_at=None, updated_at=None, _configuration=None):  # noqa: E501
        """PredictionJob - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._version_id = None
        self._model_id = None
        self._project_id = None
        self._environment_name = None
        self._environment = None
        self._config = None
        self._status = None
        self._error = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if version_id is not None:
            self.version_id = version_id
        if model_id is not None:
            self.model_id = model_id
        if project_id is not None:
            self.project_id = project_id
        if environment_name is not None:
            self.environment_name = environment_name
        if environment is not None:
            self.environment = environment
        if config is not None:
            self.config = config
        if status is not None:
            self.status = status
        if error is not None:
            self.error = error
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this PredictionJob.  # noqa: E501


        :return: The id of this PredictionJob.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PredictionJob.


        :param id: The id of this PredictionJob.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PredictionJob.  # noqa: E501


        :return: The name of this PredictionJob.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PredictionJob.


        :param name: The name of this PredictionJob.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version_id(self):
        """Gets the version_id of this PredictionJob.  # noqa: E501


        :return: The version_id of this PredictionJob.  # noqa: E501
        :rtype: int
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this PredictionJob.


        :param version_id: The version_id of this PredictionJob.  # noqa: E501
        :type: int
        """

        self._version_id = version_id

    @property
    def model_id(self):
        """Gets the model_id of this PredictionJob.  # noqa: E501


        :return: The model_id of this PredictionJob.  # noqa: E501
        :rtype: int
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this PredictionJob.


        :param model_id: The model_id of this PredictionJob.  # noqa: E501
        :type: int
        """

        self._model_id = model_id

    @property
    def project_id(self):
        """Gets the project_id of this PredictionJob.  # noqa: E501


        :return: The project_id of this PredictionJob.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PredictionJob.


        :param project_id: The project_id of this PredictionJob.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def environment_name(self):
        """Gets the environment_name of this PredictionJob.  # noqa: E501


        :return: The environment_name of this PredictionJob.  # noqa: E501
        :rtype: str
        """
        return self._environment_name

    @environment_name.setter
    def environment_name(self, environment_name):
        """Sets the environment_name of this PredictionJob.


        :param environment_name: The environment_name of this PredictionJob.  # noqa: E501
        :type: str
        """

        self._environment_name = environment_name

    @property
    def environment(self):
        """Gets the environment of this PredictionJob.  # noqa: E501


        :return: The environment of this PredictionJob.  # noqa: E501
        :rtype: Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this PredictionJob.


        :param environment: The environment of this PredictionJob.  # noqa: E501
        :type: Environment
        """

        self._environment = environment

    @property
    def config(self):
        """Gets the config of this PredictionJob.  # noqa: E501


        :return: The config of this PredictionJob.  # noqa: E501
        :rtype: Config
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this PredictionJob.


        :param config: The config of this PredictionJob.  # noqa: E501
        :type: Config
        """

        self._config = config

    @property
    def status(self):
        """Gets the status of this PredictionJob.  # noqa: E501


        :return: The status of this PredictionJob.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PredictionJob.


        :param status: The status of this PredictionJob.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def error(self):
        """Gets the error of this PredictionJob.  # noqa: E501


        :return: The error of this PredictionJob.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this PredictionJob.


        :param error: The error of this PredictionJob.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def created_at(self):
        """Gets the created_at of this PredictionJob.  # noqa: E501


        :return: The created_at of this PredictionJob.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PredictionJob.


        :param created_at: The created_at of this PredictionJob.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PredictionJob.  # noqa: E501


        :return: The updated_at of this PredictionJob.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PredictionJob.


        :param updated_at: The updated_at of this PredictionJob.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(PredictionJob, dict):
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
        if not isinstance(other, PredictionJob):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PredictionJob):
            return True

        return self.to_dict() != other.to_dict()
