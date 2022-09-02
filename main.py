import telebot
from weather import weather_want_know
import time
from datetime import datetime

token = "5572813010:AAF18_DlYPryC6-GXcIswRG2q5QTZfWlavA"
bot = telebot.TeleBot(token)

now = datetime.now()
current_time = now.strftime("%H:%M")

# Запускаем цикл для проверки времени
while True:
    time.sleep(1)
    if current_time != '6:00':
        answer = (weather_want_know())
        bot.send_message(467322175, f"Доброе утро, хозяин.\nНа улице {answer[0]} \nТемпература в н.м. {answer[1]} \n"
                                    f"Максимальная температура на сегодня {answer[2]} \nМинимальная температура на "
                                    f"сегодня {answer[2]}")

bot.infinity_polling()
