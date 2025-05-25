from django.urls import path
from . import views

urlpatterns = [
    path('', views.fixtures_view, name='home'),
    path('fixtures/', views.fixtures_view, name='fixtures'),
    path('match/<int:match_id>/', views.match_detail_view, name='match_detail'),
]
