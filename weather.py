import requests

def weather_want_know():
    city_id = 508101
    appid = "5d27c596ee56e7b6861baab0a51ae811"

    try:

        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

        data = res.json()
        answer = []
        answer.append(data['weather'][0]['description'])
        answer.append(data['main']['temp'])
        answer.append(data['main']['temp_min'])
        answer.append(data['main']['temp_max'])
        return answer
    except Exception as e:
        return ("Exception (weather):", e)
        pass

