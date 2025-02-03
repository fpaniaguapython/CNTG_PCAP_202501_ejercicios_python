lista = ['Primavera', 'Verano', 'Otoño', 'Invierno']

# Función sorted --> Generar una nueva lista ordenada
lista_ordenada = sorted(lista) # Indicando reverse=True invierte el orden
print('Lista:', lista)
print('Lista ordenada:', lista_ordenada)

# Método sort --> Ordenar la lista
lista.sort() # Indicando reverse=True invierte el orden
print('Lista (sort):', lista)

# Problema con las cadenas de caracteres - El orden viene dado por el PUNTO DE CÓDIGO 
lista = ['Primavera', 'Verano', 'otoño', 'Invierno']
lista_ordenada = sorted(lista) # Indicando reverse=True invierte el orden
print('Lista:', lista)
print('Lista ordenada:', lista_ordenada) # Lista ordenada: ['Invierno', 'Primavera', 'Verano', 'otoño'] (otoño va al final porque la o minúscula va después de las mayúsculas en las tablas de caracteres)

# Las listas de números las ordena correctamente
lista_numeros = [100000,38,10,88,3234234]
print(sorted(lista_numeros)) # [10, 38, 88, 100000, 3234234]

# Ordenar una lista de tuplas (ordena por el primer elemento)
lista_tuplas = [(3,8),(10,1),(-4,5)]
lista_tuplas_ordenadas = sorted(lista_tuplas)
print(lista_tuplas_ordenadas) # [(-4, 5), (3, 8), (10, 1)]

# El argumento key
def valoracion(elemento):
    return elemento[1] # Segundo elemento de cada tupla

lista_tuplas_ordenadas = sorted(lista_tuplas, key=valoracion)
print(lista_tuplas_ordenadas) # [(10, 1), (-4, 5), (3, 8)]

lista_tuplas.sort(key=valoracion)
print(lista_tuplas) # [(10, 1), (-4, 5), (3, 8)]






