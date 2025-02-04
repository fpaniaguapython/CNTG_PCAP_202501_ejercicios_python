# Distancia de Levenshtein
# https://pypi.org/project/Levenshtein/
# pip install levenshtein

from Levenshtein import distance

palabras = [
    "manzana", "libro", "cielo", "auto", "pelota", "viento", "feliz", "computadora", "agua", "fuego",
    "rojo", "verde", "amarillo", "flor", "estrella", "montaña", "río", "noche", "luz", "sombrero",
    "piedra", "árbol", "camino", "espejo", "ventana", "luna", "sol", "calor", "frío", "nieve",
    "tierra", "luna", "mar", "bosque", "risa", "lago", "café", "cultura", "guitarra", "bailar",
    "cantar", "leer", "escribir", "dibujar", "pintura", "viaje", "aventura", "naturaleza", "felicidad",
    "sueño", "amistad", "familia", "trabajo", "paz", "gracia", "alegría", "sentimiento", "música",
    "película", "teatro", "arte", "historia", "ciencia", "matemáticas", "tecnología", "programación",
    "lenguaje", "razón", "conocimiento", "aprender", "enseñar", "espejo", "reflejo", "invento", "idea",
    "inspiración", "creatividad", "innovación", "futuro", "pasado", "presente", "tiempo", "espacio",
    "pensamiento", "mente", "corazón", "alma", "pasión", "esperanza", "sueños", "meta", "logro",
    "trabajo", "esfuerzo", "victoria", "derrota", "lucha", "bajo", "alto", "corto", "largo", "fácil",
    "difícil", "bueno", "malo", "blanco", "negro", "gris", "colores", "tamaño", "forma", "dibujo",
    "mujer", "hombre", "niño", "niña", "familia", "amigos", "amor", "odio", "miedo", "confianza",
    "poder", "valentía", "sabiduría", "prudencia", "justicia", "equilibrio", "armonía", "diversidad", "unidad"
]

palabra = input('Introduce una palabra:')

# Búsqueda exacta
existe = palabra.lower() in palabras
print(existe)

# Búsqueda aproximada
# Versión Xabi
""" mas_proximo='Nada'
nivel_proximidad = 3

for p in palabras:
    if (distance(palabra, p) < nivel_proximidad):
        mas_proximo = p
        nivel_proximidad = distance(palabra, p)

print('La palabra más proxima es:', mas_proximo) """

# Versión Python 1 (utilizando el método sort con lambda)
if (not existe):
    palabras.sort(key = lambda palabra_actual : distance(palabra, palabra_actual))
    print(f'A lo mejor querías decir {palabras[0]}')

# Versión Python 2 (utilizando el método min con lambda)
if (not existe):
    palabra_mas_proxima = min(palabras, key = lambda palabra_actual : distance(palabra, palabra_actual))
    print(f'A lo mejor querías decir {palabra_mas_proxima}')

# Versión Python retorcida (convertir la lista en una lista de tuplas con las distancias y las palabras)
nueva_lista = [(distance(palabra_actual, palabra),palabra_actual) for palabra_actual in palabras]
print(sorted(nueva_lista)[0])