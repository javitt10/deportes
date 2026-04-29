import requests
import xml.etree.ElementTree as ET
import json
import re

def obtener_noticias():
    # Google News - Deportes México (Es una fuente que NO bloquea)
    rss_url = "https://google.com"
    noticias = []
    
    try:
        response = requests.get(rss_url, timeout=20)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        
        # Google News usa una estructura estándar
        for item in root.findall(".//item")[:10]:
            titulo = item.find("title").text
            link = item.find("link").text
            # Google News no siempre manda descripción, así que ponemos un texto base
            resumen = "Haz clic para leer la nota completa en la fuente original."
            
            noticias.append({
                "titulo": titulo,
                "resumen": resumen,
                "link": link
            })
            
    except Exception as e:
        print(f"Error: {e}")
        noticias = [{"titulo": "Actualizando...", "resumen": "Cargando noticias deportivas...", "link": "#"}]
    
    with open("noticias.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    obtener_noticias()
