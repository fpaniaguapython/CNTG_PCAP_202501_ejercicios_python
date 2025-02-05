class Persona(object):
    def __init__(self, nombre, masa):
        self.nombre = nombre
        self.masa = masa
        self.__imc = 34
    def saludar(self):
        print(f'Hola, soy {self.nombre}')
    def __calcular(self):
        print('Estoy calculando...')

class Profesor(Persona):
    def __init__(self, nombre, masa, centro_formacion, asignaturas):
        super().__init__(nombre, masa)
        self.centro_formacion = centro_formacion
        self.asignaturas = asignaturas

    def hacer_algo(self):
        print(self.nombre)
        print(self.masa)
        # print(self.__imc) # Error, no es visible
        self.saludar()
        # self.__calcular() #Error, no es visible

victor = Persona('Víctor Álvarez', 80)
xabi = Profesor('Xabier Ferreiro', 85, 'San Clemente', ['PSP', 'LM']) 

xabi.hacer_algo()