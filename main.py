#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import sys

from storage import Storage as S
s = S()

from telegram.ext import Updater
updater = Updater(token=s.get_token())
dispatcher = updater.dispatcher

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
