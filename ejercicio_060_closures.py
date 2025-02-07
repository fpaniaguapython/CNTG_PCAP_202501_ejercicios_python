# Closures (cierre) Es una función que devuelve otra función
def funcion_externa(argumento=''):
    argumento = argumento.upper()
    
    def funcion_interna():
        return argumento

    return funcion_interna

nombre = 'Víctor'
funcion_interna_demorada = funcion_externa(nombre)
nombre = 'Gonzalo'
print('Función demorada:', funcion_interna_demorada()) # Función demorada: VÍCTOR
print('Nombre:', nombre) # Nombre: Gonzalo