class Motor():
    def arrancar(self):
        print('Estoy arrancando')

def arrancar_motor(motor : Motor):
    if isinstance(motor, Motor):
        motor.arrancar()
    else:
        raise Exception('No se ha proporcionado una instancia de Motor')

# motor = 'Lechuga'
motor = Motor()
try:
    arrancar_motor(motor)
except Exception as e:
    print(e)

