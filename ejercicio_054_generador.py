# Un generador es un elemento que 'genera' datos a medida que se le van pidiendo
import random

# Parte 1 - Generador sencillo


def funcion_generadora():
    while (True):
        numero_aleatorio = random.randint(1, 1_000)
        print('NA:', numero_aleatorio)
        if (numero_aleatorio == 13):
            break
        yield numero_aleatorio


for numero_aleatorio in funcion_generadora():
    print(numero_aleatorio)

# Generador de árboles
'''
def generador_arboles(numero_arboles):
    for i in range(numero_arboles):
        nombre = random.choice(
            ['Almendro', 'Higuera', 'Roble', 'Encina', 'Castaño'])
        altura = random.randint(1, 10)
        edad = random.randint(1, 100)
        yield (nombre, altura, edad)


arboles = generador_arboles(100)
for arbol in arboles:
    print('Arbol:', arbol)
'''
