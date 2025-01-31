def sumar(s1, s2):
    if (type(s1)!=int or not isinstance(s2, int)):
        raise TypeError('Los argumentos deben ser números enteros')
    if (s1<0 or s2<0):
        # raise Exception("Error") # Es mejor ser más específico
        raise ValueError("Los argumentos no pueden ser negativos")
    resultado = s1 + s2
    return resultado

# Except sin captura del objeto de error
try:
    resultado = sumar(-3,4)
    print('****', resultado)
except:
    print("1. Ha ocurrido un error")

# Except con filtro sin captura del objeto de error
try:
    resultado = sumar(-3,4)
    print('****', resultado)
except Exception:
    print("2. Ha ocurrido un error de tipo Exception")

# Except con filtro con captura del objeto (de alto nivel) de error
try:
    resultado = sumar(-3,4)
    print('****', resultado)
except Exception as objeto_con_la_exception:
    print('3.', objeto_con_la_exception)

# Except con filtro con captura del objeto (de bajo nivel) de error
try:
    resultado = sumar(-3,4)
    print('****', resultado)
except TypeError as te:
    print('4.', te)
except ValueError as ve:
    print('5.', ve)

# Except con filtro con captura del objeto (de bajo nivel) de error, y captura de nivel superior
try:
    resultado = sumar(-3,4)
    print('****', resultado)
except TypeError as te:
    print('6.', te)
except ValueError as ve:
    print('7.', ve)
except Exception as e:
    print('8.', e)
except BaseException as be:
    print('9.', be)

# Except con filtro con captura del objeto (de bajo nivel) de error, y captura de nivel superior
try:
    resultado = sumar(-3,4)
    print('****', resultado)
except (TypeError, ValueError) as tve: # De tipo TypeError o ValueError
    print('10.',tve)
except Exception as e:
    print('11.', e)
except BaseException as be:
    print('12.', be)

# Except con filtro con captura del objeto (de bajo nivel) de error, y captura de nivel superior
try:
    resultado = sumar(3,4)
    print('****', resultado) # Solo se ejecuta si la línea anterior no da error 
except (TypeError, ValueError) as tve: # De tipo TypeError o ValueError
    print('13.', tve)
except Exception as e:
    print('14.', e)
except BaseException as be:
    print('15.', be)
finally:
    print("16. Este código se ejecuta SIEMPRE (tanto si hay error como si no)")


# Except con filtro con captura del objeto (de bajo nivel) de error, y captura de nivel superior
try:
    resultado = sumar(-3,4)
    print('****', resultado) # Solo se ejecuta si la línea anterior no da error 
except (TypeError, ValueError) as tve: # De tipo TypeError o ValueError
    print('17.', tve)
except Exception as e:
    print('18.', e)
except BaseException as be:
    print('19.', be)
else:
    print("20. Este código se ejecuta SI NO HA HABIDO UN ERROR")
finally:
    print("21. Este código se ejecuta SIEMPRE (tanto si hay error como si no)")