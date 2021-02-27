from telegram.ext import Dispatcher,CommandHandler,MessageHandler,Filters,CallbackContext
from telegram import BotCommand,Animation
import random

cards = random.sample([1,2,3,4,5,6,7,8,9,10],4)
gamegoingon = False

def start24(update, context):
    global gamegoingon
    update.effective_message.reply_text(f"Welcome to 24! Your goal is to figure out how to make 24 with these numbers.\n\n Your numbers are: {cards[0]},{cards[1]},{cards[2]}, and {cards[3]}! \n\nRemember, you can only use +, -, *, and /. \n\nGood Luck!")
    gamegoingon = True

def viewnumbers(update, context):
    update.effective_message.reply_text(f"Your numbers are: {cards[0]},{cards[1]},{cards[2]}, and {cards[3]}. \n\nGood Luck!")

def end24(update, context):
    global cards
    global gamegoingon
    cards = random.sample([1,2,3,4,5,6,7,8,9,10],4)
    update.message.reply_text('Game ended. Use the /start24 command to begin a new game.')
    gamegoingon = False

def answer(update,context):
    global gamegoingon
    print('aaa')
    
    validcharacters = ['+','-','*','/']
    for i in cards:
        validcharacters.append(str(i))

    print(validcharacters)
    if gamegoingon == True:
        valid = True
        for i in range(len(update.message.text)):
            print(i)
            if not update.message.text[i] in validcharacters:
                valid = False

        print(valid)
        if valid == True:
            usedcharacters = []
            onlyusedeachcharacteronce = True
            for i in range(len(update.message.text)):
                if not update.message.text[i] in usedcharacters:
                    usedcharacters.append(i)
                else:
                    onlyusedeachcharacteronce = False

            if onlyusedeachcharacteronce == True:
                print(update.message.text)
                if eval(update.message.text) == 24:
                    update.message.reply_text("You win! Yay!")


def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('start24', start24))
    dp.add_handler(CommandHandler('viewnumbers', viewnumbers))
    dp.add_handler(CommandHandler('end24', end24))
    dp.add_handler(MessageHandler(filters = Filters.all, callback=answer))
    return [BotCommand('start24','Begin a new game of 24'),BotCommand('viewnumbers','View the numbers of a game of 24'),BotCommand('end24','End a game of 24')]
