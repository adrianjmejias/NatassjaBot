from graph import Node, Transition
from countries import countries
from animal import animal 
from config import id_test
from disco import disco



act_node =  Node(
    '¿Estás feliz o triste?', 
    [
        Transition.simple('feliz', disco),
        Transition.simple('triste', animal)
    ],
    [
        lambda bot: ''
    ])


# if __name__ == "__main__":
#     while act_node:
#         act_node = act_node.visit()
#     pass