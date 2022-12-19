from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from Moneda.forms import Registrar_User,UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from Moneda.models import Usuario,Contacto
from Moneda.apps import random



# Create your views here.

#Vistas relacionadas al usuario
def borrarContacto(request,nombre):
    nombre = Contacto.objects.get(nombre=nombre)
    return redirect('buscador-datos')

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
            return render(request, 'Moneda/editar-perfil.html', {'formi':formulario, 'errors': formulario.errors})

    else:
        formulario = UserEditForm(initial = { "first_name": usuario.first_name,"email": usuario.email})


    return render(request, 'Moneda/editar-perfil.html', {'form':formulario}) 
 
# Vista de Juegos
@login_required
def caracruz_cara (request):
    user = Usuario.objects.get(usuario=request.user)
    resultado = user.balance
    opciones = ['CARA', 'CRUZ']
    seleccionCPU = random.randint(0,1)
    seleccionJugador = 'CARA'
    if seleccionJugador.upper() == opciones[seleccionCPU]:
        user.balance = user.balance + (user.cantidad_apostar * 2)
        user.win += 1
        user.save()
        resultado = f'HAS GANADO. FELICITACIONES!!. Ahora tienes: {user.balance}$'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        user.balance = user.balance - user.cantidad_apostar
        user.lose += 1
        user.save()
        resultado = f'HAS PERDIDO!. Ahora tienes: {user.balance}$'
        #perder plata
    return render(request,"Moneda/cara-cruz.html", {'resultado': resultado})

@login_required
def caracruz_cruz (request):
    user = Usuario.objects.get(usuario=request.user)
    resultado = user.balance
    opciones = ['CARA', 'CRUZ']
    seleccionCPU = random.randint(0,1)
    seleccionJugador = 'CRUZ'
    if seleccionJugador.upper() == opciones[seleccionCPU]:
        user.balance = user.balance + (user.cantidad_apostar * 2)
        user.win += 1
        user.save()
        resultado = f'HAS GANADO. FELICITACIONES!!. Ahora tienes: {user.balance}$'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        user.balance = user.balance - user.cantidad_apostar
        user.lose += 1
        user.save()
        resultado = f'HAS PERDIDO. Ahora tienes: {user.balance}$'
        #perder plata
    return render(request,"Moneda/cara-cruz.html", {'resultado': resultado})

@login_required
def slots (request):

    user = Usuario.objects.get(usuario=request.user)

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
        user.balance = user.balance + (user.cantidad_apostar * 10)
        user.win =+ 1
        user.save()
        resultado = f'Felicidades, has ganado!!. Ahora tienes: {user.balance}$'
    else:
        user.balance = user.balance - user.cantidad_apostar
        user.lose += 1
        user.save()
        resultado = f'Lo lamentamos, has perdido. Ahora tienes: {user.balance}$'

    return render(request,"Moneda/slots.html", {'m1':m1,'m2':m2,'m3':m3,'resultado': resultado})

@login_required
def blackjack1 (request):
    user = Usuario.objects.get(usuario=request.user)
    opciones = [1,2,3,4,5,6]
    seleccionCPU = random.choice(opciones)
    seleccionJugador = 1
    if seleccionJugador == seleccionCPU:
        user.balance = user.balance + (user.cantidad_apostar * 4)
        user.win =+ 1
        user.save()
        resultado = f'GANASTE,salio el número: "{seleccionCPU}" | (ahora tienes: {user.balance}$)'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        user.balance = user.balance - user.cantidad_apostar
        user.lose += 1
        user.save()
        resultado = f'PERDISTE,salio el número: "{seleccionCPU}" | (ahora tienes: {user.balance}$)'
        #perder plata
    return render(request,"Moneda/blackjack.html", {'resultado': resultado})

@login_required
def blackjack2 (request):
    user = Usuario.objects.get(usuario=request.user)
    opciones = [1,2,3,4,5,6]
    seleccionCPU = random.choice(opciones)
    seleccionJugador = 2
    if seleccionJugador == seleccionCPU:
        user.balance = user.balance + (user.cantidad_apostar * 4)
        user.win =+ 1
        user.save()
        resultado = f'GANASTE,salio el número: "{seleccionCPU}" | (ahora tienes: {user.balance}$)'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        user.balance = user.balance - user.cantidad_apostar
        user.lose += 1
        user.save()
        resultado = f'PERDISTE,salio el número: "{seleccionCPU}" | (ahora tienes: {user.balance}$)'
        #perder plata
    return render(request,"Moneda/blackjack.html", {'resultado': resultado})

@login_required
def blackjack3 (request):
    user = Usuario.objects.get(usuario=request.user)
    opciones = [1,2,3,4,5,6]
    seleccionCPU = random.choice(opciones)
    seleccionJugador = 3
    if seleccionJugador == seleccionCPU:
        user.balance = user.balance + (user.cantidad_apostar * 4)
        user.win =+ 1
        user.save()
        resultado = f'GANASTE,salio el número: "{seleccionCPU}" | (ahora tienes: {user.balance}$)'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        user.balance = user.balance - user.cantidad_apostar
        user.lose += 1
        user.save()
        resultado = f'PERDISTE,salio el número: "{seleccionCPU}" | (ahora tienes: {user.balance}$)'
        #perder plata
    return render(request,"Moneda/blackjack.html", {'resultado': resultado})

@login_required
def blackjack4 (request):
    user = Usuario.objects.get(usuario=request.user)
    opciones = [1,2,3,4,5,6]
    seleccionCPU = random.choice(opciones)
    seleccionJugador = 4
    if seleccionJugador == seleccionCPU:
        user.balance = user.balance + (user.cantidad_apostar * 4)
        user.win =+ 1
        user.save()
        resultado = f'GANASTE,salio el número: "{seleccionCPU}" | (ahora tienes: {user.balance}$)'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        user.balance = user.balance - user.cantidad_apostar
        user.lose += 1
        user.save()
        resultado = f'PERDISTE,salio el número: "{seleccionCPU}" | (ahora tienes: {user.balance}$)'
        #perder plata
    return render(request,"Moneda/blackjack.html", {'resultado': resultado})

@login_required
def blackjack5 (request):
    user = Usuario.objects.get(usuario=request.user)
    opciones = [1,2,3,4,5,6]
    seleccionCPU = random.choice(opciones)
    seleccionJugador = 5
    if seleccionJugador == seleccionCPU:
        user.balance = user.balance + (user.cantidad_apostar * 4)
        user.win =+ 1
        user.save()
        resultado = f'GANASTE,salio el número: "{seleccionCPU}" | (ahora tienes: {user.balance}$)'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        user.balance = user.balance - user.cantidad_apostar
        user.lose += 1
        user.save()
        resultado = f'PERDISTE,salio el número: "{seleccionCPU}" | (ahora tienes: {user.balance}$)'
        #perder plata
    return render(request,"Moneda/blackjack.html", {'resultado': resultado})

@login_required
def blackjack6 (request):
    user = Usuario.objects.get(usuario=request.user)
    opciones = [1,2,3,4,5,6]
    seleccionCPU = random.choice(opciones)
    seleccionJugador = 6
    if seleccionJugador == seleccionCPU:
        user.balance = user.balance + (user.cantidad_apostar * 4)
        user.win =+ 1
        user.save()
        resultado = f'GANASTE,salio el número: "{seleccionCPU}" | (ahora tienes: {user.balance}$)'
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        user.balance = user.balance - user.cantidad_apostar
        user.lose += 1
        user.save()
        resultado = f'PERDISTE,salio el número: "{seleccionCPU}" | (ahora tienes: {user.balance}$)'
        #perder plata
    return render(request,"Moneda/blackjack.html", {'resultado': resultado})

# Vista del Formulario de Contacto y Búsqueda

def contactoForm (request):

    if request.method == "POST":
        
        contact = Contacto.objects.create(nombre=request.POST['nombre'], mail=request.POST['mail'], cel=request.POST['cel'],msj=request.POST['msj'])
        contact.save()

        
        return redirect("home-inicio")
        
    return render(request, "Moneda/contacto.html")

def buscarDatos (request):
    return render(request, 'Moneda/busqueda.html')
    

def buscar(request):
    if request.GET["nombreb"]:
        name = request.GET["nombreb"]
        persona = Contacto.objects.filter(nombre__icontains=name)
        return render(request, 'Moneda/resultado-bsq.html', {'name':name,'persona':persona })
    else:
        respuesta = f'No has enviado datos'

    return HttpResponse(respuesta)


