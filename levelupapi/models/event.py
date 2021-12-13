from django.db import models

class Event(models.Model):

    name = models.CharField(max_length=55)
    gamer = models.ForeignKey("levelupapi.Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("levelupapi.Game", on_delete=models.CASCADE)
    date = models.DateTimeField(max_length=50)
    time = models.TimeField(max_length=50)
    location = models.CharField(max_length=50)
