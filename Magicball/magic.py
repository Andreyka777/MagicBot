import telebot
import random

#6954817418:AAHyr5LrxPkNIHQAqsf_WaWoGLr93yn4QCM
#Magicball187_bot
#создать список случайных фраз-ответов, которые будет давать "магический шар"

answers = ["Конечно.......да😋", "Конечно.......нет🤥", "Ну не знаю...🧐🧐🧐", "Ответ на этот вопрос знает только Вселенная😝", "Несомненно😍", "Секрет🤫🤫🤫"]

bot = telebot.TeleBot("6954817418:AAHyr5LrxPkNIHQAqsf_WaWoGLr93yn4QCM")

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Привет! Я бот")

@bot.message_handler(commands=["hello", "hi"])
def greeting(message):
    bot.reply_to(message, "Приветик")

@bot.message_handler(commands=["stop", "bye"])
def parting(message):
    bot.reply_to(message, "Пока-пока")

@bot.message_handler(content_types=['text'])
def answer(message):
    user_text = message.text
    if "?" in user_text:
        bot.reply_to(message, f"{random.choice(answers)}")
    else:
        bot.reply_to(message, f"Задай любой вопрос, я отвечу")

bot.polling(none_stop=True, interval=0)