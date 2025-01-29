import copy

class Factura:
    def __init__(self, identificador, importe, email, *productos):
        print('__init__')
        self.identificador = identificador
        self.importe = importe
        self.email = email
        self.productos = productos

    def __enviar(self):
        print('Enviando...')

    def __str__(self):
        print('__self__')
        return f'{self.identificador}-{self.importe}-{str(self.productos)}'

factura_01 = Factura('001', 1_000_000, 'fernando.paniagua@gmail.com', 'Pan', 'Vino', 'Huevos', 'Patatas', 'Cebolla')
print(factura_01)

factura_02 = factura_01 # *** Copia por referencia ***
print(factura_02)

factura_02.identificador = '002'
print(factura_01) # 002-1000000-('Pan', 'Vino', 'Huevos', 'Patatas', 'Cebolla')
print(factura_02) # 002-1000000-('Pan', 'Vino', 'Huevos', 'Patatas', 'Cebolla')

factura_03 = copy.deepcopy(factura_01) # *** Copia por valor ***
print(factura_01) # 002-1000000-('Pan', 'Vino', 'Huevos', 'Patatas', 'Cebolla')
print(factura_03) # 002-1000000-('Pan', 'Vino', 'Huevos', 'Patatas', 'Cebolla')

factura_03.identificador = '003'
factura_03.productos = list(factura_03.productos)
factura_03.productos[0] = 'Colines'
print(factura_01) # 002-1000000-('Pan', 'Vino', 'Huevos', 'Patatas', 'Cebolla')
print(factura_03) # 003-1000000-['Colines', 'Vino', 'Huevos', 'Patatas', 'Cebolla']