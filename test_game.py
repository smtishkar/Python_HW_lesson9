import telebot
import random
 
from telebot import types
bot = telebot.TeleBot("5868878555:AAEetjhGk43IZ2LasbIa9vKbzTNCQ92slrs")


sweets = 117
take = 10
turn = "User"

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Играть")
    markup.add(item1)
    msg = bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>\nБот, который способен на все.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, main)

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Играть':
     msg = bot.send_message(message.chat.id, 'Давай начнем! Бери конфеты первым')
     bot.register_next_step_handler(msg, play)

def play(message):
    global sweets, take, turn
    while sweets > 28:
        if sweets > 28 and turn == "User":
            take = int(message.text)
            while take > 28:
                msg_low = bot.send_message(message.chat.id, f'Человек должен быть умнее, бери меньше 28 конфет')
                bot.register_next_step_handler(msg_low, play)
                return
            sweets -= take
            bot.send_message(message.chat.id,
                            f'Осталось {sweets}')
            turn = "Bot"
        elif sweets > 28 and turn == "Bot":    
            take = random.randint(1, 28)
            sweets = sweets - take
            bot.send_message(message.chat.id, f'Бот взял {take}')
            bot.send_message(message.chat.id,
                            f'Осталось {sweets}')
            msg = bot.send_message(message.chat.id, '{Хм... Ну давай продолжим! Тяни дальше')
            turn = "User"
            bot.register_next_step_handler(msg, play)
            return
    if turn == "Bot":
        bot.send_message(message.chat.id, f'Бот победил')
    else:
        bot.send_message(message.chat.id, f'Человек победил машину')
    return


# @bot.message_handler(func=lambda message: True)

    # a, b, c = message.text.split()
    # b1 = int(a)
    # q = int(b)
    # n = int(c)
    # bn = b1 * q**(n - 1)


# @bot.message_handler(content_types=['text'])
# def main(message):
#     if message.text == 'Cлучайное число(от 1 до 10)':
#      bot.send_message(message.chat.id, str(random.randint(0,10)))
#     elif message.text == 'Геометрическая Прогрессия':
#      msg = bot.send_message(message.chat.id, "Введите первый член геометрической прогрессии, затем знаменатель прогрессии и номер последнего члена (писать через пробел)")
#      bot.register_next_step_handler(msg, calc)   
#     else:
#      bot.send_message(message.chat.id, 'Я не знаю что ответить :(')



bot.polling(none_stop=True)



# def play(message):
#     global sweets, take, turn
#     while sweets > 0:
#         if sweets > 28:
#             if turn == "User":
#                 take = int(message.text)
#                 sweets -= take
#                 bot.send_message(message.chat.id,
#                                 f'Осталось {sweets}')
#                 turn = "Bot"
#             else:
#                 take = random.randint(1, 28)
#                 sweets = sweets - take
#                 bot.send_message(message.chat.id, f'Бот взял {take}')
#                 bot.send_message(message.chat.id,
#                                 f'Осталось {sweets}')
#                 msg = bot.send_message(message.chat.id, '{Хм... Ну давай продолжим! Тяни дальше')
#                 turn = "User"
#                 bot.register_next_step_handler(msg, play)
#                 return
#     if turn == "Bot":
#         bot.send_message(message.chat.id, f'Бот победил')
#     else:
#         bot.send_message(message.chat.id, f'Человек победил машину')
#     return
