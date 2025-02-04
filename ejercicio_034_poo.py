# clase vs objeto
# atributo - define el estado
# método - define el comportamiento
# constructor (__init__) es un método especial que se ejecuta cuando se crea una instancia
# self - Es una convención para hacer referencia al objeto en el que estamos desde dentro de la clase

class Enemigo:
    def __init__(self, nombre, energia): # Constructor (el que inicializa el objeto)
        self.nombre = nombre
        self.energia = energia
        self.estado = 'Vivo' # No todos los atributos se reciben como argumento

    def caminar(self, distancia):
        print(f'Soy {self.nombre} y estoy caminando {distancia}')

sauron = Enemigo('Sauron', 1_000) # Instanciación de un OBJETO de la CLASE Enemigo
print(sauron.energia) # Acceso a un atributo

# Crear una clase Impresora que tenga 4 atributos y 2 métodos.
# Crear dos objetos de la clase impresora 
# Ejecutar los métodos de las dos impresoras