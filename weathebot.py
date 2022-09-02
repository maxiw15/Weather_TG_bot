import telebot
from weather import weather_want_know
import time
from datetime import datetime

token = "5572813010:AAF18_DlYPryC6-GXcIswRG2q5QTZfWlavA"
bot = telebot.TeleBot(token)

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    time.sleep(60)
    print(current_time)
    if current_time[-1:-2] == "00":
        answer = (weather_want_know())
        bot.send_message(467322175, f"Доброе утро.\nНа улице {round(int(answer[0]))} \n"
                                    f"Температура в настоящий момент {round(int(answer[1]))} градусов.\n"
                                    f"Минимальная температура на сегодня {round(int(answer[2]))} градусов.\n"
                                    f"Максимальная температура на "
                                    f"сегодня {round(int(answer[3]))} градусов.")
