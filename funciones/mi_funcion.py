import time


def validar_nombre(nombre, pais='Perú'):
    try:
        print(pais)
        if nombre == 'cristian':
            # print('es correcto')
            return True
        else:
            print('usuario incorrecto!')
            return False
    except Exception as e:
        print(e)


def portal_con_dni():
    dni = ''

    while dni != 48276464:
        time.sleep(0.5)
        nombre = input('¿Hola, cual es tu nombre?: ')

        validacion_name = validar_nombre(nombre)
        if validacion_name == False:
            print('ingrese un usuario correcto..')
            continue

        dni = input('¿Hola, cual es tu dni?: ')
        dni = int(dni)
        if dni != 48276464:
            print('ingrese un documento de identidad valido')
        else:
            print('tienes acceso al portal, tus codigo es 010010201')



# portal_con_dni()

# validar_nombre(nombre='henry', pais='colombia')
