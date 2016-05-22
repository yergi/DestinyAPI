
import os
import requests

from .utils import get_json
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
        self.players = player.players_from_data(player_data)

    @classmethod
    def games_from_ids(cls, game_ids, api_key=None):
        games = {}
        for game_id in game_ids:
            games[game_id] = game(game_id, api_key)
            if games[game_id].api_wait > 0:
                print "Pausing for {wait} seconds for rate limiting".format(**locals())
                time.sleep(games[game_id].api_wait + 1)
        return games

    @classmethod
    def games_from_player(cls, player_id, n=1, api_key=None):
        # TODO: return last n games for player
        return NotImplemented

    def get(self, datapath):
        return crawl_data(self, datapath)
