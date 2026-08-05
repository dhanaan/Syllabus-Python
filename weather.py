import os
from pprint import pprint
from dotenv import load_dotenv
import requests
import take_input as inp
load_dotenv()


def get_current_weather():
    print("Get Current Weather Conditions")
    city = inp.take_input("Enter city: ")
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()
    pprint(weather_data)
    print()
    print(f'Current weather for {weather_data["name"]}')
    print(f'The temp is {weather_data["main"]["temp"]}C')
    print(f'Feels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}')
    print()

if __name__ == '__main__':
    get_current_weather()
