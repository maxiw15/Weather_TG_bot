import telebot
from yandex import weather_want_know
import time
from datetime import datetime

token = "5572813010:AAF18_DlYPryC6-GXcIswRG2q5QTZfWlavA"
bot = telebot.TeleBot(token)

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    time.sleep(60)
    if current_time == '06:00':
        answer = weather_want_know()
        bot.send_photo(467322175, "https://bipbap.ru/wp-content/uploads/2017/04/0_7c779_5df17311_orig.jpg")
        bot.send_message(467322175, f"Доброе утро.\n{answer}")

    if current_time == "17:40":
        answer = weather_want_know()
        bot.send_photo(467322175, "https://klike.net/uploads/posts/2019-05/1556708032_1.jpg")
        bot.send_message(467322175, f"Добрый вечер.\n{answer}")



