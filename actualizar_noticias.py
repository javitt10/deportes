import json

def obtener_noticias():
    # DATOS DE PRUEBA LOCALES (Sin usar internet)
    noticias = [
        {
            "titulo": "¡PRUEBA EXITOSA!",
            "resumen": "Si lees esto, el robot de GitHub funciona y puede escribir archivos.",
            "link": "https://google.com"
        },
        {
            "titulo": "Siguiente paso: Conexión",
            "resumen": "Ya logramos que el archivo se genere solo. Ahora falta el internet.",
            "link": "#"
        }
    ]
    
    # Guardamos el archivo noticias.json
    with open("noticias.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=2)
    print("Archivo generado con datos de prueba.")

if __name__ == "__main__":
    obtener_noticias()
