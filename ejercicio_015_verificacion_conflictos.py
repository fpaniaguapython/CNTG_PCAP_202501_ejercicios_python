# Disponemos de dos módulos ejercicio_012_modulos.py y 
# ejercicio_013_modulos_bis.py

# Averiguar si hay conflictos entre los módulos
# utilizando dir y los métodos propios de set (conjunto)

import ejercicio_012_modulos as e12
import ejercicio_013_modulos_bis as e13

entidades_e12 = set(dir(e12))
entidades_e13 = set(dir(e13))

if entidades_e12.isdisjoint(entidades_e13):
    print("OK")
else:
    print("HAY CONFLICTO")

if len(entidades_e12.intersection(entidades_e13))>0:
    print("HAY CONFLICTO")
else:
    print("OK")