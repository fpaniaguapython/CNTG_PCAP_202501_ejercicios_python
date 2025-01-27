ciudad_nacimiento = 'Madrid' #snakecase
nombre = 'Fernando'
edad = 53

# Fernando nació en Madrid hace 53 años

print(nombre + ' nació en ' + ciudad_nacimiento + ' hace ' + str(edad) + ' años') 
print(f'{nombre} nació en {ciudad_nacimiento} hace {edad} años') #f-string
cadena = '{} nacio en {} hace {} años'.format(nombre, ciudad_nacimiento, edad)
print(cadena)