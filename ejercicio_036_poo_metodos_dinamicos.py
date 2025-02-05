class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def arrancar(self):
        print('Arrancando...')

motor_x10 = Motor(100)

# Añadiendo un método de instancia
def f_parar(self):
    print('Parando...', self.potencia)

motor_x10.parar = f_parar.__get__(motor_x10)
motor_x10.parar()

# Añadiendo un método 'estático'
def f_acelerar():
    print('Acelerando...') # No tenemos refencia a self

motor_x10.acelerar = f_acelerar
motor_x10.acelerar()