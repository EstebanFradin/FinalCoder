from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from Moneda.forms import Registrar_User,UserEditForm,AvatarForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from Moneda.models import Avatar


# Create your views here.

@login_required
def blackjack (request):
    return render(request,"Moneda/blackjack.html")

@login_required
def slots (request):
    return render(request,"Moneda/slots.html")

@login_required
def caracruz (request):
    return render(request,"Moneda/cara-cruz.html")

def ver_perfil(request):
    return render(request,"Moneda/perfil.html")

def inicio_sesion (request):
     errors = ""

     if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])
            
            if user is not None:
                login(request, user)
                return redirect("home-inicio")
            else:
                return render(request, "Moneda/login.html", {"form": formulario, "errors": "Credenciales invalidas"})

        else:

            return render(request, "Moneda/login.html", {"form": formulario, "errors": formulario.errors})

     formulario = AuthenticationForm()
     return render(request, "Moneda/login.html", {"form": formulario, "errors": errors})

def registrar_usuario (request):

    if request.method == "POST":
        formulario = Registrar_User(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home-inicio')
        else:
            return render(request, "Moneda/login.html", {"form": formulario, "errors": formulario.errors})
    

    formulario = Registrar_User()
    return render(request, "Moneda/register.html", {"form": formulario})

@login_required
def editar_perfil(request):  
    usuario = request.user

    if request.method == "POST":
        formulario = UserEditForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.first_name = data["first_name"] 
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.save()
            return redirect("home-inicio")
        else:
            return render(request, 'Moneda/editar-perfil.html', {'form':formulario, 'errors': formulario.errors})

    else:
        formulario = UserEditForm(initial = { "first_name": usuario.first_name,"email": usuario.email})


    return render(request, 'Moneda/editar-perfil.html', {'form':formulario}) 
 
@login_required
def elegir_avatar(request):
    if request.method == "POST":
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = request.user

            avatar = Avatar(user=usuario, imagen=data["imagen"])
            avatar.save()
            return redirect("home-inicio")
        else:
            return render(request, 'Moneda/agregar-avatar.html',{"form": formulario, "errors":formulario.errors})


    formulario = AvatarForm()

    return render(request, 'Moneda/agregar-avatar.html',{"form": formulario})

def Contacto (request):
   return render(request, "Final/templates/index.html")



