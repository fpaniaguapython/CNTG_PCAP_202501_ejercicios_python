'''
Clase Vehículo
- nombre
- velocidad
- arrancar()
- parar()
- avanzar()

Clase Automovil que hereda de de Vehiculo y que incorpora los atributos:
- número de ruedas
- litros de consumo a los 100 km
- avanzar()

Clase Barco que hereda de Vehiculo y que incopora los atributos:
- eslora
- manga
- nudos
- atracar()
- avanzar()
'''

class Vehiculo:
    def __init__ (self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad

    def arrancar(self):
        print(f'Soy el Vehiculo {self.nombre} y estoy arrancando')

    def parar(self):
        print(f'Soy el Vehiculo {self.nombre} y estoy parando')

    def avanzar(self):
        print(f'Soy el Vehiculo {self.nombre} y estoy avanzando')

class Automovil(Vehiculo):
    def __init__(self, nombre, velocidad, numero_ruedas, consumo):
        super().__init__(nombre, velocidad)
        self.numero_ruedas = numero_ruedas
        self.consumo = consumo
    
    def avanzar(self): #Sobreescritura del método
        super().avanzar() 
        print(f'Soy el Automovil {self.nombre} y estoy avanzando')

class Barco(Vehiculo):
    def __init__(self, nombre, velocidad, eslora, manga, nudos):
        super().__init__(nombre, velocidad)
        self.eslora = eslora
        self.manga = manga
        self.nudos = nudos
        
    def atracar(self):
        print(f'Soy el Barco {self.nombre} y estoy atracando')

    def avanzar(self):
        print(f'Soy el Barco {self.nombre} y estoy atracando')

seat_panda = Automovil('Seat Panda', 120, 4, 6.5)
seat_panda.arrancar() # Soy el Vehiculo Seat Panda y estoy arrancando
seat_panda.avanzar() # Soy el Vehiculo Seat Panda y estoy avanzando ;# Soy el Automovil Seat Panda y estoy avanzando