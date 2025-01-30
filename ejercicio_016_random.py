import random

random.seed(808.3) # Inicializamos la secuencia
print(random.random()) # [0,1)
print(random.random()) # [0,1)

random.seed() # Reiniciamos la semilla a la elegida por el sistema
print(random.random()) # [0,1)
print(random.random()) # [0,1)

print(random.randrange(100)) # Número entero [0,100)
print(random.randrange(50,100)) # Número entero [50,100)

print(random.randint(50,100)) # Número entero [50,100]