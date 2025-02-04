class Televisor:
    def __init__(self, marca, modelo):
        print('__init__')
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return '__str__'

    def __repr__(self):
        return '__repr__'

mi_tv = Televisor('Sony', 'LCD 1000')

print(mi_tv) # Utiliza __str__

lista_tv = [mi_tv]
print(lista_tv) # Utilizar __repr__