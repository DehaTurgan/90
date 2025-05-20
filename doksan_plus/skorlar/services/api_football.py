import requests
from django.conf import settings

BASE_URL = 'https://v3.football.api-sports.io'

def fetch_from_api(endpoint: str, params: dict = None) -> dict:
    """
    API-Football’dan veri çeker.
    endpoint örn: '/players'
    params örn: {'league': 39, 'season': 2024}
    """
    url = BASE_URL + endpoint
    headers = {
        'x-apisports-key': settings.API_FOOTBALL_KEY
    }
    response = requests.get(url, headers=headers, params=params or {})
    response.raise_for_status()  # 4xx/5xx hata gelirse Exception fırlatır
    return response.json()