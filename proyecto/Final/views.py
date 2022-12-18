from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render
from Moneda.models import Avatar,Usuario

def Inicio (request):
   if not request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
   else:
        imagen_url = ""

   if request.method == "GET" and request.GET.get('CantidadA') != None:
      user = Usuario.objects.get(usuario=request.user)
      user.cantidad_apostar = request.GET.get('CantidadA')
      user.save()
   

   return render(request, "index.html", {"imagen_url": imagen_url})


   