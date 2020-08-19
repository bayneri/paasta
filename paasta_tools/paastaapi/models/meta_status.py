# coding: utf-8

"""
    Paasta API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from paasta_tools.paastaapi.configuration import Configuration


class MetaStatus(object):
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
        'exit_code': 'int',
        'output': 'str'
    }

    attribute_map = {
        'exit_code': 'exit_code',
        'output': 'output'
    }

    def __init__(self, exit_code=None, output=None, local_vars_configuration=None):  # noqa: E501
        """MetaStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._exit_code = None
        self._output = None
        self.discriminator = None

        if exit_code is not None:
            self.exit_code = exit_code
        if output is not None:
            self.output = output

    @property
    def exit_code(self):
        """Gets the exit_code of this MetaStatus.  # noqa: E501

        Exit code from `paasta metastatus` command  # noqa: E501

        :return: The exit_code of this MetaStatus.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this MetaStatus.

        Exit code from `paasta metastatus` command  # noqa: E501

        :param exit_code: The exit_code of this MetaStatus.  # noqa: E501
        :type exit_code: int
        """

        self._exit_code = exit_code

    @property
    def output(self):
        """Gets the output of this MetaStatus.  # noqa: E501

        Output from `paasta metastatus` command  # noqa: E501

        :return: The output of this MetaStatus.  # noqa: E501
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this MetaStatus.

        Output from `paasta metastatus` command  # noqa: E501

        :param output: The output of this MetaStatus.  # noqa: E501
        :type output: str
        """

        self._output = output

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetaStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetaStatus):
            return True

        return self.to_dict() != other.to_dict()