import requests
import json

def obtener_noticias():
    # Usamos un convertidor que ya tiene permisos globales
    rss_original = "https://bbci.co.uk"
    api_url = f"https://rss2json.com{rss_original}"
    
    noticias = []
    
    try:
        response = requests.get(api_url, timeout=20)
        data = response.json()
        
        if data['status'] == 'ok':
            for item in data['items'][:10]:
                noticias.append({
                    "titulo": item['title'],
                    "resumen": item['description'][:120] + "...",
                    "link": item['link']
                })
        else:
            raise Exception("API respondió con error")

    except Exception as e:
        print(f"Error: {e}")
        noticias = [{"titulo": "Actualizando portal deportivo...", "resumen": "Sincronizando con los servidores de noticias...", "link": "#"}]
    
    with open("noticias.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    obtener_noticias()
