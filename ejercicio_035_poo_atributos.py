class Impresora:
    def __init__(self, marca, ppm):
        self.marca = marca
        self.ppm = ppm
        self.__estado = 'Encendida' # Atributo 'privado'

    def apagar_impresora(self):
        if (self.__estado=='Encendida'):
            self.__estado = 'Apagada'
        else:
            raise Exception('La impresora ya está apagada')

epson = Impresora('Epson', 10)
hp = Impresora('HP', 100)

print(epson.ppm) # 10 Acceso de lectura a un atributo
epson.ppm = 20 # Acceso de escritura a un atributo
# print(epson.__estado) # AttributeError, ha sido reemplazado por _Impresora__estado
# print(epson._Impresora__estado) # Encendida (no debemos acceder al atributo 'privado')
epson.apagar_impresora()

hp.precio_cartucho = 50 # Añadiendo un atributo a un objeto
print(hp.precio_cartucho)
# print(epson.precio_cartucho) # AttributeError
del hp.precio_cartucho # Eliminación de un atributo
# print(hp.precio_cartucho) # AttributeError
delattr(hp, 'ppm') # Otra alternativa al borrado de atributos
# hp.__estado = 'Activo' # OJO, Crea un atributo __estado

print(dir(hp)) # Pasando un objeto a la función dir, devuelve una lista con todos los atributos de instancia del objeto 