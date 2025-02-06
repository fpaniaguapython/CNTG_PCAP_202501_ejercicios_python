class Serie:
    '''
    Información sobre la clase Serie
    '''
    numero_series = 10
    def __init__(self, titulo, temporadas):
        self.titulo = titulo
        self.temporadas = temporadas
    
    def mostrar_info(self):
        pass

secret_level = Serie('Secret Level', 1) 

print(secret_level.__dict__) # __dict__ proporciona un dict con los atributos de INSTANCIA
print(Serie.__dict__) #__dict__ proporciona un dict con los atributos de CLASE

print(hasattr(secret_level, 'temporadas')) # True
print(hasattr(secret_level, 'numero_series')) # True
print(hasattr(Serie, 'temporadas')) # False
print(hasattr(Serie, 'numero_series')) # True

'''
__dict__ -> Muestra información de los atributos (Tanto a clase como a objeto)
__name__ -> Contiene el nombre de la clase (Sólo se aplica a la clase)
__module__ -> Contiene el nombrel módulo (Tanto a clase como a objeto)
__bases__ -> Contiene la relación de clases de las que se está heredando DIRECTAMENTE
'''
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

o = D()

print(D.__bases__) # (<class '__main__.B'>, <class '__main__.C'>)
print(B.__bases__) # (<class '__main__.A'>,)
print(A.__bases__) # (<class 'object'>,)
# print(o.__bases__) # Error (__bases__ solo está disponible en las clases)

# Funciones built-in de acceso a atributos
print(getattr(secret_level, 'titulo')) # Función para obtener el valor de un atributo.
setattr(secret_level,'titulo','Rambo') # Función para asignar un valor a un atributo
setattr(secret_level,'duracion',15) # Función para asignar un nuevo atributo con su valor inicial