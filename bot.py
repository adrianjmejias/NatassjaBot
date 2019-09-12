
# https://github.com/eternnoir/pyTelegramBotAPI

from main import act_node
import telebot
token = "876288218:AAGwZhJQw38ppbnsZxG5Ik7gSM6_Buf4HHU"
bot = telebot.TeleBot(token)


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

    print(message)
    print(message.from_user)
    # bot.forward_message(id_adri,message.from_user.id, message.text)
    bot.reply_to(message, message.text)

# bot.send_photo(id_alosa, open('./doggy.jpg', 'rb'), 'tiene un sombrerito mrc')


while act_node:
    act_node = act_node.visit(bot)



types= telebot.types

# markup = types.ReplyKeyboardMarkup(row_width=2)
# itembtn1 = types.KeyboardButton('a')
# itembtn2 = types.KeyboardButton('v')
# itembtn3 = types.KeyboardButton('d')
# markup.add(itembtn1, itembtn2, itembtn3)
# bot.send_message(id_alosa, "Choose one letter:", reply_markup=markup)


# audio = open('./aintnosunshine.mp3', 'rb')
# bot.send_audio(id_alosa, audio)

# video = open('./jaj.mp4', 'rb')
# bot.send_video(id_alosa, video, 'muack')

print("bot listening")
bot.polling(none_stop=False, interval=0, timeout=500)