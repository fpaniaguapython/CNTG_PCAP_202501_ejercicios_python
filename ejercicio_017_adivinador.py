# 1. Generar un número aleatorio entre 1 y 9.
# 2. Solicitar al usuario utilizando la función input un número
# 3. Vamos a contar el número de intentos que ha necesitado para 'adivinar' el número
# 4. Si ha necesitado 3 o menos veces, es adivino. Si no, es un fraude.

import random

numero_secreto = random.randint(1,9)
adivinado = False
intentos = 0

while (not adivinado):
    intentos+=1
    numero_candidato = int(input('Número candidato:'))
    if (numero_candidato==numero_secreto):
        adivinado = True
    else:
        print("Error. No es el número secreto")

if (intentos<=3):
    print("Eres un adivino")
else:
    print("Eres un fraude")