import requests
from io import BytesIO


results_obj = {}

player_info = {
    'ID':None,
    'full name' : None,
    'team': None,
    'games played': None,
    'points per game': None,
    'shooting percentage': None,
}

def get_API_info(name):
    results_obj[name] = player_info

    split_name = name.split()
    first_name = split_name[0]
    last_name = split_name[1]

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

    return results_obj[name]


# print(get_API_info("Stephen Curry"))