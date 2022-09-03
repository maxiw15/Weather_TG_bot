import requests


def weather_want_know():
    try:
        res = requests.get("https://api.weather.yandex.ru/v2/forecast",
                           params={'lat': '55.2547', 'lon': '37.3240', 'lang': 'ru_RU',
                                   'X-Yandex-API-Key': 'c8ff1703-12da-4776-89ca-55858ebd74da'})

        data = res.json()
    finally:
        print(data)


def transport_want_know():
    try:
        res = requests.get("https://api.rasp.yandex.net/v3.0/stations_list/ ?",
                           params={'apikey': '548ab260-4f49-4ba5-9779-c05eeacfb9a0', 'lang': 'ru_RU', 'format': 'json'})

        data = res.json()
    finally:
        print(data)


weather_want_know()
transport_want_know()
