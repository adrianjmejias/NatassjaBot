from graph import Node, Transition
from config import id_test
from disco import disco
from luz import luz
from util import asset_path

node_test = ()

animal = Node('Entonces sal a pasear. Prefieres encontrarte un…', 
    [
       # no se envían audios
       # Transition.with_actions('Perro', luz,
            #[lambda bot: bot.send_audio(id_test, open('./Audio1.mp3', 'rb'))]),
       # Transition.with_actions('Gato', luz,
            #[lambda bot: bot.send_audio(id_test, open('./Audio2.mp3', 'rb'))]),
        Transition.with_actions('Perro', luz,
            [lambda bot: bot.send_message(id_test, 'perro')]),
        Transition.with_actions('Gato', luz,
            [lambda bot: bot.send_message(id_test, 'gato')])
    ],
    [

    ])
