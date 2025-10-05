#Погодний роблю на weatherapi, бо на openweathermap не працювали ключі чомусь

import requests

API_KEY = "c11de37be37c426ab4581406250510"
CITY = "Poltava"

url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&lang=uk"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    location = data["location"]["name"]
    country = data["location"]["country"]
    temp = data["current"]["temp_c"]
    feels = data["current"]["feelslike_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    wind = data["current"]["wind_kph"]

    print(f"Погода у {location}, {country}:")
    print(f"Температура: {temp}°C (відчувається як {feels}°C)")
    print(f"Опис: {condition}")
    print(f"Вологість: {humidity}%")
    print(f"Вітер: {wind} км/год")
else:
    print("Помилка:", response.status_code, response.text)
