from graph import Node, Transition
from countries import countries
from animal import animal 

act_node =  Node(
    'Estas feliz o triste?', 
    [
        Transition.simple('feliz', Node.leaf([lambda : print('feliz')])),
        Transition.simple('triste', animal)
    ],
    [
        lambda: print('act_question'),
    ])


while act_node:
    act_node = act_node.visit()