# Ordenar por población
ciudades_gallegas = [
    {"ciudad": "A Coruña", "poblacion": 246056},
    {"ciudad": "Vigo", "poblacion": 295364},
    {"ciudad": "Ourense", "poblacion": 105000},
    {"ciudad": "Santiago de Compostela", "poblacion": 96700},
    {"ciudad": "Lugo", "poblacion": 98207},
    {"ciudad": "Pontevedra", "poblacion": 82749},
    {"ciudad": "Ferrol", "poblacion": 74788},
    {"ciudad": "Cee", "poblacion": 16920},
    {"ciudad": "Ribeira", "poblacion": 24985},
    {"ciudad": "Vilagarcía de Arousa", "poblacion": 37675}
]

# 1. Ordenar la lista por el número de habitantes de mayor a menor

# Solución 1 - Con una función 'convencional'
# def valorar_ciudad(ciudad):
#     return ciudad['poblacion']

# ciudades_gallegas.sort(key=valorar_ciudad, reverse=True)
# print(ciudades_gallegas)

# Solución 2 - Con una función 'lambda'
ciudades_gallegas.sort(key=lambda ciudad : ciudad['poblacion'])
print(ciudades_gallegas)