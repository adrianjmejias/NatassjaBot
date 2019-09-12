from graph import Node, Transition
from config import id_test


animal = Node('Entonces sal a pasear. Prefieres encontrarte un…', 
    [
        Transition.simple('Perro', Node.leaf([lambda bot: bot.send_audio(id_test, open('./Audio1.mp3', 'rb'), '')])),
        Transition.simple('Gato', Node.leaf([lambda bot: bot.send_audio(id_test, open('./Audio2.mp3', 'rb'), '')])),
        
    ],
    [

    ])