from PIL import Image
import os
import time
import threading

def ConvertirUnico(ruta_original,ruta_destino,nombre_archivo):

    imagen = Image.open(ruta_original+nombre_archivo)

    alto_original = imagen.height
    ancho_orginal = imagen.width

    redim = imagen.resize((int(ancho_orginal/2),int(alto_original/2)))
    redim.save(ruta_destino+nombre_archivo,quality=75) 


def Convertir(ruta_original,ruta_destino):

    inicio = time.time()
    archivos = os.listdir(ruta_original)
    #print(archivos)

    HILOS = []

    for archivo in archivos:
        hilo = threading.Thread(target=ConvertirUnico,args=(ruta_original,ruta_destino,archivo,))
        hilo.start()
        HILOS.append(hilo)

    for el_hilo in HILOS:
        el_hilo.join()

    fin = time.time()
    tiempo_usado = fin-inicio
    print("Las coversiones han demorado ",tiempo_usado,"segundos.")

Convertir("original/","convertidos3/")