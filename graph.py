from util import generate_buttons, run_actions
from config import id_test
from telebot import types

def game_end(bot):

    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('/start'))
    bot.send_message(id_test, 'Llega hasta aquí pero recuerda: Reinícialo cada vez que quieras una historia armada por ti y narrada por tu novia', reply_markup=markup)




class Transition:
    def __init__ (self, answer, condition, node_to_go, actions):
        self.answer = answer
        self.condition = condition
        self.node_to_go = node_to_go
        self.actions = actions

    @classmethod
    def simple (cls, name, node_to_go):
        return cls(name, lambda _name: _name == name, node_to_go, [])

    @classmethod
    def with_actions (cls, name, node_to_go, actions):
        node = cls.simple(name, node_to_go)
        node.actions = actions
        return node
        

class Node:
    def __init__ (self, question, transitions, actions):
        self.question = question
        self.transitions = transitions
        self.actions = actions

    @classmethod
    def leaf (cls, actions):
        node = cls(None, None, actions)
        node.actions.append(game_end)
        return node



    def send_query(self, bot, id):

        run_actions(self.actions, bot)

        # Si el nodo es hoja 
        if not self.transitions:
            return None

        bot.send_message(id, self.question, reply_markup=generate_buttons(self.transitions))

    def get_reply(self, bot, id, text):
        res = text

        if not self.transitions:
            return None

        # Si el nodo es interno
        for tt in self.transitions:

            if(tt.condition(res)):
                run_actions(tt.actions, bot)
                return tt.node_to_go
    
        return self