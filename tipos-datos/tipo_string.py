# tipo de datos string
empresa_it = "netflix airbnb7"
print(empresa_it)
#print(empresa_it)
#print(type(empresa_it))

number_startup_fintech = str(50)
print(number_startup_fintech)
print(type(number_startup_fintech))


print(dir(empresa_it))

print(empresa_it.capitalize())
print(empresa_it.lower())
print(empresa_it.upper())
print(empresa_it.replace('n3tflix', 'facebook'))
print(empresa_it.split(' '))
print(empresa_it.isalnum())
print(empresa_it.find('bnbrrr'))


empresa_it2 = 'mi empresa {} {}'
print(empresa_it2.format('dojopy', 'storewai'))
a = 'dojopy'
b = 'storewai'
print(f'mi empresa {a.upper()} {b.upper()}')
