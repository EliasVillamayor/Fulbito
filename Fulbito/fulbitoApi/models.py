from django.db import models
from .enums import *

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    phone_number = models.IntegerField(null=False)
    email = models.EmailField(max_length=100,null=False)
    user_type = models.CharField(choices=[(ut.value, ut.name) for ut in UserType],null=False,max_length=100)
    preferences = models.CharField(max_length=150)
    password = models.CharField(max_length=100,null=False)
    register_date = models.DateTimeField(auto_now_add=True)
    #Reserva se accede con User.reserves.all() 
    #Pago se accede con User.payments.all()
    #Canchas se accede con User.pitches.all
    #Torneo se accede con User.tournaments.all()
    #Equipo se accede con User.teams.all()

class Pitch(models.Model):
    name = models.CharField(max_length=100,null=False)
    size = models.CharField(choices=[(ps.value, ps.name) for ps in PitchSize],null=False, max_length=100)
    status = models.CharField(choices=[(ps.value, ps.name) for ps in PitchStatus],null=False, max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pitches')

class Payment(models.Model):
    ammount = models.DecimalField(null=False, max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, null=False)
    method = models.CharField(choices=[(pt.value, pt.name) for pt in PaymentType], null=False, max_length=100)
    ##Reserva = id de la reserva, se agrega automaticamente por el onetoonefield
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')

class Tournament(models.Model):
    name = models.CharField(max_length=100,null=False)
    start_date = models.DateTimeField(null=False, auto_now_add=True)
    finish_date= models.DateField(null=False)
    status = models.CharField(choices=[(ts.value, ts.name) for ts in TournamentStatus],null=False, max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tournaments')

class Team(models.Model):
    name = models.CharField(max_length=100,null=False)
    captain = models.CharField(max_length=50)
    tournament_id = models.ForeignKey(Tournament,null=False, on_delete=models.CASCADE, related_name='teams')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams')

class Reserve(models.Model):
    reserve_date_time = models.DateTimeField(null=False)
    status = models.CharField(choices=[(rs.value, rs.name) for rs in ReserveStatus],null=False,max_length=100)
    pitch = models.ForeignKey(Pitch, on_delete=models.CASCADE,null=False)
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='reserve_team_one')
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='reserve_team_two')
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, related_name='payment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reserves')


class Match(models.Model):
    date = models.DateField()
    tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches')
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE,null=False, related_name='match_team_one')
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE,null=False,related_name='match_team_two')
    winner = models.ForeignKey(Team, on_delete=models.CASCADE,null=False,related_name='winner')






