from graph import Node, Transition
from config import id_test


género = Node('¿Qué género quieres escuchar mientras te arreglas?'), 
    [
        Transition.simple('Reggaetón', Node.leaf([lambda bot: bot.send_message(id_test, '')])),
        Transition.simple('Hippie', Node.leaf([lambda bot: bot.send_message(id_test, '')])),
        Transition.simple('Funk', Node.leaf([lambda bot: bot.send_message(id_test, 'https://www.youtube.com/watch?v=zf4buOHOb-c')])),
    ],
    [

    ])
