from django.urls import path
from Moneda.views import *

urlpatterns = [
    path('blackjack/', blackjack, name="juego-blackjack"),
    path('slots/', slots, name="juego-slots"),
    path('cara-o-cruz/',caracruz, name="juego-caracruz"),
    path('iniciar-sesion/', inicio_sesion, name="inicia-sesion"),
    path('contacto/',Contacto, name="home-contacto"),
    ]