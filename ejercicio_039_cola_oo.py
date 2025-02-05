class LimiteExcedidoError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class Cola:
    def __init__(self, maxsize=0):
        self.__datos = []
        self.__maxsize = maxsize # Si es 0, el tamaño es 'infinito'

    def agregar(self, item : any):
        if (self.__maxsize>0 and len(self.__datos)==self.__maxsize):
            raise LimiteExcedidoError()
        self.__datos.append(item)
        print('Después de agregar:', self.__datos)

    def obtener(self) -> any:
        if (len(self.__datos)==0):
            raise IndexError('La cola está vacía')
        item = self.__datos.pop(0)
        print('Después de obtener:', self.__datos)
        return item
    
#mi_cola = Cola(maxsize=2)
mi_cola = Cola()
try:
    mi_cola.agregar('Tarea 1')
    mi_cola.agregar('Tarea 2')
    mi_cola.agregar('Tarea 3')
    item = mi_cola.obtener()
    print('Procesando:',item)
    item = mi_cola.obtener()
    print('Procesando:',item)
    item = mi_cola.obtener()
    print('Procesando:',item)
    item = mi_cola.obtener()
    print('Procesando:',item)
except LimiteExcedidoError:
    print('Has excedido el límite')
except IndexError as ie:
    print('Ha ocurrido un error:',ie)