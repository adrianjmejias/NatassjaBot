
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

@bot.message_handler(commands=['start'])
def start(message):
    # print(message)
    # print(message.chat.username)

    # TODO: SET WELCOME MESSAGE
    msg =   "WELCOME MESSÁGE"
    bot.reply_to(message,msg)
    pass

@bot.message_handler(func=lambda message: True)
def echo_all(message):



    # act_node = act_node.visit()
	bot.reply_to(message, message.text)

print("bot listening")
bot.polling()