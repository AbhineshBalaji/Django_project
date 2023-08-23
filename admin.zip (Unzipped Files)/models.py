from django.db import models
class signup(models.Model):
    username = models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)

# Create your models here.
