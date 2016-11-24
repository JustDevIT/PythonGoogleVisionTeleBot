import telebot

bot = telebot.TeleBot("256163711:AAFem_Ub6aT6cPEVmhyVQ7d6tt9tF9agvqM")

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, suspect)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.polling()
