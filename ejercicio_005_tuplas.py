# Colección de datos heterogéneos inmutable
tupla = () # Crea una tupla
tupla = (3,4) # Crea una tupla
tupla = (3) # Crea un int
tupla = ('Hola' + ' a todo') # Crea un string
tupla = (3,) # Crea una tupla con un único elemento

tupla = tuple() # Una tupla vacía
tupla = tuple([3,8,10]) # A partir de una lista

# Todo lo demás es igual que la lista, pero sin permitir la modificación
# tupla[0] = 10 # TypeError: 'tuple' object does not support item assignment

tupla = ('borja', 'nuria', 'rosana')

lista = [nombre.capitalize() for nombre in tupla] #Tupla como origen de una lista
print(type(lista))
print(lista)