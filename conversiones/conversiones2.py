from PIL import Image
import os

def Convertir(ruta_original,ruta_destino):
    archivos = os.listdir(ruta_original)
    #print(archivos)

    for archivo in archivos:
        imagen = Image.open(ruta_original+archivo)

        alto_original = imagen.height
        ancho_orginal = imagen.width

        redim = imagen.resize((int(ancho_orginal/2),int(alto_original/2)))
        imagen.save(ruta_destino+archivo,quality=25)    

Convertir("original/","convertidos/")