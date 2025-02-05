class Impresora:
    numero_paginas_totales = 0 # Atributo de CLASE

    def __init__(self, nombre):
        self.numero_paginas_impresas = 0 # Atributo de INSTANCIA
        self.nombre = nombre # Atributo de INSTANCIA

    def imprimir(self, numero_paginas):
        print('Imprimiendo:',numero_paginas,'páginas')
        self.numero_paginas_impresas+=numero_paginas
        Impresora.numero_paginas_totales+=numero_paginas # Accede a través del nombre de la clase

    def mostrar_numero_paginas_impresas(self):
        print(f'Soy {self.nombre} y he impreso {self.numero_paginas_impresas} páginas')

epson = Impresora('Epson')
hp = Impresora('HP')

epson.imprimir(8)
epson.imprimir(10)
epson.imprimir(2)

hp.imprimir(78)
hp.imprimir(2)

epson.mostrar_numero_paginas_impresas()
hp.mostrar_numero_paginas_impresas()

print(Impresora.numero_paginas_totales)