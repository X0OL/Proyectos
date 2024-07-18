                                                                                                
datos_usuario = int(input("Ingresa cuántas cantidades quieres: "))
suma = 0
i = 1
numeros = []

while i <= datos_usuario:
    print(f"Ingresa la calificación {i}:")
    numero_usurio = float(input())
    suma += numero_usurio
    numeros.append(numero_usurio)
    i += 1

#Aqui calculamos la media
media = suma / datos_usuario

#Aqui calculamos lo que es la deaviacion media 
desviacion_media = sum(abs(numero - media) for numero in numeros) / datos_usuario

#Aqui calculamos sacamos el resultado al cuadrado de la desviacion media
cuadrados_desviacion = [(numero - media) ** 2 for numero in numeros]

#Aqui sacamos lo que es la varianza ya una vez calculada las desviaciones medias al cuadrado
varianza = sum(cuadrados_desviacion) / datos_usuario

#Aqui mostramos lo que es los resultado de los numeros solicitados
print(f"Tus números ingresados son: {numeros}")

#Imprimimos el resultado de media
print(f"La media es: {media}")

#Imprimimos el resultado de varianza
print(f"La varianza es: {varianza}")

#Esta parte lo que hace es mostrar las desviaciones medias que se elevaron al cuadrado de cada numero ingresado
desviaciones_individuales = [(numero - media) ** 2 for numero in numeros]
print(f"Las desviaciones individuales son: {desviaciones_individuales}")

#Aqui imprimimos lo que es el resultado de la desviacion media
print(f"La desviación media es: {desviacion_media}")