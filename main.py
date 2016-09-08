#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

from storage import Storage as S
s = S()

from telegram.ext import Updater
updater = Updater(token=s.token())
dispatcher = updater.dispatcher

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def monday(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="monday")

monday_handler = CommandHandler('monday', monday)
dispatcher.add_handler(monday_handler)

def tuesday(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="tuesday")

tuesday_handler = CommandHandler('tuesday', tuesday)
dispatcher.add_handler(tuesday_handler)

updater.start_polling()
