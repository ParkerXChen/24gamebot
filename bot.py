from telegram.ext import Updater,MessageHandler, Filters,CommandHandler
from telegram import BotCommand
import os
import game24 

def start(update, context):
    msg = 'Hi! Welcome to the 24 Game Bot by @ParkerChen. This bot was made to play the game "24", a game where you try to make the number 24 using the 4 numbers I give you. Ready? Type /start24 to begin a game!'
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def read_file_as_str(file_path):
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

TOKEN=read_file_as_str('TOKEN')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

commands = game24.add_handler(dispatcher)
updater.bot.set_my_commands(commands)

updater.start_polling()
updater.idle()