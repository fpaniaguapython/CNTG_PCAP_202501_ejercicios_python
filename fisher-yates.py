import random

def mezclar(lista_original, lista_mezclada=[]) :
    """
    Función recursiva para mezclar una lista de forma aleatoria.

    Args:
        lista_original (list): La lista original que queremos mezclar.
        lista_mezclada (list, opcional): La lista que contiene los elementos mezclados.
            Por defecto, es una lista vacía.

    Returns:
        list: La lista original mezclada de forma aleatoria.
    """
    if len(lista_original) == 0:
        return lista_mezclada

    '''
    # Original
    posicion_aleatoria = random.randint(0, len(lista_original) - 1)
    elemento_seleccionado = lista_original.pop(posicion_aleatoria)
    '''
    # Utilizando choice
    elemento_seleccionado = random.choice(lista_original)
    lista_original.remove(elemento_seleccionado)

    nueva_lista_mezclada = lista_mezclada + [elemento_seleccionado]

    return mezclar(lista_original, nueva_lista_mezclada)

# Ejemplo de uso:
lista_original = [1, 2, 3, 4, 5]
lista_mezclada = mezclar(lista_original)
print(lista_mezclada)