
class player(object):
    def __init__(self, data):
        self.data = data
        self.name = data['player']['destinyUserInfo']['displayName']

    @classmethod
    def from_player_data(cls, player_data, api_key=None):
        # TODO: return dictionary where keys are player name and values are game objects
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
