import telebot
# import config
import random
 
from telebot import types
 
bot = telebot.TeleBot("5868878555:AAEetjhGk43IZ2LasbIa9vKbzTNCQ92slrs")
 
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Cлучайное число(от 1 до 10)")
    item2 = types.KeyboardButton("Геометрическая Прогрессия")
    markup.add(item1, item2)
    msg = bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>\nБот, который способен на все.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, main)
 
@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Cлучайное число(от 1 до 10)':
     bot.send_message(message.chat.id, str(random.randint(0,10)))
    elif message.text == 'Геометрическая Прогрессия':
     msg = bot.send_message(message.chat.id, "Введите первый член геометрической прогрессии, затем знаменатель прогрессии и номер последнего члена (писать через пробел)")
     bot.register_next_step_handler(msg, calc)   
    else:
     bot.send_message(message.chat.id, 'Я не знаю что ответить :(')

def calc(message):
    a, b, c = message.text.split()
    b1 = int(a)
    q = int(b)
    n = int(c)
    bn = b1 * q**(n - 1)
    sn = (b1*(q**n - 1)) // (q-1)
    bot.send_message(message.chat.id, f'Последний член геометрической прогрессии(bn) = {bn}\nСумма геометрической прогрессии(SUMn) = {sn}')



bot.polling(none_stop=True)