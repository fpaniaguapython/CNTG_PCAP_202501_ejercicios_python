# Composición es una construcción en la que un objeto de una clase tiene referencias
# a objetos de otra clase, dando así acceso a su funcionalidad

class Motor:
    def arrancar(self):
        print('Arrancando...')

class Vehiculo():
    def __init__(self, marca, modelo, motor : Motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

m = Motor()
v = Vehiculo('Seat','Panda', m)
v.motor.arrancar()