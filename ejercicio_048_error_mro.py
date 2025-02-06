class A:
    def __init__(self):
        print('Constructor de A')
    def saludar(self):
        print('Soy A y estoy saludando')

class B(A):
    def __init__(self):
        print('Constructor de B')
        super().__init__()
    def saludar(self):
        print('Soy B y estoy saludando')

class D(A,B):# El error se produce si primero se hereda de la superclase de la que hereda la otra clase
    def __init__(self):
        print('Constructor de D')
        super().__init__()
    def saludar(self):
        print('Soy D y estoy saludando')
    
#MRO (Orden de Resolución de Métodos)

d = D() # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B



