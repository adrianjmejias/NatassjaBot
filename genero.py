from graph import Node, Transition
from config import id_test
from perrito import perrito
from signo import signo


genero = Node('¿Qué género quieres escuchar mientras te arreglas?', 
    [
        Transition.with_actions('Reggaetón', perrito,
            ([lambda bot: bot.send_message(id_test, 'https://www.youtube.com/watch?v=-C8fmkL2cuI')])
        ),
        Transition.with_actions('Hippie', signo,
            ([lambda bot: bot.send_message(id_test, 'https://youtu.be/0qkOtAzCJAs')])
        ),
        Transition.with_actions('Funk', signo,
            ([lambda bot: bot.send_message(id_test, 'https://www.youtube.com/watch?v=zf4buOHOb-c')])
        ),
    ],
    [

    ])

