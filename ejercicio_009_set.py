frutas_verano = {'Sandía', 'Melón', 'Uva','Sandía'}
frutas_invierno = set(['Naranja','Piña','Naranja','Uva'])
print(type(frutas_verano)) # <class 'set'>

print(frutas_verano) # {'Uva', 'Sandía', 'Melón'} # No hay orden, elimina duplicados

frutas_verano.add('Ciruela') # Añadir elementos
print(frutas_verano) # {'Sandía', 'Ciruela', 'Melón', 'Uva'}

frutas_verano.remove('Ciruela') # Eliminar elementos
print(frutas_verano) # {'Sandía', 'Melón', 'Uva'}

# fruta = frutas_verano.pop() # Devuelve el 'primer' elemento y lo elimina
# print(fruta) # Melón (depende)
# print(frutas_verano) # {'Sandía', 'Uva'} (depende)

frutas_verano_invierno = frutas_verano.intersection(frutas_invierno)
print(type(frutas_verano_invierno)) # <class 'set'>
print(frutas_verano_invierno) # {'Uva'}

frutas_primavera = {'Uva', 'Sandía'}
# Intersección múltiple utilizando 'method chaining'
frutas_multiples = frutas_verano.intersection(frutas_invierno).intersection(frutas_primavera)
print(frutas_multiples) # {'Uva'}

# Intersección múltiple aprovechando el API
frutas_multiples = frutas_verano.intersection(frutas_invierno, frutas_primavera)
print(frutas_multiples) # {'Uva'}

for fruta in frutas_primavera:
    print(fruta)

print('Piña' in frutas_primavera) # False
print('Piña' in frutas_invierno) # True