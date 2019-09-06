



class Transition:


    def __init__ (self, answer, condition, node_to_go):
        self.answer = answer
        self.condition = condition
        self.node_to_go = node_to_go

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
        




    



italia = Node.leaf([
    lambda : print('italia')
])

countries = Node('a que pais quieres ir?', 
    [
        Transition('italia', lambda name: name == 'italia', Node.leaf([
            lambda : print('italia')
        ])),
        Transition('polonia', lambda name: name == 'polonia', Node.leaf([
            lambda : print('polonia')
        ])),
        Transition('inglaterra', lambda name: name == 'inglaterra', Node.leaf([
            lambda : print('inglaterra')
        ])),
        Transition('francia', lambda name: name == 'francia', Node.leaf([
            lambda : print('francia')
        ])),
        Transition('paises bajos', lambda name: name == 'paises bajos', Node.leaf([
            lambda : print('paises bajos')
        ]))
    ],
    [
        lambda: print('action1'),
        lambda: print('action2'),
        lambda: print('action2'),
        lambda: print('action2'),
        lambda: print('action2'),
        lambda: print('action2'),
        lambda: print('action2')
    ])

act_node = countries

print(act_node.question)

while act_node:
    act_node = act_node.visit()