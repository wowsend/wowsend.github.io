import telebot
from telebot import types

TOKEN = '7803093290:AAFlnnCG7kCg5iasmSEksNGuH3uEsB99Qr4'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):

        mainmenu = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=2)

        item1 = types.KeyboardButton('🛍 Открыть магазин')
        item2 = types.KeyboardButton('🛒 Корзина')
        item3 = types.KeyboardButton('Информация')


        mainmenu.add(item1, item2, item3)


        bot.send_message(message.chat.id, '{0.first_name}добро пожаловать в магазин одежды'.format(message.from_user), reply_markup = mainmenu)


@bot.message_handler(content_types=['text'])
def bot_message(message):
        if message.chat.type == 'private':
                if message.text == '🛍 Открыть магазин':
                        shop = types.InlineKeyboardMarkup()
                        url_btn = types.InlineKeyboardButton('🛍Открыть магазин', url='https://sosobot.github.io/')
                        shop.add(url_btn)
                        bot.send_message(message.chat.id, 'Чтобы открыть наш магазин нажмите кнопку ниже', reply_markup = shop)

                elif message.text == '🛒 Корзина':
                        bot.send_message(message.chat.id, 'Функция в разработке')   

                elif message.text == 'Информация':
                        bot.send_message(message.chat.id, 'Связь: @salaga2')






bot.polling(none_stop=True)   