from rest_framework import serializers
from .models import *


class PitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pitch
        fields = ('__all__')

class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = ('__all__')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('__all__')

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ('__all__')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('__all__')

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('__all__')

class FrequentClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentClient
        fields = ('__all__')

    