import requests
import json

def obtener_noticias():
    # Usamos un servicio intermedio que extrae las noticias por nosotros para evitar bloqueos
    # Esta URL apunta a las últimas noticias de deportes globales
    rss_proxy_url = "https://rss2json.com"
    
    noticias = []
    try:
        response = requests.get(rss_proxy_url, timeout=20)
        data = response.json()
        
        if data['status'] == 'ok':
            for item in data['items'][:10]:
                noticias.append({
                    "titulo": item['title'],
                    "resumen": "Lee la nota completa en el portal oficial.",
                    "link": item['link']
                })
        else:
            raise Exception("Proxy ocupado")
            
    except Exception:
        # Si todo falla, mantenemos estas para que el cintillo siempre se mueva
        noticias = [
            {"titulo": "LIGA MX: Actualización de última hora", "resumen": "Revisa los resultados aquí.", "link": "https://marca.com"},
            {"titulo": "F1: Novedades del GP y Checo Pérez", "resumen": "Toda la información del piloto mexicano.", "link": "https://marca.com"}
        ]
    
    with open("noticias.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    obtener_noticias()
