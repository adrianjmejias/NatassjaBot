from graph import Node, Transition
from countries import countries
from animal import animal 
from config import id_test




act_node =  Node(
    '¿Estás feliz o triste?', 
    [
        Transition.simple('feliz', Node.leaf([lambda bot:  bot.send_message(id_test, 'https://www.youtube.com/watch?v=xdhoMLGPXFc')])),
        Transition.simple('triste', animal)
    ],
    [
        lambda bot: ''
    ])


# if __name__ == "__main__":
#     while act_node:
#         act_node = act_node.visit()
#     pass