from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="kansas City"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_kEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print("\n*** Get curren weather Conditions ***")
    city = input("\nPlease enter a city name: ")

    #check for empty strings or string with only  spaces
    if not bool(city.strip()):
        city = "Kansas City" #this will be act as default value if nothing given

    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)


# #===== Only use in Cmd line output =====
# import requests
# from dotenv import load_dotenv
# import os
# from pprint import pprint #pretty print

# #load the .env contnet that's API KEY in it
# load_dotenv()

# def get_current_weather():
#     print("\n*** Get current weather conditions ***\n")

#     city = input("\nPlease enter a city name:\n")

#     #Current weather data API
#     request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_key")}&q={city}&units=imperial'

#     # print(request_url)

#     weather_data = requests.get(request_url).json()

#     #pprint(weather_data)
#     print(f'\nCurrent weather for {weather_data["name"]}')
#     print(f'\nThe temp is {weather_data["main"]["temp"]}')
#     print(f'\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}')

# if __name__ == "__main__":
#     get_current_weather()
