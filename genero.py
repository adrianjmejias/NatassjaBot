from graph import Node, Transition
from config import id_test
from perrito import perrito


genero = Node('¿Qué género quieres escuchar mientras te arreglas?', 
    [
        Transition.with_actions('Reggaetón', perrito,
            ([lambda bot: bot.send_message(id_test, '')])
        ),
        Transition.with_actions('Hippie', perrito,
            ([lambda bot: bot.send_message(id_test, '')])
        ),
        Transition.with_actions('Funk', perrito,
            ([lambda bot: bot.send_message(id_test, 'https://www.youtube.com/watch?v=zf4buOHOb-c')])
        ),
    ],
    [

    ])

