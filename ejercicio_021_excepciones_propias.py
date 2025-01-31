class IgualesError(ValueError):
    def __init__(self, msg, s1, s2):
        super().__init__(msg)
        self.s1 = s1
        self.s2 = s2
    def accion_contingencia(self):
        print('Ejecuta la acción de contigencia...')


def sumar(s1, s2):
    if (s1==s2):
        raise IgualesError('No pueden ser iguales', s1, s2)
    return s1+s2


try:
    resultado = sumar(3,3)
    print(resultado)
except IgualesError as ve: # ve trae un código creado por nosotros
    ve.accion_contingencia()
    print(ve.s1, ve.s2)