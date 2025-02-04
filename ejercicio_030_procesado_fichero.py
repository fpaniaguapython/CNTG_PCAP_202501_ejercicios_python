# https://babel.upm.es/~angel/teaching/pps/quijote.txt
# Ojo con las mayúsculas y minúsculas.

# 1. Leer el fichero y guardar el contenido en un variable
with open('quijote.txt',encoding='utf-8',mode='rt') as fichero:
    texto = fichero.read()
    #print(texto[-100:]) #Muestra los 100 últimos caracteres

# 2. Dada una palabra, averiguar si está o no está en el texto.
palabra = input('Introduce una palabra:')
existe = palabra.upper() in texto.upper()
print(f'La palabra {palabra} {"existe" if existe else "NO existe"} en el texto')

# Solución con index
# palabra = input('Introduce una palabra:')
# try:
#     posicion = texto.upper().index(palabra.upper())
#     print(f'La palabra {palabra} existe en el texto')
# except ValueError as ve:
#     print(f'La palabra {palabra} NO existe en el texto')

# 3. Dada una palabra, averiguar cuantas veces está en el texto.
palabra = input('Introduce una palabra:')
numero_apareciones = texto.upper().count(palabra.upper())
print(numero_apareciones)

# Solución con expresiones regulares
# import re
# apariciones= re.findall(palabra, texto, re.IGNORECASE)
# print(len(apariciones)) # 283 (apariciones una lista con las palabras originales que hacen 'match' con la cadena busqueda)

# 4. Generar un nuevo fichero en el que se cambien los nombres de los personajes.
personaje = input('Introduce nombre del personaje:')
personaje_reemplazo = input('Introduce nombre del personaje de reemplazo:')
import re
apariciones= re.findall(personaje, texto, re.IGNORECASE)
conjunto_apariciones = set(apariciones)
nuevo_texto = texto
for aparicion in conjunto_apariciones:
    if (aparicion.isupper()):
        nuevo_texto = nuevo_texto.replace(aparicion, personaje_reemplazo.upper())
    else:
        nuevo_texto = nuevo_texto.replace(aparicion, personaje_reemplazo)

with open('quijote_modificado.txt',encoding='utf-8',mode='wt') as fichero:
    fichero.write(nuevo_texto)