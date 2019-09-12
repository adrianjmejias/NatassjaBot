from graph import Node, Transition
from countries import countries
from animal import animal 
from config import id_test




act_node =  Node(
    'Estas feliz o triste?', 
    [
        Transition.simple('feliz', Node.leaf([lambda bot:  bot.send_message(id_test, 'feliz')])),
        Transition.simple('triste', Node.leaf([lambda bot:  bot.send_message(id_test, 'triste')]))
    ],
    [
        lambda bot: bot.send_message(id_test, 'https://twitter.com/AL0SA/status/1171093235466457089')
    ])


# if __name__ == "__main__":
#     while act_node:
#         act_node = act_node.visit()
#     pass