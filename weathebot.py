import telebot
from weather import weather_want_know
import time
from datetime import datetime

token = "5572813010:AAF18_DlYPryC6-GXcIswRG2q5QTZfWlavA"
bot = telebot.TeleBot(token)

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    time.sleep(30)
    if current_time == "13:32":
        answer = (weather_want_know())
        bot.send_message(467322175, f"Доброе утро.\nНа улице {answer[0]} \n"
                                    f"Температура в настоящий момент {answer[1]} градусов.\n"
                                    f"Минимальная температура на сегодня {answer[2]} градусов.\n"
                                    f"Максимальная температура на "
                                    f"сегодня {answer[3]} градусов.")
