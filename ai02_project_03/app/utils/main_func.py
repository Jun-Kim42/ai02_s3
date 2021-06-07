from app.models.weather_model import Weather
from app.services import weather_api
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def predict_condition():
    weather_list = Weather.query.all()

    ar = []
    label = []

    for weather in weather_list:
        a = [
            weather.temp,
            weather.feels_like,
            weather.pressure,
            weather.humidity,
            weather.deg,
            weather.speed
        ]

        ar.append(a)
        label.append(weather.label)

    ar = np.array(ar)
    label = np.array(label)
    a=1

    rfc = RandomForestClassifier()
    rfc.fit(ar,label)
    a=1

    tom_weather_list = weather_api.get_tommrrow_weather()
    tom_list = [
            tom_weather_list['temp'],
            tom_weather_list['feels_like'],
            tom_weather_list['pressure'],
            tom_weather_list['humidity'],
            tom_weather_list['deg'],
            tom_weather_list['speed']
    ]

    tom_array = np.array(tom_list)
    a=1
    pred = rfc.predict([tom_array])
    a=1
    return pred
