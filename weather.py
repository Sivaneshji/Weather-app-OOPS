import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n*** Get Current weaher conditions ***\n")
    city = input("\nPlease enter a city name:\n")
    requests_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'
    print(requests_url)
    weather_data = requests.get(requests_url).json()
    
    # pprint(weather_data)
    
    print(f'\nThe current weather of {weather_data["name"]} is {weather_data["main"]["temp"]:.1f}')
    
get_current_weather()