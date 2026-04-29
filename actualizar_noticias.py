import requests
import xml.etree.ElementTree as ET
import json
import re

def obtener_noticias():
    # URL del RSS de Marca México
        rss_url = "https://uecdn.es"
    try:
        response = requests.get(rss_url, timeout=15)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        
        noticias = []
        # Obtenemos las últimas 10 noticias
        for item in root.findall(".//item")[:10]:
            titulo = item.find("title").text if item.find("title") is not None else "Sin título"
            link = item.find("link").text if item.find("link") is not None else "#"
            desc_raw = item.find("description").text if item.find("description") is not None else ""
            
            # Limpiar etiquetas HTML del resumen
            resumen = re.sub('<[^<]+?>', '', desc_raw)[:150] + "..."
            
            noticias.append({
                "titulo": titulo,
                "resumen": resumen,
                "link": link
            })
        
        # Guardar en el archivo JSON
        with open("noticias.json", "w", encoding="utf-8") as f:
            json.dump(noticias, f, ensure_ascii=False, indent=2)
        print("Noticias actualizadas con éxito.")

    except Exception as e:
        print(f"Error al actualizar: {e}")

if __name__ == "__main__":
    obtener_noticias()
