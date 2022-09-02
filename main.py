import telebot
from weather import weather_want_know


token = "5572813010:AAF18_DlYPryC6-GXcIswRG2q5QTZfWlavA"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['чепопогоде'])
def send_welcome(message):
    answer = (weather_want_know())
    bot.reply_to(message, f"На улице {round(int(answer[0]))} \n"
                          f"Температура в настоящий момент {round(int(answer[1]))} градусов.\n"
                          f"Минимальная температура на сегодня {round(int(answer[2]))} градусов.\n"
                          f"Максимальная температура на "
                          f"сегодня {round(int(answer[3]))} градусов.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "доступная команда - /чепопогоде")


bot.infinity_polling()
