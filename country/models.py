from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Lower


class User(AbstractUser):
    pass

class Country(models.Model):
    name = models.CharField(max_length=128, unique=True)
    users = models.ManyToManyField(User, related_name='countries', through='UserCountries')

    class Meta:
        ordering = [Lower('name')]

class UserCountries(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['order']
