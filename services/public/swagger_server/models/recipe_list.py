# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.recipe import Recipe  # noqa: F401,E501
from swagger_server import util


class RecipeList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data: List[Recipe]=None):  # noqa: E501
        """RecipeList - a model defined in Swagger

        :param data: The data of this RecipeList.  # noqa: E501
        :type data: List[Recipe]
        """
        self.swagger_types = {
            'data': List[Recipe]
        }

        self.attribute_map = {
            'data': 'data'
        }
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'RecipeList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RecipeList of this RecipeList.  # noqa: E501
        :rtype: RecipeList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[Recipe]:
        """Gets the data of this RecipeList.


        :return: The data of this RecipeList.
        :rtype: List[Recipe]
        """
        return self._data

    @data.setter
    def data(self, data: List[Recipe]):
        """Sets the data of this RecipeList.


        :param data: The data of this RecipeList.
        :type data: List[Recipe]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data
