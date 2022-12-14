from django.db import models

# Create your models here.

class Iniciar (models.Model):
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=40)
    
