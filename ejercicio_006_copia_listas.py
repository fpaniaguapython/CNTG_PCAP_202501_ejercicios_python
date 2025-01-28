# Copia por valor (porque son tipos básicos)
numero_1 = 10
numero_2 = numero_1 # Asignación del valor

print(numero_1)
print(numero_2)

numero_1 = 15
print(numero_1)
print(numero_2)

# Copia por referencia
numeros = [3, 4, 5]
numeros_duplicados = numeros # Asignación por referencia

print(numeros) # [3, 4, 5]
print(numeros_duplicados) # [3, 4, 5]

numeros[1]=8 # Esta asignación modifca numeros y numeros_duplicados (son lo mismo)
print(numeros) # [3, 8, 5]
print(numeros_duplicados) # [3, 8, 5]

# (Shallow copy) Copia a través de un slice
numeros = [3, 4, 5]
numeros_duplicados = numeros[:] # Copia superficial

print(numeros) # [3, 4, 5]
print(numeros_duplicados) # [3, 4, 5]

numeros[1]=8 # Esta asignación modifca numeros y numeros_duplicados (son lo mismo)
print(numeros) # [3, 8, 5]
print(numeros_duplicados) # [3, 4, 5]

# (Shallow copy) Copia a través de un slice con dos niveles de profundidad
numeros = [3, 4, [5, 6, 7]]
numeros_duplicados = numeros[:] # Copia superficial (el segundo nivel se copia por refencia)

print(numeros) # [3, 4, [5, 6, 7]]
print(numeros_duplicados) # [3, 4, [5, 6, 7]]

numeros[0]=11
numeros[2][0]=10
print(numeros) # [11, 4, [10, 6, 7]]
print(numeros_duplicados) # [3, 4, [10, 6, 7]]

# (Deep copy) Copia en profundidad
import copy

numeros = [3, 4, [5, 6, 7]]
numeros_duplicados = copy.deepcopy(numeros) # Copia en profundidad

print(numeros) # [3, 4, [5, 6, 7]]
print(numeros_duplicados) # [3, 4, [5, 6, 7]]

numeros[0]=11
numeros[2][0]=10
print(numeros) # [11, 4, [10, 6, 7]]
print(numeros_duplicados) # [3, 4, [5, 6, 7]]