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

class Impresora:
    def __init__(self, marca : str, modelo : str, precio : int, velocidad : int):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.velocidad = velocidad
    
    def imprimir(self, texto='Por defecto'):
        print(f'Soy {self.marca}-{self.modelo} y estoy imprimiendo "{texto}"')

    def pitar(self):
        print(f'Soy {self.marca}-{self.modelo} y estoy pitando')


epson = Impresora('Epson', 'Stylus Color', 300, 10)
hp = Impresora('Hewlett Packard', 'AS330', 450, 80)

epson.imprimir('El texto que quiero imprimir')
epson.pitar()
hp.imprimir('Otro texto para imprimir')
hp.pitar()

    

    