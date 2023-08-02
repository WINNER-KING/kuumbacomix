from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128)