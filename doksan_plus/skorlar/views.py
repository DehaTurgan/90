from django.shortcuts import render
import requests
from django.core.cache import cache
from datetime import datetime, timedelta

BASE_URL = 'https://v3.football.api-sports.io'
HEADERS = {
    'x-apisports-key': '1fe6442495bf6a88ab6a95cfcb3cb436',
    'x-apisports-host': 'v3.football.api-sports.io'
}

def fixtures_view(request): 
    season_start = '2022-11-20'
    season_end = '2022-12-18'
    season_year = 2022  

    LEAGUES = {
        'World Cup 2022': 1,
    }

    all_fixtures = []
    for name, league_id in LEAGUES.items():
        cache_key = f'fixtures_{league_id}'
        data = cache.get(cache_key)
        if not data:
            url = (
                f'{BASE_URL}/fixtures'
                f'?league={league_id}'
                f'&season={season_year}'
                f'&from={season_start}'
                f'&to={season_end}'
            )
            response = requests.get(url, headers=HEADERS)
            data = response.json()
            cache.set(cache_key, data, timeout=3600)

        all_fixtures.append({
            'league': name,
            'matches': data.get('response', [])
        })
    return render(request, 'fixtures/home.html', {'all_fixtures': all_fixtures})