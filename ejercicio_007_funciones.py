def saludar():
    print("Hola")

def saludar_personalmente(nombre):
    print(f'Hola {nombre}')

def despedir_personalmente(nombre='Michael'):
    print(f'Adios {nombre}') 

def sumar(sumando_1 : int, sumando_2 : int) -> int: # Sugerencia de tipos
    resultado = sumando_1 + sumando_2
    return resultado

def funcion_calcular(inicio, salario=10, edad=20): # Opcionales SIEMPRE al final
    return salario+edad

print(funcion_calcular(10)) # 30
print(funcion_calcular(10, 50)) # 70
print(funcion_calcular(10, salario=80)) # 100
print(funcion_calcular(10, edad=20,salario=100)) # 120

def multiplicar(*numeros):
    print(type(numeros)) # tuple
    print(numeros)

multiplicar(3, 10, 3, 38, -3)

def dividir(*numeros, cantidades):
    print(numeros)
    print(cantidades)

def restar(cantidades, *numeros):
    print(numeros)
    print(cantidades)

dividir(3,8,cantidades=10)
restar(3,8,10)

def hacer_algo(**kwargs):
    print(type(kwargs)) #<clase 'dict'>
    print(kwargs) #{'nombre': 'Python', 'paradigma': 'Múltiple'}

hacer_algo(nombre='Python',paradigma='Múltiple')
