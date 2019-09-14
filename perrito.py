from graph import Node, Transition
from config import id_test

perrito = Node('Obviamente pasas por los perros antes de la disco, ¿qué salsa le pones?', 
    [
        Transition.simple('De ajo', Node.leaf(
            [lambda bot: bot.send_message(id_test, 'ajo')])
        ),
        Transition.simple('De maiz', Node.leaf(
            [lambda bot: bot.send_message(id_test, 'maiz')])
        ),
    ],
    [
        
    ])