from api import registrate, check_token, edit_token, search_task, search_answer
import os
import requests
import telebot 
from telebot import types 
from dotenv import load_dotenv

load_dotenv()   

TG_TOKEN = os.getenv('TG_TOKEN')

bot = telebot.TeleBot(TG_TOKEN)

#готовит строку для отправки задач
def task_text(task):
    task_text=' '
    i=0
    for len in task:
        i= i+1
        task_text = task_text + f'\n{i}) {len}'
    return task_text

@bot.message_handler(commands=['start'])
def welcome(message):
    
    registrate(message.chat.id)#тут регаю чела в джанго, если первый раз зашел, то регается по chat id, если не первый то будет 404 и идет дальше
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item3 = types.KeyboardButton("Идентификация")
    item2 = types.KeyboardButton("Найти вопрос")
    item1 = types.KeyboardButton('/start')

    keyboard.add(item1, item2, item3)
    bot.send_message(message.chat.id, reply_markup = keyboard, protect_content = True, text ="1-я чтобы попробовать начать сначала.\n2-ая для нахождения вопросов." 
                                                                                                                 "\n3-я кнопка для индетификации")

@bot.message_handler(content_types=["text"])
def go_send_messages(message):
    if message.text == 'Найти вопрос':
        token = check_token(message.chat.id)#проверка токена
        if token > 0:
            bot.send_message(message.chat.id, protect_content = True, text='Напишите начало вопроса текстом в чат.')
            bot.register_next_step_handler(message, bot_search_task)
        else:
            bot.send_message(message.chat.id, protect_content = True, text ='Попытки закончились. Напишите /start, чтобы вернутся в начало.')
    elif message.text == 'Идентификация':
        bot.send_message(message.chat.id, protect_content = True, text ='Пока что я просто добавлю вам токенов на вопросы.\nПотом придумаю, как это сделать умнее.')
        edit_token(message.chat.id, 1)
        welcome(message)

    else:
        bot.send_message(message.chat.id, protect_content = True, text ='Не понял запрос, начнем с начала!')
        welcome(message)

def bot_search_task(message):
    token = check_token(message.chat.id)
    edit_token(message.chat.id, 0)
    if token > 0:
        text=message.text.lower()
        tasks = search_task(text)
        if tasks != 1:
            text_task = task_text(tasks)
            bot.send_message(message.chat.id, protect_content = True, text=f'Напишите номер нужной задачи(цифрой), затем вы получите её ответ.\n{text_task}')
            bot.register_next_step_handler(message, bot_search_answer, tasks)
        else:
            bot.send_message(message.chat.id, protect_content = True, text=f'Похожих задач не найдено, попробуйте найти другую.\nНапишите начало нового вопроса в чат.')
            bot.register_next_step_handler(message, bot_search_task)

    else:
        bot.send_message(message.chat.id, protect_content = True, text ='Попытки закончились. Напишите /start, чтобы вернутся в начало.')

def bot_search_answer(message, tasks):
    # edit_token(message.chat.id, 0) нужно или нет?!
    kek = len(tasks)
    if message.text.isdigit():
        if int(message.text) <= kek:
            i = int(message.text) - 1 
            text = tasks[i]
            answer = search_answer(text)
            print(answer)
            bot.send_message(message.chat.id, protect_content = True, text =f'Задача: {answer[0]}\nОтвет: {answer[1]}\n\nЧто бы найти еще один вопрос выберите "Найти вопрос" в кнопках или напишите эту фразу вручную')
        else:
            bot.send_message(message.chat.id, protect_content = True, text=f'Вы ошиблись, проверьте номер задачи еще раз и напишите его снова.')
            bot.register_next_step_handler(message, bot_search_answer, tasks)
    else:
        bot.send_message(message.chat.id, protect_content = True, text=f'Так как это не цифра, бот выдал ошибку, начнем с начала')
        welcome(message)



try:
    bot.polling(none_stop=True)

except ConnectionError as e:
    print('Ошибка соединения: ', e)
except Exception as r:
    print("Непридвиденная ошибка: ", r)
finally:
    print("Здесь всё закончилось")

