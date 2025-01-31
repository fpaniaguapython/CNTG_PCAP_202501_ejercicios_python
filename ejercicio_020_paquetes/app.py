import persistencia.file_manager as fm 

if __name__=='__main__':
    #fm.guardar_seguro("fichero_seguro.txt", "texto de prueba")
    info = fm.leer_seguro("fichero_seguro.txt")
    print("Datos:",info)