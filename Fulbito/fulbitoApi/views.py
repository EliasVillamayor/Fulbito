import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import * 
from .serializers import *
# Create your views here.


#
#
#METODOS DE CANCHA
#
#
@api_view(['GET'])
def get_all_pitches(request):
    pitches = Pitch.objects.all()
    pitches_serialized = PitchSerializer(pitches, many=True)
    return Response(pitches_serialized.data)

@api_view(['POST'])
def create_pitch(request):
    serializer = PitchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pitch_detail(request, pk):
    try:
        pitch = Pitch.objects.get(pk=pk)
    except Pitch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        pitch_serialized = PitchSerializer(pitch)
        return Response(pitch_serialized.data)
    

    elif request.method == 'PUT':
        pitch_serialized = PitchSerializer(pitch, data=request.data)
        if pitch_serialized.is_valid():
            pitch_serialized.save()
            return Response(pitch_serialized.data)
        return Response(pitch_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        pitch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#
#
#METODOS DE PAYMENT
#
#
@api_view(['GET'])
def get_all_payments(request):
    payments = Payment.objects.all()
    payments_serialized = PaymentSerializer(payments, many=True)
    return Response(payments_serialized.data)

@api_view(['POST'])
def create_payment(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def payment_detail(request, pk):
    try:
        payment = Payment.objects.get(pk=pk)
    except Payment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        payment_serialized = PaymentSerializer(payment)
        return Response(payment_serialized.data)
    

    elif request.method == 'PUT':
        payment_serialized = PaymentSerializer(payment, data=request.data)
        if payment_serialized.is_valid():
            payment_serialized.save()
            return Response(payment_serialized.data)
        return Response(payment_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#
#
#METODOS DE TOURNAMENT
#
#
@api_view(['GET'])
def get_all_tournaments(request):
    tournaments = Tournament.objects.all()
    tournaments_serialized = TournamentSerializer(tournaments, many=True)
    return Response(tournaments_serialized.data)

@api_view(['POST'])
def create_tournament(request):
    serializer = TournamentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tournament_detail(request, pk):
    try:
        tournament = Tournament.objects.get(pk=pk)
    except Tournament.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        tournament_serialized = TournamentSerializer(tournament)
        return Response(tournament_serialized.data)
    

    elif request.method == 'PUT':
        tournament_serialized = TournamentSerializer(tournament, data=request.data)
        if tournament_serialized.is_valid():
            tournament_serialized.save()
            return Response(tournament_serialized.data)
        return Response(tournament_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        tournament.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#
#
#METODOS DE TEAM
#
#
@api_view(['GET'])
def get_all_teams(request):
    teams = Team.objects.all()
    teams_serialized = TeamSerializer(teams, many=True)
    return Response(teams_serialized.data)

@api_view(['POST'])
def create_team(request):
    serializer = TeamSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, pk):
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        team_serialized = TeamSerializer(team)
        return Response(team_serialized.data)
    

    elif request.method == 'PUT':
        team_serialized = TeamSerializer(team, data=request.data)
        if team_serialized.is_valid():
            team_serialized.save()
            return Response(team_serialized.data)
        return Response(team_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#
#
#METODOS DE RESERVE
#
#
@api_view(['GET'])
def get_all_reserves(request):
    reserves = Reserve.objects.all()
    reserves_serialized = ReserveSerializer(reserves, many=True)
    return Response(reserves_serialized.data)

@api_view(['POST'])
def create_reserve(request):
    serializer = ReserveSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def reserve_detail(request, pk):
    try:
        reserve = Reserve.objects.get(pk=pk)
    except Reserve.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        reserve_serialized = ReserveSerializer(reserve)
        return Response(reserve_serialized.data)
    

    elif request.method == 'PUT':
        reserve_serialized = ReserveSerializer(reserve, data=request.data)
        if reserve_serialized.is_valid():
            reserve_serialized.save()
            return Response(reserve_serialized.data)
        return Response(reserve_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        reserve.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#
#
#METODOS DE MATCH
#
#
@api_view(['GET'])
def get_all_matches(request):
    matches = Match.objects.all()
    matches_serialized = MatchSerializer(matches, many=True)
    return Response(matches_serialized.data)

@api_view(['POST'])
def create_match(request):
    serializer =MatchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def match_detail(request, pk):
    try:
        match = Match.objects.get(pk=pk)
    except Match.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        match_serialized = MatchSerializer(match)
        return Response(match_serialized.data)
    

    elif request.method == 'PUT':
        match_serialized = MatchSerializer(match, data=request.data)
        if match_serialized.is_valid():
            match_serialized.save()
            return Response(match_serialized.data)
        return Response(match_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        match.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


#
#
#METODOS DE Cliente
#
#
@api_view(['GET'])
def get_all_clients(request):
    clients = FrequentClient.objects.all()
    clients_serialized = FrequentClientSerializer(clients, many=True)
    return Response(clients_serialized.data)

@api_view(['POST'])
def create_client(request):
    serializer = FrequentClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    try:
        client = Pitch.objects.get(pk=pk)
    except FrequentClient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        client_serialized = FrequentClientSerializer(client)
        return Response(client_serialized.data)
    

    elif request.method == 'PUT':
        client_serialized = FrequentClientSerializer(client, data=request.data)
        if client_serialized.is_valid():
            client_serialized.save()
            return Response(client_serialized.data)
        return Response(client_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



############################################################

#Metodo de recuperacion de data de mp desde el front
@api_view(['POST'])
def get_mp_data(request):
    ##TAREAS:
    ## 1- Chequear que sea transferencia
    ## 2- Guardar el payment
    ## 3 - Agregar el id del payment correspondiente a la reserva correspondiente


    # Obtener el JSON de la notificación
    notification_data = json.loads(request.body)


    # Verificar si el tipo de evento es "transfer"
    if notification_data['type'] == 'transfer':
        # Procesar la transferencia
        transfer_data = notification_data['data']
        # ... (extraer y procesar los datos de la transferencia)

    return HttpResponse('OK', status=200)