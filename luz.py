from graph import Node, Transition
from config import id_test
from viaje import viaje

luz = Node('¿Tienes luz?', 
    [
        #VIDEO NATASSJA TQM
        # Transition.simple('No', Node.leaf([lambda bot: bot.send_message(id_test, 'ok')])),
        Transition.with_actions('Sí', viaje, []),
    ],
    [
        
    ])