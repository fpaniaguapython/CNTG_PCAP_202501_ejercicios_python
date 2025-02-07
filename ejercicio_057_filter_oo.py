# Definir una clase Candidato con los atributos nombre, ingles (bool), Python (bool)
# Creamos 4 instancias y las guardamos en una lista
# Utilizando una función lambda aplicar un filtro (función filter) y
#   obtener la lista de candidatos que sepan inglés y Python

class Candidato:
    def __init__(self, nombre : str, ingles : bool, python : bool):
        self.nombre = nombre
        self.ingles = ingles
        self.python = python

    def __repr__(self):
        return f'{self.nombre}-{self.ingles}-{self.python}'
    
    def __str__(self):
        return self.nombre
    
c1 = Candidato('Candidato 1', True, True)
c2 = Candidato('Candidato 2', True, False)
c3 = Candidato('Candidata 3', True, False)
c4 = Candidato('Candidata 4', True, True)

candidatos = (c1, c2, c3, c4)

# Solución sin lambdas
#def validar(candidato):
#    return candidato.ingles and candidato.python
# candidatos_aceptados = filter(validar, candidatos)

candidatos_aceptados = filter(lambda candidato : candidato.ingles and candidato.python, candidatos)

lista_candidatos_aceptados = list(candidatos_aceptados)
print(lista_candidatos_aceptados) # Utiliza el __repr__
print(lista_candidatos_aceptados[0]) # Utiliza el __str__ y si no existe el __repr__

# Este código es el equivalente al uso de filter de la línea 27
'''
candidatos = (c1, c2, c3, c4)
candidatos_aceptados = []
for candidato in candidatos:
    if (candidato.ingles and candidato.python):
        candidatos_aceptados.append(candidato)

print(candidatos_aceptados)
'''