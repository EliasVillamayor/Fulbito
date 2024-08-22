from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import * 
from .serializers import *
# Create your views here.

#
#
#METODOS DE USUARIO
#
#
@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    users_serialized = UserSerializer(users, many=True)
    return Response(users_serialized.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        user_serialized = UserSerializer(user)
        return Response(user_serialized.data)
    

    elif request.method == 'PUT':
        user_serialized = UserSerializer(user, data=request.data)
        if user_serialized.is_valid():
            user_serialized.save()
            return Response(user_serialized.data)
        return Response(user_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

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