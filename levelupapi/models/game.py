from django.db import models


class Game(models.Model):
    
    class Skill(models.IntegerChoices):
        BEGINNER = 1
        EXPERIENCED = 2
        PROFESSIONAL = 3
        EXPERT = 4
    
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey("levelupapi.Gamer", on_delete=models.CASCADE)
    gametype = models.ForeignKey("levelupapi.GameType", on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField(choices=Skill.choices)
    
