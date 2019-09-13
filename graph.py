def run_actions(actions, *args):
    for action in actions:
        action(*args)

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
        
pass

class Node:
    def __init__ (self, question, transitions, actions):
        self.question = question
        self.transitions = transitions
        self.actions = actions

    @classmethod
    def leaf (cls, actions):
        return cls(None, None, actions)

    def act(self, bot):
        for action in self.actions:
            action(bot)

    def visit(self, bot):

        self.act(bot)

        # Si el nodo es hoja 
        if not self.transitions:
            return None

        #bot.send_message()
        res = input(self.question)

        # Si el nodo es interno
        for tt in self.transitions:
            print('checking ' + tt.answer)

            if(tt.condition(res)):
                print('it is '+ tt.answer)
                return tt.node_to_go

        return self