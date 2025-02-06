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
    def accion_de_b(self):
        print('Soy B y estoy algo específico')

class C(A):
    def __init__(self):
        print('Constructor de C')
        super().__init__()
    def saludar(self):
        print('Soy C y estoy saludando')
    def accion_de_c(self):
        print('Soy C y estoy algo específico')

class D(B,C):
    def __init__(self):
        print('Constructor de D')
        super().__init__()
    def saludar(self):
        print('Soy D y estoy saludando')
    
#MRO (Orden de Resolución de Métodos)

d = D()
# Constructor de D
# Constructor de B
# Constructor de C
# Constructor de A

d.saludar() # Ejecutará en orden aparición D, B, C o A