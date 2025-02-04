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
existe = palabra.lower() in palabras
print(existe)

# distance(palabra1, palabra2)