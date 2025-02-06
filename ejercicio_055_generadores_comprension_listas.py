lista = [2, 8, 5, 3]

lista_dobles = [numero*2 for numero in lista]  # Genera otra lista
print(type(lista_dobles))  # <class 'list'>
print(lista_dobles)

generador_dobles = (numero*2 for numero in lista)  # Genera un generador
print(type(generador_dobles))  # <class 'generator'>
print(generador_dobles)

# Curiosidad:
# Si modificamos la lista original que utiliza el generador, los resultados cambian
for item in generador_dobles:
    if item == 16:
        lista[3] = 15
    print(item)

print('Fin:', lista[3])
