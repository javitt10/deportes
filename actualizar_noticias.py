import os
import requests
import json

def obtener_noticias():
    # 1. Obtenemos la API Key desde la 'caja fuerte' de GitHub
    api_key = os.getenv("NEWS_API_KEY")
    
    # 2. Configuramos la URL para México (mx), Deportes (sports) y en Español (es)
    url = f"https://newsapi.org{api_key}"
    
    noticias = []
    
    try:
        # 3. Hacemos la petición a la API profesional
        print("Conectando con NewsAPI...")
        response = requests.get(url, timeout=20)
        data = response.json()
        
        if data.get('status') == 'ok':
            articulos = data.get('articles', [])
            
            if not articulos:
                print("No se encontraron noticias en este momento.")
                # Datos de relleno por si la API no tiene noticias hoy
                noticias = [{"titulo": "Sin noticias nuevas", "resumen": "Refrescando titulares...", "link": "#"}]
            else:
                # Tomamos las primeras 10 noticias
                for article in articulos[:10]:
                    noticias.append({
                        "titulo": article['title'],
                        "resumen": article['description'] if article['description'] else "Click para ver detalles.",
                        "link": article['url']
                    })
                print(f"Se obtuvieron {len(noticias)} noticias exitosamente.")
        else:
            print(f"Error de la API: {data.get('message')}")
            raise Exception("API Error")
            
    except Exception as e:
        print(f"Hubo un problema: {e}")
        # Mantenemos noticias de respaldo para que tu web nunca falle
        noticias = [
            {"titulo": "LIGA MX: Actualización en proceso", "resumen": "Sincronizando con los servidores de México...", "link": "#"},
            {"titulo": "F1: Novedades de Checo Pérez", "resumen": "Toda la información del piloto mexicano.", "link": "#"}
        ]
    
    # 4. Guardamos el archivo final
    with open("noticias.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=2)
    print("Archivo noticias.json actualizado.")

if __name__ == "__main__":
    obtener_noticias()
