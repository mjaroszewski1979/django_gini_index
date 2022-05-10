from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Lower


class User(AbstractUser):
    pass

class Chart(models.Model):
    name = models.CharField(max_length=128, unique=True)
    users = models.ManyToManyField(User, related_name='charts', through='UserCharts')
    photo = models.ImageField(upload_to='film_photos/', blank=True, null=True)

    class Meta:
        ordering = [Lower('name')]

class UserCharts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['order']
