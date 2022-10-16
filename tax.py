import requests
import datetime
import csv


def check_price():
    url = "https://widget.city-mobil.ru/c-api"
    payload = {
        "method": "getprice",
        "ver": "4.59.0",
        "phone_os": "widget",
        "os_version": "web mobile-web",
        "locale": "ru",
        "latitude": 55.431964,
        "longitude": 37.565696,
        "del_latitude": 55.422457,
        "del_longitude": 37.536246,
        "options": [],
        "payment_type": ["cash"],
        "tariff_group": [2],
        "source": "O",
        "hurry": 1
    }
    headers = {
        "authority": "widget.city-mobil.ru",
        "accept": "application/json, text/plain, */*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json",
        "origin": "https://city-mobil.ru",
        "referer": "https://city-mobil.ru/",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Linux",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    print("Price", end=" ")
    price = response.json()["prices"][0]["price"]
    td = datetime.datetime.now()
    tme = td.strftime("Time: %H:%M:%S")
    date = td.strftime("Date: %d/%m/%Y")
    print(tme, date)
    my_data = [date, tme, price]
    with open("data.csv", "a") as file:
        writer = csv.writer(file, dialect='excel')
        writer.writerow(my_data)
