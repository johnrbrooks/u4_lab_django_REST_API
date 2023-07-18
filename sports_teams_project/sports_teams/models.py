from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length = 25)
    city = models.CharField(max_length = 25)
    league = models.CharField(max_length = 3)
    division = models.CharField(max_length = 25)
    wins = models.IntegerField()
    losses = models.IntegerField()

    def __str__(self):
        return self.name
    
class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length = 25)
    position = models.CharField(max_length=25)
    age = models.IntegerField()
    is_injured = models.BooleanField()
    goals = models.IntegerField()

    def __str__(self):
        return self.name