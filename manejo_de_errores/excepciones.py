# python manejo de errroes.
lastName = 'henry'

try:
    try:
        print(lastName.uper())
    except Exception as e:
        print(e)
    print('dentro del try except main')
except NameError:
    print('esa variable no esta declarada :9')
except Exception as e:
    print(e)

# print(lastName.uper())

try:
    # print(lastName.uper())
    print('hola mundo')
except AttributeError:
    print('no existe ese metodo')
finally:
    print('final de la excepcion')
