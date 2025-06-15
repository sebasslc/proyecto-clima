import requests
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

# Obtener la API Key desde las variables de entorno
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Ciudad que vamos a consultar
CITY = "Buenos Aires"

# URL de la API de OpenWeather
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=es"

# Hacer la solicitud a la API
response = requests.get(URL)
data = response.json()

# Mostrar algunos resultados
print(f"Ciudad: {data['name']}")
print(f"Temperatura: {data['main']['temp']}°C")
print(f"Humedad: {data['main']['humidity']}%")
print(f"Clima: {data['weather'][0]['description'].capitalize()}")
