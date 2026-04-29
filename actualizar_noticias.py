import os 
import requests
import json

def obtener_noticias():
    # El código toma la llave de la "caja fuerte" de GitHub
    api_key = os.getenv("NEWS_API_KEY") 
    
    url = f"https://newsapi.org{api_key}"
    
    
    noticias = []
    try:
        response = requests.get(api_url, timeout=20)
        data = response.json()
        
        if data.get('status') == 'ok':
            for article in data.get('articles', [])[:10]:
                noticias.append({
                    "titulo": article['title'],
                    "resumen": article['description'] if article['description'] else "Click para leer más...",
                    "link": article['url']
                })
        else:
            print("Error de la API:", data.get('message'))
            
    except Exception as e:
        print(f"Error de conexión: {e}")
        # Noticias de respaldo si la API falla
        noticias = [{"titulo": "Sincronizando noticias locales...", "resumen": "Refrescando titulares deportivos de México.", "link": "#"}]
    
    # Guardamos en tu noticias.json
    with open("noticias.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    obtener_noticias_mexico()
