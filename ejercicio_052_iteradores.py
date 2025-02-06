class ItemFacturable:
    def __init__(self, importe):
        self.importe = importe

class Factura:
    def __init__(self, items_facturables):
        self.items_facturables = items_facturables

    def __iter__(self):
        print('__iter__') # Sólo una vez
        self.__indice=-1
        return self

    def __next__(self):
        print('__next__') # Una vez por cada iteracción
        self.__indice+=1
        if (self.__indice==len(self.items_facturables)):
            raise StopIteration()
        return self.items_facturables[self.__indice]

i1 = ItemFacturable(10)
i2 = ItemFacturable(-5)
i3 = ItemFacturable(20)
i4 = ItemFacturable(-8)
i5 = ItemFacturable(120)

items_facturables = [i1, i2, i3, i4, i5]
factura = Factura(items_facturables)

for item in factura:
    print(item.importe)

for item in factura:
    print(item.importe)