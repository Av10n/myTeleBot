import telebot
import script


bot = telebot.TeleBot(script.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi!, I\'m AWED\'s bot!')

@bot.message_handler(content_types='text')
def message(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()