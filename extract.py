import schedule
import time
import pandas as pd
import requests
import os

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 39.7767,
        "longitude": 30.5206,
        "current_weather": "true"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        time = data['current_weather']['time']
        current_temp = data['current_weather']['temperature']
        current_wind_speed = data['current_weather']['windspeed']

        df = pd.DataFrame([{
            'time': time,
            'temperature': current_temp,
            'wind_speed': current_wind_speed
        }])

        file_exists = os.path.isfile("weather_data.csv")

        df.to_csv("weather_data.csv", mode="a", index=False, header=not file_exists)

        print("Yeni veri eklendi:\n", df)

    else:
        print(f"Veri alınırken hata oluştu: {response.status_code}")

get_weather()