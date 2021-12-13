from django.db import models


class Game(models.Model):
    
    gametype = models.ForeignKey("levelupapi.GameType", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
