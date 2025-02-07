# Opción 1
# Apertura con función
fichero = open('nombre_fichero.txt',mode='wt',encoding='utf-8')

# Cierre mediante método
fichero.close()

# Opción 2
# Alterantivamente, utilizando with el close se hace solo.

with open('nombre_fichero.txt', mode='wt', encoding='utf-8') as fichero:
    pass