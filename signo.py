from graph import Node, Transition
from config import id_test

signo = Node('En la disco conoces a alguien, ¿qué signo te gustaría que fuera?', 
    [
        # these transitions are added at the bottom
    ],
    [
    ])




cancer = Node('Te ibas con esa persona pero se quedó llorando cuando escuchó La canción, así que llamaste a un taxi. Al llegar a tu casa te consigues un regalo:', 
    [
        Transition.simple('Abrir regalo', Node.leaf(
            [lambda bot: bot.send_message(id_test, 'lkjk')])
        ),
    ],
    [

    ])

leo = Node('Te ofreció la cola y te llevó hasta tu casa en un carro último modelo. Al llegar a tu casa te consigues un regalo:', 
    [
        Transition.simple('Abrir regalo', Node.leaf(
            [lambda bot: bot.send_message(id_test, 'lkas')])
        ),
    ],
    [

    ])

libra = Node('Te ofreció la cola pero después te dijo que no estaba seguro si podía llevarte. Te fuiste con alguien virgo. Al llegar a tu casa te consigues un regalo:',
    [
        Transition.simple('Abrir regalo', Node.leaf(
            [lambda bot: bot.send_message(id_test, 'jasjaja')])
        ),
    ],
    [

    ])

signo.transitions = [
        Transition.with_actions('Cáncer', cancer,  
            [lambda bot: bot.send_message(id_test, 'not implementet yet')]
        ),  
        Transition.with_actions('Leo', leo, 
            [lambda bot: bot.send_message(id_test, 'not implementet yet')]
        ),  
        Transition.with_actions('Libra', libra, 
            [lambda bot: bot.send_message(id_test, 'not implementet yet')]
        ),
    ]   