#https://babel.upm.es/~angel/teaching/pps/quijote.txt

#0. Obtener una palabra
palabra = input('Introduce una palabra:')

# 1. Leer el fichero y guardar el contenido en un variable
with open('quijote.txt',encoding='utf-8',mode='rt') as fichero:
    texto = fichero.read()
    #print(texto[-100:]) #Muestra los 100 últimos caracteres

# 2. Dada una palabra, averiguar si está o no está en el texto.

# 3. Dada una palabra, averiguar cuantas veces está en el texto.

# 4. Generar un nuevo fichero en el que se cambien los nombres de los personajes.

# Ojo con las mayúsculas y minúsculas.
