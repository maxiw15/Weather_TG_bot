import requests
from pprint import  pprint

weather_dict = {"clear": "Ясно",
                "partly-cloudy": "Малооблачно",
                "cloudy": "Облачно с прояснениями",
                "overcast": "Пасмурно",
                "drizzle": "Морось",
                "light-rain": "Небольшой дождь",
                "rain": "Дождь",
                "moderate-rain": "Умеренно сильный дождь",
                "heavy-rain": "Сильный дождь",
                "continuous-heavy-rain": "Длительный сильный дождь",
                "showers": "Ливень",
                "wet-snow": "Дождь со снегом",
                "light-snow": "Небольшой снег",
                "snow": "Снег",
                "snow-showers": "Снегопад",
                "hail": "Град",
                "thunderstorm": "Гроза",
                "thunderstorm-with-rain": "Дождь с грозой",
                "thunderstorm-with-hail": "Гроза с градом"}


def weather_want_know():
    try:
        url = "https://api.weather.yandex.ru/v2/informers?"
        headers = {'X-Yandex-API-Key': 'c8ff1703-12da-4776-89ca-55858ebd74da'}
        res = requests.get(url, params={'lat': '55.4242', 'lon': '37.5547', 'lang': 'ru_RU', "hours": "true",
                                        'X-Yandex-API-Key': 'c8ff1703-12da-4776-89ca-55858ebd74da'}, headers=headers)
        data = res.json()
    finally:
        return f'В настоящий момент температура {data["fact"]["temp"]} градусов. \n' \
               f'Ощущается как {data["fact"]["feels_like"]} градусов. \n' \
               f'{weather_dict[data["fact"]["condition"]]}. \n' \



def transport_want_know():
    try:
        res = requests.get("https://api.rasp.yandex.net/v3.0/search/?",
                           params={'from': "s9600731", "to": "s2001005", 'apikey': '548ab260-4f49-4ba5-9779'
                                                                                   '-c05eeacfb9a0', 'format': 'json'})

        data = res.json()
    finally:
        return data


