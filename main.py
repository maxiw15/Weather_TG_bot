import telebot
from weather import weather_want_know
import time
from datetime import datetime

token = "5572813010:AAF18_DlYPryC6-GXcIswRG2q5QTZfWlavA"
bot = telebot.TeleBot(token)

now = datetime.now()
current_time = now.strftime("%H:%M")


while True:
    time.sleep(1)
    if current_time != '6:00':
        answer = (weather_want_know())
        bot.send_message(467322175, f"Доброе утро, хозяин.\nНа улице {answer[0]} \n"
                                    f"Температура в настоящий момент {answer[1]} градусов\n"
                                    f"Минимальная температура на сегодня {answer[2]} градусов \n"
                                    f"Максимальная температура на "
                                    f"сегодня {answer[3]} градусов")

bot.infinity_polling()
