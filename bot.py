# import json
import os

# import config
import telebot 
# from telebot import types 
from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.getenv('TG_TOKEN')

bot = telebot.TeleBot(TG_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
        bot.send_message(message.chat.id, "Метро Люблино, работаем Бототяги")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
        print(message)
        bot.send_message(message.chat.id, "ку")

bot.polling(none_stop=True)