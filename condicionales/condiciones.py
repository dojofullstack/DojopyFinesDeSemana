""" python condiciones simples """

eres_freelancer = False
lista_tareas = ['nueva funcion projectx', 'comprar manzanas', 'ejecutar push']

if eres_freelancer:
    print('genial!')
    if len(lista_tareas) == 2:
        print('tareas ok!')
# else:
#     print('no se cumple')


""" python condiciones anidadas """

if len(lista_tareas) >= 5:
    print('tienes varias tareas!')
elif lista_tareas.count('comprar manzanas'):
    print('ve a comprar manzanas :D')
elif len(lista_tareas) >= 2:
    print('ok')
else:
    print('ninguna se valido, es lo que queda')


""" python condiciones anidadas con operacion or y and """

if len(lista_tareas) >= 2 and lista_tareas.count('comprar manzanas') and lista_tareas.index('ejecutar push'):
    print('todas son validas!')


if len(lista_tareas) >= 5 or lista_tareas.index('ejecutar push') == 1:
    print('al menos una es valida!')
else:
    print('niguna es valida :9')


print('#'*50)

if len(lista_tareas) >= 3 and lista_tareas.index('ejecutar push') == 1 or lista_tareas.count('comprar manzanas') == 1:
    print('super es valida!')

else:
    print('niguna es valida :9')
