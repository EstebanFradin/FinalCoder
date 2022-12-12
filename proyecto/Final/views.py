from django.http import HttpResponse
from django.template import Template,Context,loader

def Plantilla (request):
    datos = loader.get_template("index.html")
    documento = datos.render()
    return HttpResponse(documento)