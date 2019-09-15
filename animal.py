from graph import Node, Transition
from config import id_test
from luz import luz
from util import asset_path

animal = Node('Entonces sal a pasear. Prefieres encontrarte un…', 
    [
       Transition.with_actions('Perro', luz,
            [lambda bot: bot.send_photo(id_test, open(asset_path('Audio1.mp3'), 'rb'), '')]
        ),
        Transition.with_actions('Gato', luz,
            [lambda bot: bot.send_audio(id_test, open(asset_path('Audio2.mp3'), 'rb'), '')]
        ),
    ],
    [

    ])