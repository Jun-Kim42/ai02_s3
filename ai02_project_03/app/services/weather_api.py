import requests
import json

API_KEY='fe3f094dcbab22dd2176499891842699'

API_URL = f'https://api.openweathermap.org/data/2.5/weather?q=Incheon&appid={API_KEY}'

def get_current_weather():
    raw_data = requests.get(API_URL)
    parsed_data = json.loads(raw_data.text)

    temp        = parsed_data['main']['temp']
    pressure    = parsed_data['main']['pressure']
    humidity    = parsed_data['main']['feels_like']
    feels_like  = parsed_data['main']['temp']
    speed       = parsed_data['wind']['speed']
    deg         = parsed_data['wind']['deg']
    dt          = parsed_data['dt']


    weather_data = {
        'id':dt,
        'temp':temp,
        'pressure':pressure,
        'humidity':humidity,
        'feels_like':feels_like,
        'speed':speed,
        'deg':deg
    }
    return weather_data

def get_tommrrow_weather():
    lon = 126.4161
    lat = 37.45
    city_name = 'Incheon'
    API_KEY='940e55d06615f7c5992a88ff60084c56'
    API_URL2 = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=daily&appid={API_KEY}'
    
    raw_data = requests.get(API_URL2)
    parsed_data = json.loads(raw_data.text)
    a=1

    temp        = parsed_data['hourly'][23]['temp']
    pressure    = parsed_data['hourly'][23]['pressure']
    humidity    = parsed_data['hourly'][23]['humidity']
    feels_like  = parsed_data['hourly'][23]['feels_like']
    speed       = parsed_data['hourly'][23]['wind_speed']
    deg         = parsed_data['hourly'][23]['wind_deg']
    


    weather_data_to = {
        'temp':temp,
        'pressure':pressure,
        'humidity':humidity,
        'feels_like':feels_like,
        'speed':speed,
        'deg':deg
    }
    return weather_data_to
