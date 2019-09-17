from graph import Node, Transition
from config import id_test
from signo import signo
from util import asset_path


perrito = Node('Obviamente pasas por los perros antes de la disco. ¿Qué salsa le pones?', 
    [
        Transition.with_actions('De ajo', signo,
            [lambda bot: bot.send_photo(id_test, open(asset_path('ajo.jpg'), 'rb'), '')]
        ),
        Transition.with_actions('De maíz', signo,
            [lambda bot: bot.send_sticker(id_test, open(asset_path('natica1.webp'), 'rb'), '')]
        ),
    ],
    [
        
    ])