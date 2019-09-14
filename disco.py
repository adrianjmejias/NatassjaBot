from graph import Node, Transition
from config import id_test
from util import asset_path
from genero import genero

disco = Node('Decidiste ir a la disco. ¿Qué color de sombra usarías?', 
    [
        Transition.with_actions('Azul', genero, 
            [lambda bot: bot.send_message(id_test, 'https://twitter.com/VitaVirginiaBot/status/1167462809430630400?s=20')]
        ),
        Transition.with_actions('Rojo', genero, 
            [lambda bot: bot.send_message(id_test, 'https://www.poeticous.com/evaristo-carriego/el-clavel?locale=es')]
        ),
        Transition.with_actions('Negro', genero, 
            [lambda bot: bot.send_photo(id_test, open( asset_path('gatonegro.jpg'), 'rb'), '')]
        ),
        Transition.with_actions('Verde', genero, 
            [lambda bot: bot.send_message(id_test, 'https://www.desmos.com/calculator/x3vloqe7lq')]
        ),
    ],
    [

    ])



