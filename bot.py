import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import pickle
import shelve

bot = telebot.TeleBot("5216151294:AAGqtj1iTiQpqIKIQHARZGpJmNANH6whv_k")
places=['ПАВЛОВСКИЙ ТРАКТ','ЛЕНТА','ЛЕНИНА','ОГНИ','Новый рынок']
with open('grafic_dump.dat', 'rb') as f:
    total_graf = pickle.load(f)

@bot.message_handler(content_types=["text"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()                                             
    for i in places:
        button = types.InlineKeyboardButton(text = i[0], callback_data = i.index())
        keyboard.add(button)
    bot.send_message(message.chat.id, "Выберете место из списка:", reply_markup = keyboard)

@bot.callback_query_handler(func = lambda call: True)
def ans(call):
    message = call.message
    print(int(call.data))
    if int(call.data) in range(5):
        keyboard = types.InlineKeyboardMarkup()
        hair_graf = total_graf[int(call.data)]
        for masters in hair_graf:
            button = types.InlineKeyboardButton(text = masters[0], callback_data = str(masters[1]))
            keyboard.add(button)
        bot.send_message(message.chat.id, "Выберете мастера из списка:", reply_markup = keyboard)
    for hair in total_graf:
        for master in hair:
            for j in master:
                if int(call.data) == j:
                    bot.send_message(message.chat.id, 'Расписание мастера с учетом замен на текущий месяц:')
                    bot.send_message(message.chat.id, text = master[2])

bot.infinity_polling()