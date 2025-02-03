class Automovil:
    def __init__(self, marca, modelo, precio, potencia):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.potencia = potencia

    def __repr__(self):
        return self.marca + ':' + self.modelo
    
    def __lt__(self, other): #Less than
        return self.precio - other.precio

seat = Automovil(marca='Seat', modelo='Ibiza', precio=18_000, potencia=140)
kia = Automovil(marca='Kia', modelo='Ceed', precio=17_000, potencia=100)
peugeot = Automovil('Peugeot', '205', 1_500, 90)

coches = [seat, kia, peugeot]

# Ordenar la lista por precio (utilizando __lt__)
print(sorted(coches, reverse=True))
