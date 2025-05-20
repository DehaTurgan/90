from django.urls import path
from .views import fixtures_view

urlpatterns = [
    path('', fixtures_view, name='home'),  # Bu satır root (ana sayfa) için
    path('fixtures/', fixtures_view, name='fixtures'),
]
