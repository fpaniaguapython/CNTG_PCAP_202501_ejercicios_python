# Un función lambda es (en teoría) de un solo uso

# lambda parametros : expresión que genera el retorno

def saludar(nombre):
    return f'Hola {nombre}'

# Esto (asignar la función lambda a una variable) se puede hacer, pero no se hace
saludar_lambda = lambda nombre : f'Hola {nombre}'
print(saludar_lambda('Julio'))

# Esto (asignar la función lambda a una variable) se puede hacer, pero no se hace
sumar = lambda a, b: a+b
print(sumar(3,8))

#filter (obtener un subconjunto de una lista, tupla,... (un iterable) que cumple con una condición)
edades = (18, 9, 21, 88, 17)

# Obtener la lista de los mayores de edad (utilizando una función 'tradicional')
def es_mayor_edad(edad):
    return edad>=18

mayores_de_edad = filter(es_mayor_edad, edades)
print(list(mayores_de_edad))

# Obtener la lista de los mayores de edad (utilizando una función lambda)
mayores_de_edad = filter(lambda edad : edad>=18, edades)
print(type(mayores_de_edad)) # <class 'filter'>
print(list(mayores_de_edad)) # La conversión a list es porque lo que devuelve filter es 

#map (obtener un cojunto con una 'transformación' de los elementos de una lista, tupla... (iterable))
edades = (18, 9, 21, 88, 17)

nuevas_edades = map(lambda edad : edad+1, edades)
print(type(nuevas_edades)) # <class 'map'>
print(list(nuevas_edades)) # [19, 10, 22, 89, 18]