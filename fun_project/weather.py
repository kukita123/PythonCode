import requests


class WeatherParams:
    def __init__(self, city, units="metric", lang="en"):
        self.city = city
        self.units = units
        self.lang = lang
        self.mode = "json"


def get_weather(appid, weather_params):
    endpoint = "https://api.openweathermap.org/data/2.5/weather"
    query_params = {
        'q': weather_params.city,
        'units': weather_params.units,
        'lang': weather_params.lang,
        'mode': weather_params.mode,
        'appid': appid,
    }
    resp = requests.get(endpoint, params=query_params)
    return resp.json()


appid = "c0878029d1bafb4e5d5ec1602bc1c515"
city_name = "Sofia"
params = WeatherParams(city_name)
print(
    f"Current temperature in {city_name} is {get_weather(appid, params)['main']['temp']} degrees")
print(
    f"Current temperature in {city_name} is {get_weather(appid, params)['main']['temp']} degrees")
params = WeatherParams(city="Plovdiv", lang="bg")
print(
    f"Current temperature in Plovdiv is {get_weather(appid, params)['main']['temp']} degrees")
