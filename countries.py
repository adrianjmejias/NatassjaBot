from graph import Node, Transition
from config import id_test

countries = Node('a que pais quieres ir?', 
    [
        Transition.simple('italia', Node.leaf([lambda bot : bot.send_message(id_test, 'italia')])),
        Transition.simple('polonia', Node.leaf([lambda bot : bot.send_message(id_test, 'polonia')])),
        Transition.simple('inglaterra', Node.leaf([lambda bot : bot.send_message(id_test, 'inglaterra')])),
        Transition.simple('francia', Node.leaf([lambda bot : bot.send_message(id_test, 'francia')])),
        Transition.simple('paises bajos', Node.leaf([lambda bot : bot.send_message(id_test, 'paises bajos')]))
    ],
    [
        lambda bot: bot.send_message(id_test, 'action1'),
        lambda bot: bot.send_message(id_test, 'action2'),
        lambda bot: bot.send_message(id_test, 'action2'),
        lambda bot: bot.send_message(id_test, 'action2'),
        lambda bot: bot.send_message(id_test, 'action2'),
        lambda bot: bot.send_message(id_test, 'action2'),
        lambda bot: bot.send_message(id_test, 'action2')
    ])