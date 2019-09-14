from telebot import types

def asset_path(file_name):
    return './assets/'+file_name

def run_actions(actions, *args):
    for action in actions:
        action(*args)


def generate_buttons(transitions):
    markup = types.ReplyKeyboardMarkup()

    buttons = list(map( lambda tt: types.KeyboardButton(tt.answer), transitions ))
    markup.add( *buttons )
    
    return markup