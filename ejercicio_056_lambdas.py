# Un función lambda es (en teoría) de un solo uso

# lambda parametros : expresión que genera el retorno

def saludar(nombre):
    return f'Hola {nombre}'

# Esto se puede hacer, pero no se hace
saludar_lambda = lambda nombre : f'Hola {nombre}'

print(saludar_lambda('Julio'))

