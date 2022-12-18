from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class Iniciar (models.Model):
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=40)

    
class Usuario(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    balance = models.IntegerField(default=10000)
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    cantidad_apostar = models.IntegerField(default=200)
    def __str__(self) -> None:
        return str(self.usuario)
        
@receiver(post_save,sender=User)
def concetarUsuarios(sender, instance,created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)

class Avatar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    mail = models.EmailField()
    cel = models.IntegerField()
    msj = models.CharField(max_length=150)
