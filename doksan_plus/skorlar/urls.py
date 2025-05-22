from django.urls import path
from . import views

urlpatterns = [
    path('', views.fixtures_view, name='fixtures'),
    path('match/<int:match_id>/', views.match_detail_view, name='match_detail'),
]


# from django.urls import path
# from .views import fixtures_view

# urlpatterns = [
#     path('', fixtures_view, name='home'),  # Bu satır root (ana sayfa) için
#     path('fixtures/', fixtures_view, name='fixtures'),
# ]
