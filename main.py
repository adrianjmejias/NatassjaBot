from graph import Node, Transition
from countries import countries
from animal import animal 



id_adri = 392991435

id_alosa = id_adri #388964408

act_node =  Node(
    'Estas feliz o triste?', 
    [
        Transition.simple('feliz', Node.leaf([lambda bot:  bot.send_message(id_alosa, 'feliz')])),
        Transition.simple('triste', Node.leaf([lambda bot:  bot.send_message(id_alosa, 'triste')]))
    ],
    [
        lambda bot: bot.send_message(id_alosa, 'https://twitter.com/AL0SA/status/1171093235466457089')
    ])


# if __name__ == "__main__":
#     while act_node:
#         act_node = act_node.visit()
#     pass