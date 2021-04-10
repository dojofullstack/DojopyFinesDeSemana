# tipo de dato dict

""" metodos y propiedas para el objeto dict
 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
"""

registro_usuarios = {
    'user': 'henry',
    'user2': 'cristian',
    'user3': 'Jose',
    'user4': 'Josue',
}

print(registro_usuarios)
print(type(registro_usuarios))
user_edad = dict([['henry', '25'], ['jose', '26']])
# print(user_edad)

print(len(registro_usuarios))

# print(registro_usuarios['user55'])

print(registro_usuarios.get('user2', 'user not exist'))
# print('hello world')

# print(dir(registro_usuarios))
# print(registro_usuarios.clear())
# print(registro_usuarios.keys())
# print(registro_usuarios.values())

# print(registro_usuarios.popitem())
# print(registro_usuarios)

# registro_usuarios.pop('user')
# print(registro_usuarios)
registro_usuarios['user4'] = 'Josue 25'
registro_usuarios['user5'] = 'Rick'
print(registro_usuarios)

registro_usuarios.update({'user6': 'pepe'})
print(registro_usuarios)
