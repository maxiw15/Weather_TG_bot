import telebot
from yandex import weather_want_know
import time
from datetime import datetime

token = "5572813010:AAF18_DlYPryC6-GXcIswRG2q5QTZfWlavA"
bot = telebot.TeleBot(token)


def time_weather(morning, evening, id):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    time.sleep(60)
    if current_time == morning:
        answer = weather_want_know()
        bot.send_photo(id, "https://bipbap.ru/wp-content/uploads/2017/04/0_7c779_5df17311_orig.jpg")
        bot.send_message(id, f"Доброе утро.\n{answer}")

    if current_time == evening:
        answer = weather_want_know()
        bot.send_photo(id, "https://klike.net/uploads/posts/2019-05/1556708032_1.jpg")
        bot.send_message(id, f"Добрый вечер.\n{answer}")


while True:
    time_weather("09:00", "17:40", 467322175)
    time_weather("09:00", "17:40", 551376473)
    time_weather("09:00", "17:40", 488717704)
