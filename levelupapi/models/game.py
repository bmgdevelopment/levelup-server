from django.db import models


class Game(models.Model):

    type = models.OneToOneField(max_length=55)
    name = models.CharField(max_length=50)
