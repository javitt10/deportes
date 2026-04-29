import requests
import xml.etree.ElementTree as ET
import json
import re

def obtener_noticias():
    # Usaremos ESPN México por ser muy estable
    rss_url = "https://espn.com.mx"
    noticias = []
    
    # Este es el "disfraz" para que el sitio crea que eres una persona
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Hacemos la petición con los headers
        response = requests.get(rss_url, headers=headers, timeout=20)
        response.raise_for_status()
        
        # Procesamos el XML
        root = ET.fromstring(response.content)
        for item in root.findall(".//item")[:10]:
            titulo = item.find("title").text if item.find("title") is not None else "Sin título"
            link = item.find("link").text if item.find("link") is not None else "#"
            
            # Limpiamos el resumen de etiquetas HTML
            desc_raw = item.find("description").text if item.find("description") is not None else ""
            resumen = re.sub('<[^<]+?>', '', desc_raw)[:150] + "..."
            
            noticias.append({"titulo": titulo, "resumen": resumen, "link": link})

        if not noticias:
            raise ValueError("No se encontraron noticias en el archivo")

    except Exception as e:
        # Si algo falla, este mensaje se guarda en el JSON
        print(f"Error detectado: {e}")
        noticias = [{"titulo": f"Error técnico: {str(e)[:40]}", "resumen": "Refrescando conexión...", "link": "#"}]
    
    # Guardamos el archivo noticias.json
    with open("noticias.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    obtener_noticias()
