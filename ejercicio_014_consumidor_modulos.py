""" 
import ejercicio_012_modulos
import ejercicio_013_modulos_bis

ejercicio_012_modulos.funcion_01()
ejercicio_012_modulos.funcion_02()
ejercicio_012_modulos.funcion_03()

ejercicio_013_modulos_bis.funcion_01()
"""


""" 
import ejercicio_012_modulos, ejercicio_013_modulos_bis

ejercicio_012_modulos.funcion_01()
ejercicio_012_modulos.funcion_02()
ejercicio_012_modulos.funcion_03()

ejercicio_013_modulos_bis.funcion_01() 
"""


""" 
import ejercicio_012_modulos as e12, ejercicio_013_modulos_bis as e13
e12.funcion_01()
e13.funcion_01() 
"""

# from ejercicio_012_modulos import * # No recomendado
# from ejercicio_013_modulos_bis import * # No recomendado

from ejercicio_012_modulos import funcion_01, funcion_03
from ejercicio_013_modulos_bis import funcion_01 as f_01, funcion_02

funcion_01()
f_01()
funcion_02()

