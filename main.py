#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

from os import system
from storage import Storage

from telegram.ext import Updater
from telegram.ext import CommandHandler

from calendar import weekheader

class Worker:
    def __init__(self):
        system('python3 migration.py')
        self.s = Storage()

        self.updater = Updater(token=self.s.token())
        dispatcher = self.updater.dispatcher

        start_handler = CommandHandler('start', self.new_user)
        dispatcher.add_handler(start_handler)

        weekdays = [weekday.lower() for weekday in weekheader(3).split(' ')]
        for weekday in weekdays:
            def feedback(bot, update, weekday=weekday):
                self.answer_weekday(weekday, bot, update)
            handler = CommandHandler(weekday, feedback)
            dispatcher.add_handler(handler)

    def work(self):
        self.updater.start_polling()

    def new_user(self, *args):
        text = "I'm a bot, please talk to me!"
        self.send_message(text, *args)

    def answer_weekday(self, weekday, *args):
        self.send_message(weekday, *args)

    def send_message(self, text, *args):
        bot, update = args
        bot.sendMessage(chat_id=update.message.chat_id,
                        text=text)

Worker().work()
