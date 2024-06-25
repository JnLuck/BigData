# Importamos las dependencias
import requests
from bs4 import BeautifulSoup

import os
import shutil
from datetime import datetime
# Importamos las dependencias para exportar csv
import codecs # Para manekar la codificación (utf-8) y escribir el archivo csv
import csv 


# Creamos las variables
url = 'https://diariosinfronteras.com.pe/category/puno/'
response = requests.get(url)

# Creamos un Objeto BeatufulSop para obtener el contenido
html = BeautifulSoup(response.text, 'html.parser')
secciones = html.find_all('li', class_='infinite-post')
print(secciones)

# Nos movemos sobre las secciones para obtener la información
for seccion in secciones: #* Iteramos sobre las secciones extraídas
    # Obtenemos el enlace de la noticia 
    enlace = seccion.find('a')['href']
    # Obtenemos la fecha de la noticia a partir del enlace usando expresiones regulares
    fecha_str = "/".join(enlace.split('/')[3:6])
    # Convertimos la fecha a un objeto datetime
    fecha = datetime.strptime(fecha_str, '%Y/%m/%d')
    # Formateamos la fecha
    fecha_formateada = fecha.strftime('%d/%B/%Y')  # Cambiamos el formato de la fecha
    # Imprimimos la fecha
    print("Fecha: " + fecha_formateada)
    # Obtenemos el título de la noticia
    titulo = seccion.find('h2').text
    # Imprimimos el título
    print("Titulo: " + titulo)
    # Obtenemos el resumen de la noticia
    resumen = seccion.find('p').text
    # Imprimimos el resumen
    print("Resumen: " + resumen)
    print('--------------------------------------')


# Creamos el archivo CSV
with codecs.open('noticias_sf.csv', 'w', 'utf-8-sig') as csvfile:
    writer = csv.writer(csvfile, delimiter='|')
    writer.writerow(['Fecha', 'Título', 'Resumen'])  # Escribimos los encabezados

    # Iteramos sobre las secciones para obtener la información
    for seccion in secciones:
        # Obtenemos la información de la sección
        enlace = seccion.find('a')['href']
        fecha_str = "/".join(enlace.split('/')[3:6])
        fecha = datetime.strptime(fecha_str, '%Y/%m/%d')
        fecha_formateada = fecha.strftime('%d/%B/%Y')
        titulo = seccion.find('h2').text
        resumen = seccion.find('p').text

        # Escribimos los datos en el archivo CSV
        writer.writerow([fecha_formateada, titulo, resumen])