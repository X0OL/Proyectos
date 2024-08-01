import os
def opciones_archivos():
    while True:
            print("Selecciona una opción:")
            print("1. Buscar archivo y leerlo")
            print("2. Crear el archivo y guardarlo")
            print("3. Añadir textos")
            print("4. Sobreescribir")
            print("5. Salir")
            opcion = int(input("¿Qué quieres hacer? (1-3): "))  
            if opcion in [1,2,3,4,5]:
                return opcion
            else:
                print("")
opcion = opciones_archivos()   
while True:
    if opcion in [1]:
            RutaArchivo = input("Introduce qué archivo quieres buscar:")
            acceso = 'C:/Users/angel/OneDrive/Documentos/'+ RutaArchivo
    if opcion ==5:
          print("ADIOOOOOOOS")
          break
    elif opcion==1:
        if os.path.isfile(acceso):     
            try:
                    with open(acceso, 'r') as archivos:
                            texto = archivos.read()
                            print("El Archivo existe")
                            print(f"Aqui esta el texto de {RutaArchivo}:\n{texto}")
                            break
            except FileNotFoundError:
                        print("No se ah encontrado tu archivo")
                        break
    elif opcion==2:
        CreerArchivo= input("Nombre Del archivo para crearlo:")
        acceso = 'C:/Users/angel/OneDrive/Documentos/'
        ruta_archivo = os.path.join(acceso, CreerArchivo)
        try:
                        with open(ruta_archivo, 'x') as archivos:
                            texto= input("Introduce texto para el archivo: ")
                            archivos.write(texto)
                        print(f"El Archivo {CreerArchivo} con exito!!")
                        break
        except FileExistsError:
                        print("Un archivo ya tiene ese nombre")
                        break
    elif opcion==3:
        def obtener_opciones():
            while True:
                print("Selecciona una opción:")
                print("1. Añadir texto")
                print("2. Añadir texto en la siguiente línea")
                print("3. Salir")
                try:
                    opciones = int(input("¿Qué quieres hacer? (1-3): "))
                    if opciones in [1, 2, 3]:
                        return opcion
                    else:
                        print("Opción no válida. Por favor, selecciona un número del 1 al 3.")
                except ValueError:
                    print("Por favor, introduce un número válido.")

        while True:
            opciones_editar = obtener_opciones()
            if opciones_editar == 3:
                print("¡HASTA LA PROXIMAAAAA!")
                break
            elif opciones_editar in [1, 2]:
                Creer_Archivo = input("Nombre del archivo para crearlo: ")
                acceso = 'C:/Users/angel/OneDrive/Documentos/'
                ruta_Archivo = os.path.join(acceso, Creer_Archivo)
                try:
                    with open(ruta_Archivo, 'a') as archivoss:
                        textos = input("Introduce texto para el archivo: ")
                        if opciones_editar == 1:
                            archivoss.write(" " + textos)
                        elif opciones_editar == 2:
                            archivoss.write("\n" + textos)
                        print(f"¡El archivo {Creer_Archivo} se ha modificado con éxito!")
                except FileNotFoundError:
                    print("No se ha encontrado tu archivo.")
    elif opcion==4:
          CreerArchivo= input("Nombre Del archivo para crearlo:")
          acceso = 'C:/Users/angel/OneDrive/Documentos/'
          ruta_archivo = os.path.join(acceso, CreerArchivo)
          try:
                        with open(ruta_archivo, 'w') as archivos:
                            texto= input("Introduce texto para el archivo: ")
                            archivos.write(texto)
                        print(f"El Archivo {CreerArchivo} con exito!!")
                        break
          except FileExistsError:
                        print("Un archivo ya tiene ese nombre")
                        break