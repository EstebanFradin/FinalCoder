from django.urls import path
from Moneda.views import slots,inicio_sesion,registrar_usuario,editar_perfil,ver_perfil,blackjack1,blackjack2,blackjack3,blackjack4,blackjack5,blackjack6,caracruz_cara,caracruz_cruz, contactoForm, buscarDatos,buscar,borrarContacto
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('blackjack1/', blackjack1, name="juego-blackjack"),
    path('blackjack2/', blackjack2, name="juego-blackjack2"),
    path('blackjack3/', blackjack3, name="juego-blackjack3"),
    path('blackjack4/', blackjack4, name="juego-blackjack4"),
    path('blackjack5/', blackjack5, name="juego-blackjack5"),
    path('blackjack6/', blackjack6, name="juego-blackjack6"),
    path('slots/', slots, name="juego-slots"),
    path('cara-o-cruz1/',caracruz_cara, name="juego-caracruz-cara"),
    path('cara-o-cruz2/',caracruz_cruz, name="juego-caracruz-cruz"),

    path('iniciar-sesion/', inicio_sesion, name="auth-login"),
    path('registrar/', registrar_usuario, name="auth-register"),
    path('cerrar-sesion/',LogoutView.as_view(template_name='Moneda/logout.html'), name="auth-logout"),
    path('edit-perfil/', editar_perfil, name="auth-editar-perfil"),
    path('perfil/', ver_perfil, name="auth-perfil"),

    path('contacto/',contactoForm, name="home-contacto"),
    path('buscar-datos/', buscarDatos, name="buscador-datos"),
    path('buscar/', buscar, name="resultados"),
    path('eliminar/', borrarContacto, name="borrar"),
    ]