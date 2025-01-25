from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    age = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} {self.last_name}"
    
class Post(models.Model):
    title = models.CharField(max_length= 255)
    content =  models.TextField()
    is_published = models.BooleanField(default= True)
    
    author = models.ForeignKey(to = Author, on_delete= models.CASCADE, null= True)
    
    
