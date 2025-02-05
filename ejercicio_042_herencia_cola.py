class Cola:
    def __init__(self):
        self.datos = []
        
    def agregar(self, item : int):
        self.datos.append(item)
        print('Después de agregar:', self.datos)

    def obtener(self) -> int:
        item = self.datos.pop(0)
        print('Después de obtener:', self.datos)
        return item
    
# Crear una clase ColaExtendida que hereda de Cola
# Incorpora un atributo que contiene la suma de los elementos de la estructura de datos

class ColaExtendida(Cola):
    def __init__(self):
        super().__init__()
        self.__contador = 0

    def agregar(self, item : int):#Sobreescritura del método
        super().agregar(item)
        self.__contador+=item

    def obtener(self) -> int:
        item = super().obtener()
        self.__contador-=item
        return item
    
    def get_contador(self):
        return self.__contador

mi_cola = ColaExtendida()    
mi_cola.agregar(3)
print(mi_cola.get_contador())
mi_cola.agregar(8)
print(mi_cola.get_contador())
mi_cola.agregar(10)
print(mi_cola.get_contador())
item = mi_cola.obtener()
print('Procesando:',item)
print(mi_cola.get_contador())
item = mi_cola.obtener()
print('Procesando:',item)
print(mi_cola.get_contador())