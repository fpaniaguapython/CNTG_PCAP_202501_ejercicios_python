vehiculos = [('Seat',25_000,120), ('Fiat',15_000,80), ('Skoda',25_000,200), ('Nissan',18_000,180)]

# Utilizar la función sorted

# 1. Ordenar por precio de menor a mayor
vehiculos.sort(key=lambda vehiculo : vehiculo[1])
print('Test 1:',vehiculos)

# 2. Ordenar por precio de menor a mayor y (en caso de igualdad) por potencia de mayor a menor
def ponderar(vehiculo):
    return vehiculo[1],-vehiculo[2] # Devolución de una tupla

vehiculos.sort(key=ponderar)
print('Test 2:',vehiculos)

# 3. Ordenar por potencia de mayor a menor
def valorar_vehiculo(vehiculo):
    return vehiculo[2]

vehiculos.sort(key=valorar_vehiculo, reverse=True)
print('Test 3:',vehiculos)

# Solución Víctor
# vehiculos = [ ('Fiat',15_000,80), ('Skoda',25_000,200), ('Nissan',18_000,180), ('Seat',25_000,120)]
# vehiculos.sort(key=lambda vehiculo: vehiculo[2], reverse=True)
# def valorar_precio(vehiculo):
#     return vehiculo[1]
# vehiculos.sort(key=valorar_precio, reverse=False)
# print(vehiculos)