
# https://github.com/eternnoir/pyTelegramBotAPI

import telebot

token = "876288218:AAGwZhJQw38ppbnsZxG5Ik7gSM6_Buf4HHU"

bot = telebot.TeleBot(token)

def FefiVocal(a):
    if(a == 'a'): 
        return 'i'
    if(a == 'e'): 
        return 'i'
    if(a == 'o'): 
        return 'i'
    if(a == 'u'): 
        return 'i'
    return a

@bot.message_handler(commands=['dictator'])
def route_fefify(message):
    print(message)
    print(message.chat.username)

    fefiedMsg = message.text

    fefiedMsg = fefiedMsg.split(' ')

    fefiedMsg.pop(0)

    fefiedMsg = ' '.join(fefiedMsg)
    print(fefiedMsg)
    
    fefiedMsg = ''.join([FefiVocal(x) for x in fefiedMsg])
    print(fefiedMsg)
    bot.reply_to(message,fefiedMsg)
    pass

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

print("bot listening")
bot.polling()