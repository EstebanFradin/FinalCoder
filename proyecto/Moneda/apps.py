from django.apps import AppConfig
import random

resultado =''


class MonedaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Moneda'

def moneda():
    MontoApostado = input('Ingrese el monto que desea apostar...')
    opciones = ['CARA', 'CRUZ']
    seleccionCPU = random.randint(0,1)
    seleccionJugador = input('Elige entre Cara o Cruz')
    if seleccionJugador.upper() == opciones[seleccionCPU]:
        print('Has ganado!!')
        #duplicar plata self.balance = self.balance + int(MontoApostado)
    else:
        #perder plata
        print('Lo sentimos, has perdido :(')
        
def slots():
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
        resultado = 'Felicidades, has ganado!!'
    else:
        resultado = 'Lo lamentamos, has perdido :('