# tipo de dato lista o array
lista_companies = ['facebook','google' ,'google', 'airbnb', 'netflix', 'twitter']
print(len(lista_companies))
print(type(lista_companies))

companie = 'facebook'
# print(len(companie))
list_companies2 = list(companie)
# print(list_companies2)

print(lista_companies[0])   # obtener el primero elemnto
print(lista_companies[-1])  # obtener el ultimo elemento
print(lista_companies[-2]) #  obtener el penultimo elemento
print(lista_companies[1:3]) # para obterner multiples elementos por rango

print(lista_companies[-2:])
print(lista_companies[len(lista_companies)-2:])

# print(dir(lista_companies))

"""
Propiedades y metodos para el objeto array:
'append',
'clear',
'copy',
'count',
'extend',
'index',
'insert',
'pop',
'remove',
'reverse',
'sort' """

lista_companies.append('whatsapp')
lista_companies.append('messegner')
# lista_companies.clear()
googles_vals = lista_companies.count('google')
lista_companies.extend(['etoro', 'uber'])

# print(lista_companies.index('uber'))
print(lista_companies)
print(len(lista_companies))
lista_companies.insert(len(lista_companies), 'instagram')
print(len(lista_companies))
print(lista_companies)

lista_companies.remove('twitter')
lista_companies.remove('netflix')
# print(lista_companies)

# delete_company = lista_companies.pop(0)

# print(delete_company)
# print(lista_companies)

# lista_companies.reverse()
# print(lista_companies)

# lista_companies.sort()
# print(lista_companies)

print(lista_companies)
lista_companies_new = lista_companies.copy()
lista_companies_new.append('dojopy')
print(lista_companies_new)
print(lista_companies)
