# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot import types
import time
import os
import sys

scriptpath = "./faces.py"

sys.path.append(os.path.abspath(scriptpath))

import faces

API_TOKEN = '256163711:AAFem_Ub6aT6cPEVmhyVQ7d6tt9tF9agvqM'

bot = telebot.TeleBot(API_TOKEN)

hideBoard = types.ReplyKeyboardHide()

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

# Handle '/face'
@bot.message_handler(commands=['face'])
def send_photo(message):
	faces.main("/home/pi/project/images/abba.png","/home/pi/project/images/out_put.png",4)
	bot.send_photo(message.chat.id, open('/home/pi/project/images/out_put.png', 'rb'), reply_to_message_id=message.message_id)




# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


    
    
bot.polling()

while True:
    time.sleep(0)
