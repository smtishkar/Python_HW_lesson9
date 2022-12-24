import  telebot
from random import randint

bot = telebot.TeleBot("5868878555:AAEetjhGk43IZ2LasbIa9vKbzTNCQ92slrs")

sweets = 117
turn = 1 
who_will_start = randint(0,1) 



def who_will_start():
    first_player = randint(0,1) 
    if first_player == 0:
        return 'Я тут случайно определил, что начинает игрок'
    elif first_player == 1:
        return 'Я тут случайно определил, что начинает МегаБот'





@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Прибет я Мегабот')
    
@bot.message_handler(commands=['play'])
def play(message):
    bot.send_message(message.chat.id, who_will_start())

@bot.message_handler(content_types=['text'])
def game_process(message):
    global sweets
    if message.text == '1':
        msg = bot.send_message(message.from_user.id, 'Введите номер телефона: ')
    # if turn [message.chat.id] == 100:
    #     sweets = 105
    #     bot.send_message(message.chat.id, 'Я разум')

bot.infinity_polling()
message: True

