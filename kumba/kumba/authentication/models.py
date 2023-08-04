from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # nom = models.CharField(max_length=100)
    # prenom = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'
    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')