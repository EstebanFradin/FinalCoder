from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def blackjack (request):
    return render(request,"Moneda/blackjack.html")

def slots (request):
    return render(request,"Moneda/slots.html")

def caracruz (request):
    return render(request,"Moneda/cara-cruz.html")

