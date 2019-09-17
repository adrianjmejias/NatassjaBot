from graph import Node, Transition

from luz import luz
from util import asset_path

animal = Node('Entonces sal a pasear. Prefieres encontrarte un…', 
    [
       Transition.with_actions('Perro', luz,
            [lambda bot, id_test: bot.send_photo(id_test, open(asset_path('corgi2.jpg'), 'rb'), 'Un corgi cumpleañero para otro corgi cumpleañero')]
        ),
        Transition.with_actions('Gato', luz,
            [lambda bot, id_test: bot.send_audio(id_test, open(asset_path('Audio2.mp3'), 'rb'), '')]
        ),
    ],
    [

    ])