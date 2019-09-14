from graph import Node, Transition
from config import id_test
from signo import signo

perrito = Node('Obviamente pasas por los perros antes de la disco, ¿qué salsa le pones?', 
    [
        Transition.with_actions('De ajo', signo,
            [lambda bot: bot.send_message(id_test, 'ajo')]
        ),
        Transition.with_actions('De maiz', signo,
            [lambda bot: bot.send_message(id_test, 'maiz')]
        ),
    ],
    [
        
    ])