import pandas as pd
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Cargar clave API desde .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Ruta al archivo de ciudades
csv_ciudades = "data/ciudades_argentina_con_coordenadas.csv"

# Leer la lista de ciudades
ciudades = pd.read_csv(csv_ciudades)

# Lista para guardar resultados
resultados = []

# Recorrer cada ciudad
for _, row in ciudades.iterrows():
    ciudad = row["ciudad"]
    provincia = row["provincia"]
    lat = row["lat"]
    lon = row["lon"]

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=es"

    try:
        response = requests.get(url)
        data = response.json()

        resultados.append({
            "ciudad": ciudad,
            "provincia": provincia,
            "lat": lat,
            "lon": lon,
            "temperatura": data["main"]["temp"],
            "humedad": data["main"]["humidity"],
            "clima": data["weather"][0]["description"],
            "fecha": datetime.now().strftime("%Y-%m-%d"),
            "hora": datetime.now().strftime("%H:%M:%S")
        })

    except Exception as e:
        print(f"⚠️ Error consultando {ciudad}: {e}")

# Convertir a DataFrame
df_resultados = pd.DataFrame(resultados)

# Guardar en CSV dentro de /data
output_csv = "data/datos_clima_argentina.csv"

# Si ya existe, agregar (sin duplicar encabezado)
if os.path.exists(output_csv):
    df_resultados.to_csv(output_csv, mode='a', header=False, index=False)
else:
    df_resultados.to_csv(output_csv, index=False)

print("✅ Datos de clima guardados correctamente en data/datos_clima_argentina.csv")
