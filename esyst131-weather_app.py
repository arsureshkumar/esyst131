
'''

ESYST-131 - Weather App

A. Suresh Kumar (5/23/22)

==================================

This program will make a call to the Open Weather

API to print out weather information from a city

of the user's choosing.

==================================

Variables:

weather_dict   # contains the json information returned from the Open Weather API call

condition     # contains extracted weather condition

temp     # contains extracted temperature

increment     # contains extracted wind speed

increment     # contains extracted wind direction

==================================

Functions:

get_weather(city) # uses the inputted city parameter to display weather information to the user

==================================

Imports:

requests      # used to request data from the Open Weather API

'''

import requests

def get_weather(city):
    #requests the data from the API based on an inputted city parameter, then converts the response to a dictionary, stroed in the weather_dict variable
    weather_dict = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=fc8f32ecacdd8afcef77e9f4d33c08f2").json()

    #extracts the condition, temperature, wind speed, and wind direction statistics from the weather_dict dictionary
    condition, temp, wind_speed, wind_dir = weather_dict['weather'][0]['main'], (weather_dict['main']['temp'] - 273.15)*9/5+32, weather_dict['wind']['speed'], weather_dict['wind']['deg']

    #displays the labelled data to the user
    print("The condition there is " + str(condition) + ", the temperature is " + str(temp) + "°F, the wind speed is " + str(wind_speed) + "mi/hr, and the wind direction is " + str(wind_dir) + " in meteorological degrees.")

get_weather(input("Enter your city: "))