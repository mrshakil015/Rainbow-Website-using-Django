from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    USERTYPE = [
        ('Admin','Admin'),
        ('Student','Student'),
    ]
    UserType = models.CharField(choices=USERTYPE,max_length=100)
    