import telebot
import script


bot = telebot.TeleBot(script.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi!, I\'m AWED\'s bot!')

@bot.message_handler(commands=['sendMeImage'])
def image(message):
    bot.send_photo(message.chat.id, 'https://cdn.discordapp.com/attachments/1032285013644947486/1032716976205877248/animeArt.jpg')

@bot.message_handler(content_types='text')
def message(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()