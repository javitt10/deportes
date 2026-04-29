import os
import requests
import json

def obtener_noticias():
    api_key = os.getenv("NEWS_API_KEY")
    # URL para NewsData: México, Deportes, Español
    url = f"https://newsdata.io{api_key}&country=mx&category=sports&language=es"
    
    noticias = []
    try:
        response = requests.get(url, timeout=20)
        data = response.json()
        
        if data.get('status') == 'success':
            for article in data.get('results', [])[:10]:
                noticias.append({
                    "titulo": article['title'],
                    "resumen": article['description'][:150] + "..." if article['description'] else "Click para ver más",
                    "link": article['link']
                })
        else:
            raise Exception(f"API Error: {data.get('results')}")
            
    except Exception as e:
        print(f"Error: {e}")
        noticias = [{"titulo": "LIGA MX: Preparativos jornada", "resumen": "Sincronizando datos...", "link": "#"}]
    
    with open("noticias.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    obtener_noticias()
