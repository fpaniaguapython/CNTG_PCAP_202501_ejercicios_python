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

# Métodos isalnum(), isalpha(), isdigit() - Indican si la cadena tiene digitos y caracteres; sólo caracteres; sólo dígitos

# Métodos islower(), isupper() - Indican si la cadena está en minúsculas o mayúsculas

# Método isspace() - Indica si la cadena está compuesta solo por espacios

# Método join() - Construye una cadena a partir de un iterable ('contrario' del split)

cadena_base = 'x'
lista_elementos = ['Uno','Dos','Tres']
cadena_resultado = cadena_base.join(lista_elementos)
print(cadena_resultado) # UnoxDosxTres

# Métodos lower() y upper() - Conversión a minúsculas y mayúsculas

# Métodos lstrip(), rstrip(), strip() - Eliminan los espacios en blanco de la izquierda, la derecha o ambos lados

pedido = '     café     '
print(pedido.strip()) # 'café'

# Métodos replace() - Reemplaza una subcadena por otra en un str

# Método rfind() - Igual que find pero empezando por la derecha de la cadena

# Método split() - Genera una lista con los token de la cadena indicando el separador

# Método swapcase() y title() - Cambia mayúsculas por minúsculas y viceversa; pone en mayúsculas la primera letra de cada palabra y el resto en minúsculas

texto = 'bOLsa de vaLOres: en alta'
print(texto.swapcase()) # BolSA DE VAloRES: EN ALTA
print(texto.capitalize()) # Bolsa de valores: en alta
print(texto.title()) # Bolsa De Valores: En Alta
