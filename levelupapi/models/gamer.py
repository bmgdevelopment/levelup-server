from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User


class Gamer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    # join_date = models.DateTimeField(null=True, required=True, unique=False)
    # url_website = models.URLField()
