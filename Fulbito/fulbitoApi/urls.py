from django.urls import path
from .views import *

urlpatterns = [
    path('pitches/', get_all_pitches, name='get_all_pitches'),
    path('pitch/<int:pk>/', pitch_detail, name='pitch_detail'),
    path('pitch/create', create_pitch, name='create_pitch'),

    path('payments/', get_all_payments, name='get_all_payments'),
    path('payment/<int:pk>/', payment_detail, name='payment_detail'),
    path('payment/create', create_payment, name='create_payment'),

    path('tournaments/', get_all_tournaments, name='get_all_tournaments'),
    path('tournament/<int:pk>/', tournament_detail, name='tournament_detail'),
    path('tournament/create', create_tournament, name='create_tournament'),

    path('matches/', get_all_matches, name='get_all_matches'),
    path('match/<int:pk>/', match_detail, name='match_detail'),
    path('match/create', create_match, name='create_match'),

    path('teams/', get_all_teams, name='get_all_teams'),
    path('team/<int:pk>/', team_detail, name='team_detail'),
    path('team/create', create_team, name='create_team'),

    path('reserves/', get_all_reserves, name='get_all_reserves'),
    path('reserve/<int:pk>/', reserve_detail, name='reserve_detail'),
    path('reserve/create', create_reserve, name='create_reserve'),

    path('clients/', get_all_clients, name='get_all_clients'),
    path('client/<int:pk>/', client_detail, name='client_detail'),
    path('client/create', create_client, name='create_client')

    
]

