from graph import Node, Transition
from countries import countries

act_node =  Node(
    'Estas feliz o triste?', 
    [
        Transition.simple('feliz', Node.leaf([lambda : print('feliz')])),
        Transition.simple('triste', countries)
    ],
    [
        lambda: print('action1'),
    ])


while act_node:
    act_node = act_node.visit()