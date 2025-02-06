# Crear una clase Actuante
# Crear una clase Pelicula
# Una película tiene una lista de actuantes
# Convertir la película en un iterador y recorrer la lista de actuantes

class Actuante:
    def __init__(self, nombre):
        self.nombre = nombre


class Pelicula:
    def __init__(self, titulo, actuantes):
        self.titulo = titulo
        self.actuantes = actuantes

    def __iter__(self):
        self.__current_position = -1
        return self

    def __next__(self):
        self.__current_position += 1
        if (self.__current_position == len(self.actuantes)):
            raise StopIteration()
        return self.actuantes[self.__current_position]


a1 = Actuante('Cristiano Ronaldo')
a2 = Actuante('Laura Rodríguez')
p1 = Pelicula('Lo que el viento se llevó', [a1, a2])

for actuante in p1:
    print(actuante.nombre)
