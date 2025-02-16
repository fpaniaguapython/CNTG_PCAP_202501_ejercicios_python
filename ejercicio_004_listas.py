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
dias_diario = ['Luns', 'Martes', 'Mércores', 'Xoves', 'Venres']

# Obtener una lista con las longitudes de los días
longitudes = [len(dia) for dia in dias_diario]
print(longitudes)

# Obtener una lista con los días de la semana convertidos a mayúsculas
# Versión 'clásica'
dias_mayusculas = []
for dia in dias_diario:
    dias_mayusculas.append(dia.upper())

# Versión 'list comprehension'
dias_mayusculas = [dia.upper() for dia in dias_diario]
print(dias_mayusculas)

# Obtener una lista con los tres primeros caracteres de cada día
dias_mayusculas = [dia[0:3] for dia in dias_diario]
print(dias_mayusculas)

# Censurar los elementos de una lista (calamidad y feo)
frase = 'Eres un calamidad y además eres feo'
lista_palabras = frase.split(' ')

def censurar(palabra):
    if palabra=='calamidad' or palabra=='feo':
        return '***'
    else:
        return palabra

lista_palabras_censuradas = [censurar(palabra) for palabra in lista_palabras]
frase_censurada = ' '.join(lista_palabras_censuradas)
print(frase_censurada) # Eres un *** y además eres ***

# Obtener una lista equivalente a dias_diario con el formato ***nombre_dia*** en minúscula
dias_diario = ['Luns', 'Martes', 'Mércores', 'Xoves', 'Venres']

dias_minusculas = ['***'+dia.lower()+'***' for dia in dias_diario]
print(dias_minusculas) # ['***luns***', '***martes***', '***mércores***', '***xoves***', '***venres***']

# Comprensión de listas con condición
dias_diario = ['Luns', 'Martes', 'Mércores', 'Xoves', 'Venres']

# if
dias_con_e = [dia for dia in dias_diario if 'e' in dia]
print(dias_con_e) # ['Martes', 'Mércores', 'Xoves', 'Venres']

# if-else
dias_con_r = [dia if ('r' in dia) else '***' for dia in dias_diario]
print(dias_con_r) # ['***', 'Martes', 'Mércores', '***', 'Venres']

# slice - notación abreviada
print(dias_diario[0:len(dias_diario)]) # Desde el primero hasta el último
print(dias_diario[:]) # Desde el primero hasta el último
print(dias_diario[0:3]) # Tres primeros
print(dias_diario[:3]) # Tres primeros
print(dias_diario[3:]) # ['Xoves', 'Venres']
print(dias_diario[len(dias_diario)-2:]) # 2 últimos ['Xoves', 'Venres']
print(dias_diario[-2:]) # 2 últimos ['Xoves', 'Venres']
print(dias_diario[::2]) # Cada dos elementos ['Luns', 'Mércores', 'Venres']

# slice - notación 'extendida'
corte = slice(1,2)
print(type(corte)) # <class 'slice'>
print(dias_diario[corte])# ['Martes']