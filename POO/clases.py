
# creando clases con Python

class Auto:
    color = ''
    kilometraje = ''
    modelo = ''
    motor = ''


class Piloto:
    nombre = ''
    edad = ''
    experiencia = ''


obj_auto = Auto()
print(obj_auto)
obj_auto.modelo = 'tesla'
obj_auto.kilometraje = '1200'
obj_auto.color = 'rojo'
obj_auto.motor = 'xyz'
print(obj_auto.__dict__)

# print(type('hello'))
# print(type(obj_auto))
# print(dir(obj_auto))

obj_auto_toyota = Auto()
obj_auto_toyota.modelo = 'toyota'
obj_auto_toyota.kilometraje = '1500'
obj_auto_toyota.color = 'azul'
obj_auto_toyota.motor = 'a1'
print(obj_auto_toyota.__dict__)


obj_josue = Piloto()
obj_josue.nombre = 'josue'
obj_josue.edad = '25'
obj_josue.experiencia = '3 años'

print(obj_josue.__dict__)
