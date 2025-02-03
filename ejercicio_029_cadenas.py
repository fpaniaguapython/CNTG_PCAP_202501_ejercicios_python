# SON INMUTABLES

# Función ord
punto_codigo = ord('a')
print(punto_codigo) # 97

# Función chr
letra = chr(98)
print(letra) # 'b'

# Slicing
print('Esto es una cadena de caracteres'[:-10]) # Esto es una cadena de

# Operadorse in y not in
print('az' in 'El cielo está azul esta tarde') # True

# Función min y max
print(min('Ordenador')) # O
print(max('Ordenador')) # r

# Método index - Indica la posición de la cadena buscada (ValueError si no existe)
alergeno = 'mostaza'
receta = 'Rebozar el pulpo en una disolución de aceite y mostaza'
print (alergeno in receta) # True
posicion = receta.index(alergeno) # Si no lo encuentra -> ValueError
print(posicion) # 47

# Función list - Convierte a lista los caracteres de la cadena
print(list(receta)) # ['R', 'e', 'b', 'o', 'z', 'a', 'r', ' ',...

# Método count - Cuenta el número de veces que una subcadena está presente en una cadena
print(receta.count(alergeno)) # 1

# Método find - Indica la posición de la cadena buscada (-1 si no lo encuentra)
posicion = receta.find('salicilico')
print(posicion) # -1

# Método capitalize - Convierte a formato 'oracion'
cadena = 'lO qUe SEa'
print(cadena.capitalize()) # Lo que sea

# Método center - Centra el texto en un espacio indicado
print('-'+cadena.center(20)+'-') #-     lO qUe SEa     -

# Métodos endswith, startswith - Indican si una cadena empieza o termina por una subcadena
fichero = 'mifoto.jpg'
print(fichero.endswith('jpg')) # True

# Métodos lower y upper - Convertir una a minúsculas o mayúsculas
nombre = 'python'
nombre.upper()
print(nombre) # python
nombre = nombre.upper()
print(nombre) # PYTHON


