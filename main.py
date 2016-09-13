#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

from os import system
from storage import Storage

from telegram.ext import Updater
from telegram.ext import CommandHandler

class Worker:
    def __init__(self):
        system('python3 migration.py')
        self.s = Storage()

        self.updater = Updater(token=self.s.token())
        dispatcher = self.updater.dispatcher

        start_handler = CommandHandler('start', self.new_user)
        dispatcher.add_handler(start_handler)

        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        for weekday in weekdays:
            feedback = lambda bot, update, weekday=weekday: self.answer_weekday(bot, update, weekday)
            handler = CommandHandler(weekday, feedback)
            dispatcher.add_handler(handler)

    def work(self):
        self.updater.start_polling()

    def new_user(self, bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

    def answer_weekday(self, bot, update, weekday):
        bot.sendMessage(chat_id=update.message.chat_id, text=str(self.s.day(weekday)))

Worker().work()
