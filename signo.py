from graph import Node, Transition

from util import asset_path

signo = Node('En la disco conoces a alguien. ¿Qué signo te gustaría que fuera?', 
    [
        # these transitions are added at the bottom
    ],
    [
    ])




cancer = Node('Te ibas con esa persona pero se quedó llorando cuando escuchó La canción, así que llamaste a un taxi. Al llegar a tu casa te consigues un regalo:', 
    [
        Transition.simple('Abrir regalo', Node.leaf(
            [lambda bot, id_test: bot.send_message(id_test, 'https://www.youtube.com/watch?v=Uqg4Y6N53k0&')])
        ),
    ],
    [

    ])

leo = Node('Te ofreció la cola y te llevó hasta tu casa en un carro último modelo. Al llegar a tu casa te consigues un regalo:', 
    [
        Transition.simple('Abrir regalo', Node.leaf(
            [lambda bot, id_test: bot.send_message(id_test, 'https://www.youtube.com/watch?v=Uqg4Y6N53k0&')])
        ),
    ],
    [

    ])

libra = Node('Te ofreció la cola pero después te dijo que no estaba seguro si podía llevarte. Te fuiste con alguien virgo. Al llegar a tu casa te consigues un regalo:',
    [
        Transition.simple('Abrir regalo', Node.leaf(
            [lambda bot, id_test: bot.send_message(id_test, 'https://www.youtube.com/watch?v=Uqg4Y6N53k0&')])
        ),
    ],
    [

    ])

signo.transitions = [
        Transition.with_actions('Cáncer', cancer,  
            [lambda bot, id_test: bot.send_document(id_test, open(asset_path('File.pdf'), 'rb'), '')]
        ),  
        Transition.with_actions('Leo', leo, 
            [lambda bot, id_test: bot.send_photo(id_test, open(asset_path('juj.jpg'), 'rb'), '')]
        ),  
        Transition.with_actions('Libra', libra, 
            [lambda bot, id_test: bot.send_sticker(id_test, open(asset_path('cachapa.webp'), 'rb'), '')]
        ),
    ]   

    