from PIL import Image
import os

def Convertir(ruta_original,ruta_destino):
    archivos = os.listdir(ruta_original)
    #print(archivos)

    for archivo in archivos:
        imagen = Image.open(ruta_original+archivo)
        imagen.save(ruta_destino+archivo,quality=10)    

Convertir("original/","convertidos/")