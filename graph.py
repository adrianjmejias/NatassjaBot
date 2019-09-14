from util import generate_buttons, run_actions

class Transition:
    def __init__ (self, answer, condition, node_to_go, actions):
        self.answer = answer
        self.condition = condition
        self.node_to_go = node_to_go
        self.actions = actions

    @classmethod
    def simple (cls, name, node_to_go):
        return cls(name, lambda _name: _name == name, node_to_go,[])

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
        return cls(None, None, actions)



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
            print('checking ' + tt.answer)

            if(tt.condition(res)):
                run_actions(tt.actions, bot)
                print('it is '+ tt.answer)
                return tt.node_to_go
    
        return self