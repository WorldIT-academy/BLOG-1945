from django.db import models
#
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    
    name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"