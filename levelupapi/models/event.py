from django.db import models
from levelupapi.models import Gamer, Game

class Event(models.Model):

    name = models.CharField(max_length=55)
    gamerId = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    date = models.DateTimeField(max_length=50)
    time = models.TimeField(max_length=50)
    location = models.CharField(max_length=50)
