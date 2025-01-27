# Heterogéneas

# Construcción
lista_1 = [] # Lista vacía
lista_2 = list() # Lista vacía
lista_3 = ['Uno',2] # Lista con dos elementos

tupla_1 = ('Tres',4) # Tupla
lista_4 = list(tupla_1) # Lista a partir de una tupla (iterable)

dias_diario = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

# Acceder para leer
print(dias_diario[0]) #'Lunes'

# Acceder para modificar
dias_diario[0]='Luns'
dias_diario[2]='Mércores'
dias_diario[3]='Xoves'
dias_diario[4]='Venres'

# Recorrer una lista
print("*****")
for dia in dias_diario:
    print(dia)

# ¿Cómo saber si un elemento está en una lista?
print('Xoves' in dias_diario) # True
print('Sábado' in dias_diario) # False
print('Sábado' not in dias_diario) # True
print(not 'Sábado' in dias_diario) # True

# ¿Cómo saber el número de elementos de una lista?
print(len(dias_diario))

# List comprehension (comprensión de listas)
longitudes = [len(dia) for dia in dias_diario]
print(longitudes)