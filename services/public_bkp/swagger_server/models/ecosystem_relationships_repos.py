# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ecosystem_relationships_repos_links import EcosystemRelationshipsReposLinks  # noqa: F401,E501
from swagger_server import util


class EcosystemRelationshipsRepos(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, links: EcosystemRelationshipsReposLinks=None):  # noqa: E501
        """EcosystemRelationshipsRepos - a model defined in Swagger

        :param links: The links of this EcosystemRelationshipsRepos.  # noqa: E501
        :type links: EcosystemRelationshipsReposLinks
        """
        self.swagger_types = {
            'links': EcosystemRelationshipsReposLinks
        }

        self.attribute_map = {
            'links': 'links'
        }
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'EcosystemRelationshipsRepos':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Ecosystem_relationships_repos of this EcosystemRelationshipsRepos.  # noqa: E501
        :rtype: EcosystemRelationshipsRepos
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self) -> EcosystemRelationshipsReposLinks:
        """Gets the links of this EcosystemRelationshipsRepos.


        :return: The links of this EcosystemRelationshipsRepos.
        :rtype: EcosystemRelationshipsReposLinks
        """
        return self._links

    @links.setter
    def links(self, links: EcosystemRelationshipsReposLinks):
        """Sets the links of this EcosystemRelationshipsRepos.


        :param links: The links of this EcosystemRelationshipsRepos.
        :type links: EcosystemRelationshipsReposLinks
        """

        self._links = links