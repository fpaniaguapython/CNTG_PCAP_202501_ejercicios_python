def comprobar_ventana_1():
    print('Comprobando ventana 1')
    return False

def comprobar_ventana_2():
    print('Comprobando ventana 2')
    return True

todas_ventanas_abiertas = comprobar_ventana_1() and comprobar_ventana_2() # Opera en modo cortocircuito
print(todas_ventanas_abiertas)

todas_ventanas_abiertas = comprobar_ventana_1() & comprobar_ventana_2() # Evalúa los dos lados de la expresión
print(todas_ventanas_abiertas)

alguna_ventana_abierta = comprobar_ventana_2() or comprobar_ventana_1() # Opera en modo cortocircuito
print(alguna_ventana_abierta)

alguna_ventana_abierta = comprobar_ventana_2() | comprobar_ventana_1() # Evalúa los dos lados de la expresión
print(alguna_ventana_abierta)

solo_una_ventana_abierta = comprobar_ventana_1() ^ comprobar_ventana_2() # xor - Sólo es True si está abierta únicamente una ventana
print(solo_una_ventana_abierta)