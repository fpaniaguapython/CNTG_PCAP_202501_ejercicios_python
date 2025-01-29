# dict o diccionario, también conocido como:
# 'hash table', 'array asociativos' (en PHP), 'map' (en Java)

diccionario_vacio = {} # Es un diccionario no un SET
diccionario_vacio = dict()
info_python = { 'nombre' : 'Python', 'año' : 1991 }
info_java = dict([('nombre','Java'),('año',1990)])

agenda = { 'Fernando': 'fernando.paniagua@gmail.com', 'Anna' : 'anna.gomez@hotmail.com', 'Felipe' : 'fel.rom.384@gmail.com' }

# Acceso a un elemento
print(agenda['Anna']) # anna.gomez@hotmail.com
agenda['Anna'] = 'anna.gomez.rodriguez@hotmail.com'
print(agenda['Anna']) # anna.gomez.rodriguez@hotmail.com

print(agenda.get('Anna')) # anna.gomez.rodriguez@hotmail.com

# agenda['Iñigo'] # KeyError: 'Iñigo'
print(agenda.get('Iñigo')) # None

print(list(agenda)) # ['Fernando', 'Anna', 'Felipe']
print(list(agenda.values())) # ['fernando.paniagua@gmail.com', 'anna.gomez.rodriguez@hotmail.com', 'fel.rom.384@gmail.com']

for clave in agenda.keys():
    print(clave)

for valor in agenda.values():
    print(valor)

for clave, valor in agenda.items():
    print(clave, valor)

print('Fernanda' in agenda) # False
print('Fernanda' not in agenda) # True
print('fernando.paniagua@gmail.com' in agenda.values()) # True

# agenda.clear() # Borra el diccionario

agenda_vecino = {'Luisa':'luisa@hotmail.com'}
agenda.update(agenda_vecino) # Agrega los elementos de agenda_vecino a agenda
print(agenda) # {'Fernando': 'fernando.paniagua@gmail.com', 'Anna': 'anna.gomez.rodriguez@hotmail.com', 'Felipe': 'fel.rom.384@gmail.com', 'Luisa': 'luisa@hotmail.com'}

agenda.update(victor='victor@gmail.com', gonzalo='gonzalo@gmail.com') # Agrega los elementos
print(agenda) # {'Fernando': 'fernando.paniagua@gmail.com', 'Anna': 'anna.gomez.rodriguez@hotmail.com', 'Felipe': 'fel.rom.384@gmail.com', 'Luisa': 'luisa@hotmail.com', 'victor': 'victor@gmail.com', 'gonzalo': 'gonzalo@gmail.com'}

# Construcción de un diccionario a partir de dos iterables
sensores = ('Tejado','Ventana superior','Ventana inferior', 'Sotano')
temperaturas = (10, 12, 8, 3, 10)

dict_informacion_edificio = zip(sensores, temperaturas) # Si no tienen la misma longitud, descarta los excedentes
# dict_informacion_edificio = zip(sensores, temperaturas, strict=True) # Si no tienen la misma longitud, provoca error
print(dict(dict_informacion_edificio)) # {'Tejado': 10, 'Ventana superior': 12, 'Ventana inferior': 8, 'Sotano': 3}