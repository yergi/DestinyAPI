
import time
import pandas as pd

import destiny

game_ids = ['4892996696']
games = {}
dfStats = pd.DataFrame(columns=())

# either pass in API key here or set as an environment variable
# by either pasting following line into terminal or adding to ~/.profile
# export BUNGIE_NET_API_KEY='key'
api_key = None

# going to add game class method to hide this loop and the rate limiting unpleasantness
for game_id in game_ids:
    games[game_id] = destiny.game(game_id, api_key)
    if games[game_id].api_wait > 0:
        print "Pausing for {wait} seconds for rate limiting".format(**locals())
        time.sleep(games[game_id].api_wait + 1)

for game_id in game_ids:
    players = games[game_id].players
    for player in players.values():
        dfAppend = pd.DataFrame(
            {
                'Player Name': [player.get('player.destinyUserInfo.displayName')],
                'Team Name': [player.get('values.team.basic.displayValue')]
            })
        dfStats = dfStats.append(dfAppend, ignore_index=True)

print dfStats
