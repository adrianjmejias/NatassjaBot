from graph import Node, Transition
from config import id_test


node_test =  Node.leaf([lambda bot: bot.send_message(id_test, 'you moved to a test node')])

animal = Node('Entonces sal a pasear. Prefieres encontrarte un…', 
    [
        Transition.simple('Perro', Node.leaf([lambda bot: bot.send_audio(id_test, open('./Audio1.mp3', 'rb'), '')])),
        Transition.simple('Gato', Node.leaf([lambda bot: bot.send_audio(id_test, open('./Audio2.mp3', 'rb'), '')])),
        Transition.with_actions('test', node_test,
            [lambda bot: bot.send_message(id_test, 'this is shown as a Transition\'s action')]
        )
    ],
    [

    ])


