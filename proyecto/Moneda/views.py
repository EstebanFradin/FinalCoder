from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from Moneda.forms import Registrar_User,UserEditForm,AvatarForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from Moneda.models import Avatar
from Moneda.apps import moneda,slots,random



# Create your views here.

#Vistas relacionadas al usuario

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

# Vista de Juegos
def caracruz_cara (request):
    opciones = ['CARA', 'CRUZ']
    seleccionCPU = random.randint(0,1)
    seleccionJugador = 'CARA'
    if seleccionJugador.upper() == opciones[seleccionCPU]:
        resultado = f'Ganaste {seleccionCPU}'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        resultado = f'perdiste {seleccionCPU}'
        #perder plata
    return render(request,"Moneda/cara-cruz.html", {'resultado': resultado})

def caracruz_cruz (request):
    opciones = ['CARA', 'CRUZ']
    seleccionCPU = random.randint(0,1)
    seleccionJugador = 'CRUZ'
    if seleccionJugador.upper() == opciones[seleccionCPU]:
        resultado = 'Ganaste'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        resultado = 'perdiste'
        #perder plata
    return render(request,"Moneda/cara-cruz.html", {'resultado': resultado})

def slots (request):


    opciones = ['#','@','*']
    row1 = [0,0,0]
    row2 = [0,0,0]
    row3 = [0,0,0]
    matriz = [row1,row2,row3]
    for i in matriz:
        x = 0
        for p in matriz[x]:
            matriz[x][0] = opciones[random.randint(0,2)]
            matriz[x][1] = opciones[random.randint(0,2)]
            matriz[x][2] = opciones[random.randint(0,2)]
            x += 1
    m1 = (matriz[0])
    m2 = (matriz[1])
    m3 = (matriz[2])
    if row2[0] == row2[1] and row2[1] == row2[2]:
        resultado = 'gamaste bro'
    else:
        resultado = 'perdiste amigo'

    return render(request,"Moneda/slots.html", {'m1':m1,'m2':m2,'m3':m3,'resultado': resultado})

def blackjack1 (request):
    opciones = [1,2,3,4,5,6]
    seleccionCPU = random.choice(opciones)
    seleccionJugador = 1
    if seleccionJugador == seleccionCPU:
        resultado = f'Ganaste----salio el {seleccionCPU}'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        resultado = f'Perdiste----salio el {seleccionCPU}'
        #perder plata
    return render(request,"Moneda/cara-cruz.html", {'resultado': resultado})

def blackjack2 (request):
    opciones = [1,2,3,4,5,6]
    seleccionCPU = random.choice(opciones)
    seleccionJugador = 2
    if seleccionJugador == seleccionCPU:
        resultado = f'Ganaste----salio el {seleccionCPU}'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        resultado = f'Perdiste----salio el {seleccionCPU}'
        #perder plata
    return render(request,"Moneda/cara-cruz.html", {'resultado': resultado})

def blackjack3 (request):
    opciones = [1,2,3,4,5,6]
    seleccionCPU = random.choice(opciones)
    seleccionJugador = 3
    if seleccionJugador == seleccionCPU:
        resultado = f'Ganaste----salio el {seleccionCPU}'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        resultado = f'Perdiste----salio el {seleccionCPU}'
        #perder plata
    return render(request,"Moneda/cara-cruz.html", {'resultado': resultado})

def blackjack4 (request):
    opciones = [1,2,3,4,5,6]
    seleccionCPU = random.choice(opciones)
    seleccionJugador = 4
    if seleccionJugador == seleccionCPU:
        resultado = f'Ganaste----salio el {seleccionCPU}'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        resultado = f'Perdiste----salio el {seleccionCPU}'
        #perder plata
    return render(request,"Moneda/cara-cruz.html", {'resultado': resultado})

def blackjack5 (request):
    opciones = [1,2,3,4,5,6]
    seleccionCPU = random.choice(opciones)
    seleccionJugador = 5
    if seleccionJugador == seleccionCPU:
        resultado = f'Ganaste----salio el {seleccionCPU}'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        resultado = f'Perdiste----salio el {seleccionCPU}'
        #perder plata
    return render(request,"Moneda/cara-cruz.html", {'resultado': resultado})

def blackjack6 (request):
    opciones = [1,2,3,4,5,6]
    seleccionCPU = random.choice(opciones)
    seleccionJugador = 6
    if seleccionJugador == seleccionCPU:
        resultado = f'Ganaste----salio el {seleccionCPU}'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        resultado = f'Perdiste----salio el {seleccionCPU}'
        #perder plata
    return render(request,"Moneda/cara-cruz.html", {'resultado': resultado})

# Vista del Formulario de Contacto

def Contacto (request):
   return render(request, "Final/templates/index.html")



