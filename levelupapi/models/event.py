from django.db import models

class Event(models.Model):

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value

    gamer = models.ForeignKey("levelupapi.Gamer", on_delete=models.CASCADE)
    description = models.CharField(max_length=150, default='Game info here')
    game = models.ForeignKey("levelupapi.Game", on_delete=models.CASCADE)
    date = models.DateTimeField(max_length=10)
    time = models.TimeField(auto_now_add=False)
    attendees = models.ManyToManyField("levelupapi.Gamer", related_name="myevents")
    joined = models.BooleanField()

    # title = models.CharField(max_length=55)
    # game = models.ForeignKey("levelupapi.Game", on_delete=models.CASCADE)
    # gamer = models.ForeignKey("levelupapi.Gamer", on_delete=models.CASCADE)
    # location = models.CharField(max_length=50)
    