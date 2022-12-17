from django.urls import path
from Moneda.views import blackjack,slots,caracruz,Contacto,inicio_sesion,registrar_usuario,editar_perfil,ver_perfil,elegir_avatar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('blackjack/', blackjack, name="juego-blackjack"),
    path('slots/', slots, name="juego-slots"),
    path('cara-o-cruz/',caracruz, name="juego-caracruz"),

    path('iniciar-sesion/', inicio_sesion, name="auth-login"),
    path('registrar/', registrar_usuario, name="auth-register"),
    path('cerrar-sesion/',LogoutView.as_view(template_name='Moneda/logout.html'), name="auth-logout"),
    path('edit-perfil/', editar_perfil, name="auth-editar-perfil"),
    path('perfil/', ver_perfil, name="auth-perfil"),
    path('avatar/', elegir_avatar, name="auth-avatar"),

    path('contacto/',Contacto, name="home-contacto"),
    ]