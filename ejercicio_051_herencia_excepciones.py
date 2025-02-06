class MiException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

    def metodo_extra(self):
        print('Acción extra')

try:
    cadena = 'cosa'
    if (cadena=='cosa'):
        raise MiException('Texto del mensaje')
except MiException as me:
    print(me)
    me.metodo_extra()