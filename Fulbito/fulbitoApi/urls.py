from django.urls import path
from .views import *

urlpatterns = [
    path('users/', get_all_users, name='get_all_users'),
    path('user/<int:pk>/', user_detail, name='user_detail'),
    path('user/create', create_user, name='create_user'),

    path('pitches/', get_all_pitches, name='get_all_pitches'),
    path('pitch/<int:pk>/', pitch_detail, name='pitch_detail'),
    path('pitch/create', create_pitch, name='create_pitch'),

    
]

