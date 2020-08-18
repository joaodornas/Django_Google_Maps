from django.db import models

# Create your models here.

class Customers(models.Model):
    id = models.IntegerField(default=0,primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
