import requests
import xml.etree.ElementTree as ET
import json
import re

def obtener_noticias():
    rss_url = "https://nasa.gov"
    noticias = []
    
    try:
        # Intentamos obtener noticias de Marca
        response = requests.get(rss_url, timeout=15)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        
        for item in root.findall(".//item")[:10]:
            titulo = item.find("title").text if item.find("title") is not None else "Sin título"
            link = item.find("link").text if item.find("link") is not None else "#"
            desc_raw = item.find("description").text if item.find("description") is not None else ""
            resumen = re.sub('<[^<]+?>', '', desc_raw)[:150] + "..."
            
            noticias.append({"titulo": titulo, "resumen": resumen, "link": link})
            
    except Exception as e:
        print(f"Error al conectar con Marca: {e}")
        # Si Marca falla, creamos noticias de respaldo para que el archivo NO esté vacío
        noticias = [
            {"titulo": "Servicio temporalmente en actualización", "resumen": "Estamos refrescando los datos deportivos...", "link": "#"},
            {"titulo": "Revisa más tarde", "resumen": "Las noticias de Marca MX volverán pronto.", "link": "#"}
        ]
    
    # ESTA PARTE ES CRUCIAL: Guarda el archivo sí o sí
    with open("noticias.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=2)
    print("Archivo noticias.json generado correctamente.")

if __name__ == "__main__":
    obtener_noticias()
