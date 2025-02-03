class Automovil:
    def __init__(self, marca, modelo, precio, potencia):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.potencia = potencia


seat = Automovil(marca='Seat', modelo='Ibiza', precio=18_000, potencia=140)
kia = Automovil(marca='Kia', modelo='Ceed', precio=17_000, potencia=100)
peugeot = Automovil('Peugeot', '205', 1_500, 90)

coches = [seat, kia, peugeot]

# Ordenar la lista por precio (Xabi utilizando lambdas)