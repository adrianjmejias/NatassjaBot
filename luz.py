from graph import Node, Transition

from viaje import viaje

luz = Node('¿Tienes luz?', 
    [
        #VIDEO NATASSJA TQM
        # Transition.simple('No', Node.leaf([lambda bot, id_test: bot.send_message(id_test, 'ok')])),
        Transition.with_actions('Sí', viaje, []
        ),
        Transition.simple('No', Node.leaf(
            [lambda bot, id_test: bot.send_message(id_test, 'https://www.youtube.com/watch?v=pX6U8FNLozo')])
        )
    ],
    [
        
    ])