import requests
from django.shortcuts import render
from .utils.sport_api import get_league_results

def home(request):
    # Her bir lig için sonuçları çek
    super_lig = get_league_results('super-lig')  # Türkiye Süper Lig
    premier = get_league_results('ingiltere-premier-ligi')   # İngiltere Premier Ligi
    laliga = get_league_results('ispanya-la-ligi')         # İspanya La Liga
    bundesliga = get_league_results('almanya-bundesliga')  # Almanya Bundesliga
    serie_a = get_league_results('italya-serie-a')         # İtalya Serie A
    ligue1 = get_league_results('fransa-ligue-1')          # Fransa Ligue 1

    context = {
        'super_lig_results': super_lig,
        'premier_results': premier,
        'laliga_results': laliga,
        'bundesliga_results': bundesliga,
        'seriea_results': serie_a,
        'ligue1_results': ligue1,
    }
    return render(request, 'home.html', context)