from graph import Node, Transition
from config import id_test


disco = Node('Decidiste ir a la disco. ¿Qué color de sombra usarías?', 
    [
        Transition.simple('Azul', Node.leaf([lambda bot: bot.send_message(id_test, 'https://twitter.com/VitaVirginiaBot/status/1167462809430630400?s=20')])),
        Transition.simple('Rojo', Node.leaf([lambda bot: bot.send_message(id_test, 'https://www.poeticous.com/evaristo-carriego/el-clavel?locale=es')])),
        Transition.simple('Negro', Node.leaf([lambda bot: bot.send_photo(id_test, open('./gatonegro.jpg', 'rb'), '')])),
        Transition.simple('Verde', Node.leaf([lambda bot: bot.send_message(id_test, 'https://www.desmos.com/calculator/x3vloqe7lq')]))
    ],
    [

    ])
