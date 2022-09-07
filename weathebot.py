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
        bot.send_message(467322175, f"Доброе утро.\n{answer}")
    if current_time == "17:40":
        answer = weather_want_know()
        bot.send_message(467322175, f"Добрый вечер.\n{answer}")


