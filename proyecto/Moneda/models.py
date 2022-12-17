from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Iniciar (models.Model):
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=40)
    
class Jugador(models.Model):
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=40)
    balance = models.IntegerField()

class Avatar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
