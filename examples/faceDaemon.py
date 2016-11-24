# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot import types
import time
import os
import sys
from daemon import runner
import logging

scriptpath = "./faces.py"

sys.path.append(os.path.abspath(scriptpath))

import faces

API_TOKEN = '256163711:AAFem_Ub6aT6cPEVmhyVQ7d6tt9tF9agvqM'

bot = telebot.TeleBot(API_TOKEN)

hideBoard = types.ReplyKeyboardHide()

class faceDaemon():

    def __init__(self):
        self.stdin_path='/dev/null'
        self.stdout_path='/dev/null'
        self.stderr_path='/dev/null'
        self.pidfile_path='/home/pi/project/pyTelegramBotAPI/examples/daemon.pid'
        self.pidfile_timeout=5


    def run(self):
        while True:
            try:
                # logger.info('start')
                if os.path.isfile("/home/pi/project/images/input.jpg"):
                   logger.info("find image")
                   faces.main("/home/pi/project/images/input.jpg","/home/pi/project/images/out_put.jpg",4) 
                   os.remove("/home/pi/project/images/input.jpg")
                   logger.info("send bot")
                   bot.send_photo("290652509", open('/home/pi/project/images/out_put.jpg', 'rb'))
                   os.remove('/home/pi/project/images/out_put.jpg')
                time.sleep(1)
            except Exception as e:
                logger.exception("message")
            
        #bot.send_photo("starterfly", open('/home/pi/project/images/out_put.jpg', 'rb'), "straterfly")
        #os.remove('/home/pi/project/images/out_put.jpg')

        # Handle '/start' and '/help'
        #    @bot.message_handler(commands=['help', 'start'])
        #    def send_welcome(message):
        #        bot.reply_to(message, """\
        #        Hi there, I am EchoBot.
        #        I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
        #        """)
        #
        #        # Handle '/face'
        #        @bot.message_handler(commands=['face'])
        #        def send_photo(message):
        #    	faces.main("/home/pi/project/images/abba.png","/home/pi/project/images/out_put.png",4)
        #	    bot.send_photo(message.chat.id, open('/home/pi/project/images/out_put.png', 'rb'), reply_to_message_id=message.message_id)




        #        # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
        #        @bot.message_handler(func=lambda message: True)
        #        def echo_message(message):
        #        bot.reply_to(message, message.text)

  
app = faceDaemon()
logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("/home/pi/project/pyTelegramBotAPI/examples/faceLog.log")
handler.setFormatter(formatter)
logger.addHandler(handler)

daemon_runner = runner.DaemonRunner(app)
daemon_runner.daemon_context.files_preserve=[handler.stream]
daemon_runner.do_action()
