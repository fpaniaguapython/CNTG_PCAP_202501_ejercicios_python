def realizar_tarea_01():
    print("Realizando tarea 01...")

def realizar_tarea_02():
    print("Realizando tarea 02...")

def realizar_tarea_03():
    print("Realizando tarea 03...")

def ejecutador_tareas(tarea): # Recibe una función como argumento y la ejecuta
    tarea() 

t1 = realizar_tarea_01
t1() # Realizando tarea 01...

t2 = realizar_tarea_02
ejecutador_tareas(t2) # Realizando tarea 02...

t3 = realizar_tarea_03

# Crear una ¿lista o tupla? que contenga una relación de tareas de tipo t1, t2, t3
# y ejecutarlas de manera secuencial

print("*** Motor de ejecución ***")
tareas = (t1, t2, t3, t2, t3, t1)
for tarea in tareas:
    # tarea() # Opción 1
    ejecutador_tareas(tarea) # Opción 2