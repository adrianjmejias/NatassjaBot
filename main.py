from graph import Node, Transition
from animal import animal 
from config import id_test
from disco import disco



init_node = Node(
    '¿Estás feliz o triste?', 
    [
        Transition.simple('Feliz', disco),
        Transition.simple('Triste', animal)
    ],
    [
        lambda bot: ''
    ])


# if __name__ == "__main__":
#     while act_node:
#         act_node = act_node.visit()
#     pass