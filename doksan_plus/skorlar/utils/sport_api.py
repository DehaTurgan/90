import requests
from django.conf import settings

def get_league_results(league_key):
    """
    CollectAPI üzerinden verilen lig için maç sonuçlarını döndürür.
    league_key: örn. 'ingiltere-premier-ligi', 'almanya-bundesliga', 'super-lig' vb.
    """
    url = f"https://api.collectapi.com/football/results?data.league={league_key}"
    headers = {
        "authorization": "apikey 5MZvRFh6w74TClgWPvKr6z:42s39uyQlDYI4oPTWDMuTV",
        "content-type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        # API JSON yanıtında 'result' anahtarında maç listesi var
        return data.get('result', [])
    except requests.RequestException as e:
        # Hata durumunda boş liste döndür veya log kaydı bırak
        print(f"{league_key} sonuçları alınırken hata:", e)
        return []

