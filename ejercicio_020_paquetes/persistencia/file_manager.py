def guardar_normal(nombre_fichero, texto):
    fichero = open(nombre_fichero, mode='w', encoding='utf-8')
    fichero.write(texto)
    fichero.close()

def guardar_with(nombre_fichero, texto):
    with open(nombre_fichero, mode='w', encoding='utf-8') as fichero:
        fichero.write(texto)
        # El cierre del fichero se hace automáticamente

def leer_normal(nombre_fichero):
    fichero = open(nombre_fichero, mode='r', encoding='utf-8')
    texto = fichero.read()
    fichero.close()
    return texto

def leer_with(nombre_fichero):
    with open(nombre_fichero, mode='r', encoding='utf-8') as fichero:
        texto = fichero.read()
        # El cierre del fichero se hace automáticamente
    return texto






