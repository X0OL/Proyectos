import os
#r= lectura
#a= agregar y si no hay crea
#w= escritura
#x= crear
def opciones_archivos():
    while True:
            print("Selecciona una opción:")
            print("1. Crear un archivo (x)")
            print("2. Leer un archivo (r)")
            print("3. Editar un archivo (w)")
            print("4. Agregar un archivo (a) ")
            print("5. Eliminar Archivo ")
            print("6. Salir")
            opcion = int(input("¿Qué quieres hacer? (1-6): "))  
            if opcion in [1, 2, 3, 4,5,6]:
                return opcion
            else:
                print("Opción no válida. Por favor, selecciona un número del 1 al 4.")
opcion = opciones_archivos()   
while True:
    if opcion in [1, 2, 3, 4]:
            NombreCrear= input("Ingrese el archivo con terminación .txt: ")
    elif opcion ==6:
        print("HASTA LA PROXIMAAAAA")
        break
    elif opcion == 1:
                    try:
                        with open(NombreCrear, 'x') as archivos:
                            texto= input("Introduce texto para el archivo: ")
                            archivos.write(texto)
                        print(f"El Archivo {NombreCrear} con exito!!")
                    except FileExistsError:
                        print("Un archivo ya tiene ese nombre")
                    break
    elif opcion == 2:
                    try:
                        with open(NombreCrear, 'r') as archivos:
                            texto = archivos.read()
                        print(f"Aqui esta el texto de {NombreCrear}:\n {texto}")
                    except FileNotFoundError:
                        print("No se ah encontrado tu archivo")
                    break
    elif opcion ==3: 
                    try:
                        with open(NombreCrear, 'w') as archivos:
                            texto= input("Introduce texto para el archivo: ")
                            archivos.write(texto)
                        print(f"El archivo {NombreCrear} se ah modificado con exito!!")
                    except FileNotFoundError:
                        print("No se ah encontrado tu archivo")
                    break
    elif opcion ==4:
                    try:
                        with open(NombreCrear, 'a') as archivos:
                            texto= input("Introduce texto para el archivo: ")
                        archivos.write(texto)
                        print(f"El Archivo {NombreCrear} con exito!!")
                    except FileExistsError:
                        print("Un archivo ya tiene ese nombre")
                    break
    elif opcion ==5:
                    try:
                        Archivo= input("Que archivo deseas eliminar, escribelo con terminacion .txt: ")
                        os.remove(Archivo)
                        print(f"El archivo {Archivo}, se borro con exito")
                        break
                    except FileNotFoundError:
                          print("El archivo no existe")
                    continue 