class Vehiculo:
    pass

class Automovil(Vehiculo):
    pass

class AutomovilElectrico(Automovil):
    pass

ae = AutomovilElectrico()

# función built-in isinstance, nos dice si un objeto es instancia de una clase
print(isinstance(ae, AutomovilElectrico)) # True
print(isinstance(ae, Automovil)) # True
print(isinstance(ae, Vehiculo)) # True
print(isinstance(ae, object)) # True

# función built-in issubclass, nos dice si un x es subclase de una clase
print(issubclass(AutomovilElectrico, Automovil)) # True
print(issubclass(AutomovilElectrico, Vehiculo)) # True
print(issubclass(AutomovilElectrico, object)) # True