import telebot
import script


bot = telebot.TeleBot(script.token)

@bot.message_handler(content_types='text')
def message(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()