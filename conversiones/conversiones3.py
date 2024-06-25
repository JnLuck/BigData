from PIL import Image
import os
import time

def Convertir(ruta_original,ruta_destino):

    inicio = time.time()
    archivos = os.listdir(ruta_original)
    #print(archivos)

    for archivo in archivos:
        imagen = Image.open(ruta_original+archivo)

        alto_original = imagen.height
        ancho_orginal = imagen.width

        redim = imagen.resize((int(ancho_orginal/2),int(alto_original/2)))
        redim.save(ruta_destino+archivo,quality=75) 

    fin = time.time()
    tiempo_usado = fin-inicio
    print("Las coversiones han demorado ",tiempo_usado,"segundos.")

Convertir("original/","convertidos2/")