
from .utils import crawl_data
# from .constants import KEY_STATS

class Player(object):
    def __init__(self, data):
        self.type = 'player'
        self.data = data
        self.name = data['player']['destinyUserInfo']['displayName']

    @classmethod
    def players_from_data(cls, player_data, api_key=None):
        players = {}
        for pd in player_data:
            newplayer = Player(pd)
            players[newplayer.name] = newplayer
        return players

    def get(self, datapath):
        return crawl_data(self, datapath)
