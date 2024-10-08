from django.db import models
from .enums import *

# Create your models here.

class Pitch(models.Model):
    name = models.CharField(max_length=100,null=False)
    size = models.CharField(choices=[(ps.value, ps.name) for ps in PitchSize],null=False, max_length=100)
    status = models.CharField(choices=[(ps.value, ps.name) for ps in PitchStatus],null=False, max_length=100)
    
class Payment(models.Model):
    ammount = models.DecimalField(null=False, max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, null=False)
    method = models.CharField(choices=[(pt.value, pt.name) for pt in PaymentType], null=False, max_length=100)
      
class Team(models.Model):
    name = models.CharField(max_length=100,null=False)
    captain = models.CharField(max_length=50)

class Tournament(models.Model):
    name = models.CharField(max_length=100,null=False)
    start_date = models.DateTimeField(null=False, auto_now_add=True)
    finish_date= models.DateField(null=False)
    status = models.CharField(choices=[(ts.value, ts.name) for ts in TournamentStatus],null=False, max_length=100)
    teams = models.ManyToManyField(Team, related_name='tournaments')
   
class Reserve(models.Model):
    client = models.CharField(default='client', null=False, max_length=50)
    reserve_date_time = models.DateTimeField(null=False)
    pitch = models.ForeignKey(Pitch, on_delete=models.CASCADE)
    status = models.CharField(choices=[(rs.value, rs.name) for rs in ReserveStatus], max_length=10, default='Pendiente')

class Match(models.Model):
    date = models.DateField()
    tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches')
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE,null=False, related_name='match_team_one')
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE,null=False,related_name='match_team_two')
    winner = models.ForeignKey(Team, on_delete=models.CASCADE,null=False,related_name='winner')

class FrequentClient(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    phone_number = models.CharField(max_length=20, null=False)






