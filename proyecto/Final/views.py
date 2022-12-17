from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render
from Moneda.models import Avatar

def Inicio (request):
   if request.user.is_authenticated:
      imagen_model = Avatar.objects.filter(user = request.user.id).order_by("-id")[0]
      imagen_url = imagen_model.imagen.url
   else:
         imagen_url = ""

   return render(request,"index.html", {"imagen_url": imagen_url})


   