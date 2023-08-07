from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # nom = models.CharField(max_length=100)
    # prenom = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    profile_photo = models.ImageField(verbose_name='Photo de profil')
