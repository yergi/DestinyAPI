import requests
import json
import pandas as pd

head = {'X-API-Key':'insert_key_here'}
gameID = ['4892996696']
dfStats = pd.DataFrame(columns=())
keyStats = [{'value': 'weaponKillsSniper',
            'displayValue': 'Sniper Kills'},
            {'value': 'weaponKillsShotgun',
            'displayValue': 'Shotgun Kills'},
            {'value': 'weaponKillsFusionRifle',
            'displayValue': 'Fusion Rifle Kills'}]

for game in gameID:
    response = requests.get('https://www.bungie.net/Platform/Destiny/Stats/PostGameCarnageReport/' + game,
                            headers=head)
    response.raise_for_status()
    body = response.json()
    for item in body['Response']['data']['entries']:
        dfAppend = pd.DataFrame(
            {
                'Player Name': [item['player']['destinyUserInfo']['displayName']],
                'Team Name': [item['values']['team']['basic']['displayValue']]
            })
        dfStats = dfStats.append(dfAppend, ignore_index=True)
    print(dfStats)