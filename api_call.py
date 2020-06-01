import requests
from io import BytesIO
from flask import Flask

app = Flask(__name__)

# helper function
def _NBA_stats(first_name, last_name):

    player_info = {
        'ID':None,
        'full name' : None,
        'team': None,
        'games played': None,
        'points per game': None,
        'shooting percentage': None,
    }

    r = requests.get(f"https://www.balldontlie.io/api/v1/players?search={first_name}")

    data = r.json()['data']
    for i in range( len(data)):
        if data[i]['last_name'] == last_name:
            player_info['full name'] = (f"{data[i]['first_name']} {data[i]['last_name']}")
            player_info['team'] = data[i]['team']['full_name']
            player_info['ID'] = data[i]['id']

    stats = requests.get(f"https://www.balldontlie.io/api/v1/season_averages?season=2019&player_ids[]={player_info['ID']}")
    statsData = stats.json()['data'][0]

    player_info['games played'] = statsData['games_played']
    player_info['points per game'] = statsData['pts']
    player_info['shooting percentage'] = (f"{float(statsData['fg_pct'] * 100)}%")

    return player_info


# get the stats of NBA players or return the name of the known person
def get_stats(name):

    fullname_split = name.split("-")
    fullname = fullname_split[0].split()

    if len(fullname) == 2:
        first_name = fullname[0]
        last_name = fullname[1]
        return _NBA_stats(first_name, last_name)
    else:
        fullname_split.pop()
        name = fullname_split[0]
        return name