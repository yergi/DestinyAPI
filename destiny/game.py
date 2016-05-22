
import os
import requests

from .player import player

class game(object):
    def __init__(self, game_id, api_key=None):
        if not api_key:
            api_key = os.environ['BUNGIE_NET_API_KEY']
        self.game_id = str(game_id)
        data = get_json(game_id, api_key)
        self.api_wait = data['ThrottleSeconds']
        # separate player data and game data
        player_data = data['Response']['data'].pop('entries')
        self.data = data['Response']['data']
        # TODO: move this into player class, replace following with
        # self.players = player.from_data(player_data)
        self.players = {}
        for pd in player_data:
            newplayer = player(pd)
            self.players[newplayer.name] = newplayer

    @classmethod
    def from_id_list(cls, game_ids, api_key=None):
        # TODO: return dictionary where keys are game_ids and values are game objects
        return NotImplemented

    @classmethod
    def last_n_from_player(cls, player_id, n=1, api_key=None):
        # TODO: return last n games for player
        return NotImplemented

    # TODO: centralize repeated method
    def get(self, datapath):
        # helper to navigate nested dicts via period-delimited string instead
        path = datapath.split('.')
        # start at top of path
        loc = self.data
        for p in path:
            if p in loc.keys():
                # continue navigating
                loc = loc[p]
            else:
                keys = loc.keys()
                print "Using {path}, couldn't find {p}. Possible values at this level:\n{keys}".format(**locals())
                print loc[p]
        return loc


def get_json(game_id, api_key):
    url = 'https://www.bungie.net/Platform/Destiny/Stats/PostGameCarnageReport/' + str(game_id)
    headers = {'X-API-Key': api_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
