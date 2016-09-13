#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

from os import system
system('python3 migration.py')

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

def answer_weekday(bot, update, weekday):
    bot.sendMessage(chat_id=update.message.chat_id, text=str(s.day(weekday)))

weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
for weekday in weekdays:
    feedback = lambda bot, update, weekday=weekday: answer_weekday(bot, update, weekday)
    handler = CommandHandler(weekday, feedback)
    dispatcher.add_handler(handler)

updater.start_polling()
