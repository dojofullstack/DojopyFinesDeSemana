
# programacion orientada a o objetos en Python

class NaturalRiqueza():
    def __init__(self):
        self.riquezas = ['costa', 'sierra', 'selva']

    def costa(self):
        print('riqueza de la costa')

    def sierra(self):
        print('riqueza de la sierra')

    def selva(self):
        print('riqueza de la selva')


class Planeta(NaturalRiqueza):
    def __init__(self, nombre, satelites, tamano, life=False, habitantes='0'):
        self.nombre = nombre
        self.satelites = satelites
        self.tamano = tamano
        self.life = life
        self.__habitantes = habitantes
        print('se termino de crear el constructor')
        NaturalRiqueza.__init__(self)

    def detectando_vida(self):
        print(self.__habitantes)
        print(f'hay vida en el planeta {self.nombre} ?')
        is_life = self.detectando_agua()
        if is_life:
            print('si hay agua!!')
        else:
            print('no hay agua :(')

    def detectando_agua(self):
        if self.nombre == 'tierra':
            self.__temperatura_promedio('15')
            print(self.riquezas)
            self.costa()
            self.sierra()
            self.selva()
            return True
        return False

    def __temperatura_promedio(self, temperatura):
        print(f'la temperatura es de {temperatura}')



# obj_marte = Planeta('marte','5', '10', False, '0')
# obj_marte.detectando_vida()
# print(obj_marte.satelites)
# print(obj_marte.life)
# print(dir(obj_marte))
# print(obj_marte.__dict__)
# obj_marte.detectando_vida()
# print('#'*20)

obj_tierra = Planeta('tierra','1', '5')
obj_tierra.detectando_vida()
print(obj_tierra.satelites)
# obj_tierra.__temperatura_promedio('15')
# print(obj_tierra.__habitantes)
