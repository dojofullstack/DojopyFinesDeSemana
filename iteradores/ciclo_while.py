# iterador while
import time

team = ['jesus', 'carlos', 'henry', 'josue', 'jose', 'cristian']
contador = 0

# if len(team) != 5:
#     print('correcot es 6')

dni = ''

while dni != 48276464:
    time.sleep(0.5)
    dni = input('¿Hola, cual es tu dni?')
    dni = int(dni)
    if dni != 48276464:
        print('ingrese un documento de identidad valido')
    else:
        print('tienes acceso al portal, tus codigo es 010010201')
