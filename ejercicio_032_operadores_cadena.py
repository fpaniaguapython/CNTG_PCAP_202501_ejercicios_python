# Se pueden utilizar operadores de comparación con las cadenas: puntos de código

print('Albacete'>'zamora') # False
print('albacete'>'Zamora') # True
print('cosa'>'cosax') # False (porque cosax tienes más caracteres)
# print('cosa'>3) # TypeError

# Operadores de igualdad == y !=
print('cadena'==3) # False
print('3'==3) # False
print('cadena'==True) # False
print('cadena'==['cadena','i2']) # False
print('cadena'==None) # False
print('cadena'=={'nombre':'Python','autor':'Guido'}) # False