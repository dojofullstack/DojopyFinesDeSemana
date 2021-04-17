
""" python ciclo For """

nombre = 'Henry Vasquez Conde'
# nombre = list(nombre)
# print(nombre)

lista_empresas_it = ['twitter', 'netflix', 'xioami', 'apple']
lista_divisas = ['euro', 'dolar', 'jen', 'libra-esterlina']

precio_lista_divisas = {
    'libra-esterlina': 1.5
}

# for elemento in nombre:
#     print(elemento.upper()* 10)

for item in lista_empresas_it:
    try:
        print(item.upper())
        if len(lista_empresas_it) >= 4:
            for value in lista_divisas[2:]:
                print(value)
    except Exception as e:
        print(e)

print('#'*20)

for index, value in enumerate(lista_divisas):
    if index == 3:
        precio = precio_lista_divisas.get(value)
        print(f'El precio de {value} es {precio} dolares')

print('#'*20)


for value in range(1000):
    print(value)
    if value >= 500:
        print('ejecutando break')
        break
    if value >= 499:
        print('ejecutando continue')
        continue
    print('buenos dias!', value)

print('termino el For')
