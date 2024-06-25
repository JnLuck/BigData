import requests
from bs4 import BeautifulSoup
import re

url = 'https://diariosinfronteras.com.pe/category/puno/'
response = requests.get(url)

html = BeautifulSoup(response.content, 'html.parser')

secciones = html.find_all("li", class_="infinite-post")

for seccion in secciones:
    enlace_noticia = seccion.find("a", href=True)
    titulo = seccion.find("h2")
    descripcion = seccion.find("p")
    
    if enlace_noticia and titulo and descripcion:
        # Extracción de la fecha de la URL
        fecha_match = re.search(r'/(\d{4}/\d{2}/\d{2})/', enlace_noticia['href'])
        fecha = fecha_match.group(1) if fecha_match else "Fecha no disponible"
        
        print(f"Fecha: {fecha}")
        print(f"Título: {titulo.text.strip()}")
        print(f"Descripción: {descripcion.text.strip()}")
        print("-----")

