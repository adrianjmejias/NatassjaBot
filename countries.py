from graph import Node, Transition
from config import id_test

countries = Node('¿A qué país quieres ir?', 
    [
        Transition.simple('Italia', Node.leaf([lambda bot : bot.send_message(id_test, 'Italia')])),
        Transition.simple('Polonia', Node.leaf([lambda bot : bot.send_message(id_test, 'Polonia')])),
        Transition.simple('Inglaterra', Node.leaf([lambda bot : bot.send_message(id_test, 'Inglaterra')])),
        Transition.simple('Francia', Node.leaf([lambda bot : bot.send_message(id_test, 'Francia')])),
        Transition.simple('Países Bajos', Node.leaf([lambda bot : bot.send_message(id_test, 'Países Bajos')]))
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