from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.CharField(max_length=16,null=False,unique=True)
    full_name = models.CharField(max_length=32,null=False,unique=True)
    passwd = models.CharField(max_length=16,null=False,unique=True)
