# LIFO (Last In First Out) - Pila

# FIFO (First In First Out) - Cola

# Implementar una cola con funciones

cola = list()

def agregar(cola : list, item : any):
    cola.append(item)
    print('Agregar:',cola)

def obtener(cola : list) -> any:
    # Método 'cutre'
    """ item = cola[0]
    del cola[0]
    print('Consumir:',cola)
    return item """

    # Método 'guay'
    item = cola.pop(0)
    print('Consumir:', cola)
    return item

agregar(cola, 1)
agregar(cola, 2)
agregar(cola, 3)
print('Procesando:', obtener(cola))
agregar(cola, 4)
print('Procesando:', obtener(cola))