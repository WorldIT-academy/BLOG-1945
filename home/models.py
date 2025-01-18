from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    age = models.IntegerField()