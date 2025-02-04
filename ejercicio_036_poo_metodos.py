class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def arrancar(self):
        print('Arrancando...')

motor_x10 = Motor(100)