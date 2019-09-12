from graph import Node, Transition
from config import id_test


animal = Node('¿Cuál prefieres?', 
    [
        Transition.simple('Perro', Node.leaf([lambda bot: bot.send_message(id_test, 'Perro')])),
        Transition.simple('Gato', Node.leaf([lambda bot: bot.send_message(id_test, 'Gato')])),
        
    ],
    [

    ])