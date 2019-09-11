



class Transition:
    def __init__ (self, answer, condition, node_to_go):
        self.answer = answer
        self.condition = condition
        self.node_to_go = node_to_go

    # so we avoid code bloating for simple transitions
    @classmethod
    def simple (cls, name, node_to_go):
        return cls(name, lambda _name: _name == name, node_to_go)


        
    pass


class Node:
    def __init__ (self, question, transitions, actions):
        self.question = question
        self.transitions = transitions
        self.actions = actions

    @classmethod
    def leaf (cls, actions):
        return cls(None, None, actions)

    def act(self):
        for action in self.actions:
            action()

    def visit(self):

        self.act()

        # Si el nodo es hoja 
        if not self.transitions:
            print('hoja' + str(self.actions))
            return None

        res = input(self.question)

        # Si el nodo es interno
        for tt in self.transitions:
            print('checking ' + tt.answer)

            if(tt.condition(res)):
                print('it is '+ tt.answer) 
                print(tt.node_to_go) 
                return tt.node_to_go

        return self