from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=264)
    last_name=models.CharField(max_length=264)
    Email=models.EmailField(max_length=264,unique=True)
