import requests
import xml.etree.ElementTree as ET
import json
import re

def obtener_noticias():
    # Fuente estable: BBC Mundo Deportes
    rss_url = "https://bbci.co.uk"
    noticias = []
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(rss_url, headers=headers, timeout=20)
        response.raise_for_status()
        
        # Usamos una forma más flexible de leer el XML
        content = response.content
        root = ET.fromstring(content)
        
        # Buscamos los elementos 'item'
        items = root.findall(".//item")
        
        for item in items[:10]:
            titulo = item.find("title").text if item.find("title") is not None else "Sin título"
            link = item.find("link").text if item.find("link") is not None else "#"
            desc = item.find("description").text if item.find("description") is not None else ""
            
            # Limpiamos el texto
            resumen = re.sub('<[^<]+?>', '', desc)[:120] + "..."
            
            noticias.append({
                "titulo": titulo,
                "resumen": resumen,
                "link": link
            })

        if not noticias:
            raise ValueError("Archivo vacío o sin noticias")

    except Exception as e:
        print(f"Error: {e}")
        noticias = [{"titulo": "Actualizando titulares...", "resumen": "Refrescando conexión con el servidor deportivo.", "link": "#"}]
    
    with open("noticias.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    obtener_noticias()
