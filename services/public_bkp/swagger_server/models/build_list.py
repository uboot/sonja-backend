# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.build import Build  # noqa: F401,E501
from swagger_server import util


class BuildList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data: List[Build]=None):  # noqa: E501
        """BuildList - a model defined in Swagger

        :param data: The data of this BuildList.  # noqa: E501
        :type data: List[Build]
        """
        self.swagger_types = {
            'data': List[Build]
        }

        self.attribute_map = {
            'data': 'data'
        }
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'BuildList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BuildList of this BuildList.  # noqa: E501
        :rtype: BuildList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[Build]:
        """Gets the data of this BuildList.


        :return: The data of this BuildList.
        :rtype: List[Build]
        """
        return self._data

    @data.setter
    def data(self, data: List[Build]):
        """Sets the data of this BuildList.


        :param data: The data of this BuildList.
        :type data: List[Build]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data