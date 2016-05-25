# -*- coding: utf-8 -*-

"""
destiny.Player
~~~~~~~~~~~~~~~~

This module provides access to the `SearchDestinyPlayer` endpoint of the
Destiny API.

"""

import os
from . import utils


class Player(object):
    """
    Return JSON object from `SearchDestinyPlayer` endpoint.
    :param membership_type: 'xbox' or 'psn'; needed to accurately locate player
    :param display_name: Screen name of the player
    """
    def __init__(self, membership_type, display_name, api_key=None):
        if not api_key:
            api_key = os.environ['BUNGIE_NET_API_KEY']
        if membership_type == 'xbox':
            self.membership_type = 'TigerXbox'
        elif membership_type == 'psn':
            self.membership_type = 'TigerPsn'
        self.display_name = str(display_name)
        path = 'SearchDestinyPlayer/{0}/{1}'.format(
            self.membership_type, self.display_name
        )
        data = utils.get_json(path, api_key)
        self.data = data['Response'][0]
        self.api_wait = data['ThrottleSeconds']
        self.player_id = data['Response'][0]['membershipId']

    def get(self, data_path):
        """
        Get the value from a dict entry by specifying a period-delimited string
        :param data_path: period-delimited string defining path to wanted value
        :return: value of specified key from SearchDestinyPlayer JSON object
        """
        return utils.crawl_data(self, data_path)
