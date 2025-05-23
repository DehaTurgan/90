from django.shortcuts import render, get_object_or_404
import requests
from django.core.cache import cache
from datetime import datetime, timedelta

BASE_URL = 'https://v3.football.api-sports.io'
HEADERS = {
    'x-apisports-key': '1fe6442495bf6a88ab6a95cfcb3cb436',
    'x-apisports-host': 'v3.football.api-sports.io'
}

def fixtures_view(request): 
    season_start = '2023-03-23'
    season_end = '2024-08-12'
    season_year = 2023  

    LEAGUES = {
        'Euro Championship - Qualification' : 960,
        'World Cup - Qualification Africa' : 29,
        'Asian Cup': 7,
        'Netherlands - Super Cup' : 543,
        'Arab Club Champions Cup' : 768,
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

def match_detail_view(request, match_id):
    # Try to get match data from cache
    cache_key = f'match_{match_id}'
    match_data = cache.get(cache_key)
    
    if not match_data:
        # Fetch match details
        url = f'{BASE_URL}/fixtures?id={match_id}'
        response = requests.get(url, headers=HEADERS)
        match_data = response.json().get('response', [])[0]
        
        # Fetch match statistics
        stats_url = f'{BASE_URL}/fixtures/statistics?fixture={match_id}'
        stats_response = requests.get(stats_url, headers=HEADERS)
        stats_data = stats_response.json().get('response', [])
        
        if stats_data:
            # Process statistics
            home_stats = stats_data[0].get('statistics', [])
            away_stats = stats_data[1].get('statistics', [])
            
            # Combine statistics
            combined_stats = []
            for home_stat in home_stats:
                stat_name = home_stat.get('type')
                home_value = home_stat.get('value')
                away_value = next((stat.get('value') for stat in away_stats if stat.get('type') == stat_name), '-')
                
                # Convert percentage strings to numbers for possession
                if stat_name == 'Ball Possession':
                    home_value = int(home_value.strip('%'))
                    away_value = int(away_value.strip('%'))
                # Convert other string values to numbers
                elif isinstance(home_value, str) and home_value.isdigit():
                    home_value = int(home_value)
                if isinstance(away_value, str) and away_value.isdigit():
                    away_value = int(away_value)
                
                combined_stats.append({
                    'name': stat_name,
                    'home': home_value,
                    'away': away_value
                })
            
            match_data['statistics'] = combined_stats
        
        # Fetch and process events
        events_url = f'{BASE_URL}/fixtures/events?fixture={match_id}'
        events_response = requests.get(events_url, headers=HEADERS)
        events_data = events_response.json().get('response', [])
        
        if events_data:
            formatted_events = []
            for event in events_data:
                time = event.get('time', {}).get('elapsed', '')
                event_type = event.get('type', '')
                detail = event.get('detail', '')
                team = event.get('team', {}).get('name', '')
                player = event.get('player', {}).get('name', '')
                
                # Format the event description
                if event_type == 'Goal':
                    event_desc = f"{player} ({team})"
                elif event_type == 'Card':
                    event_desc = f"{player} ({team}) - {detail}"
                elif event_type == 'Subst':
                    event_desc = f"{player} ({team})"
                else:
                    event_desc = f"{player} ({team}) - {detail}"
                
                formatted_events.append({
                    'time': time,
                    'type': event_type,
                    'description': event_desc
                })
            
            match_data['events'] = formatted_events
        
        # Cache the match data
        cache.set(cache_key, match_data, timeout=3600)
    
    return render(request, 'fixtures/match_detail.html', {'match': match_data})