from graph import Node, Transition
from config import id_test
from disco import disco
from util import asset_path


museo1 = Node('Visitarás la Galería Borghese. ¿Qué quieres ver?',
[
        Transition.with_actions('Escultura', disco,
                [lambda bot: bot.send_photo(id_test, open(asset_path('LaVerdad.jpg'), 'rb'), 'La verità svelata dal Tempo, Bernini, 1645')]
        ),
        Transition.with_actions('Pintura', disco,
                [lambda bot: bot.send_photo(id_test, open(asset_path('Danae.jpg'), 'rb'), 'Danae, Correggio, ca. 1531')]
        ),
],
[

])


museo2 = Node('Visitarás la Galería Borghese. ¿Qué quieres ver?',
[
        Transition.with_actions('Escultura', disco,
                [lambda bot: bot.send_photo(id_test, open(asset_path('LaVerdad.jpg'), 'rb'), 'La verità svelata dal Tempo, Bernini, 1645')]
        ),
        Transition.with_actions('Pintura', disco,
                [lambda bot: bot.send_photo(id_test, open(asset_path('Danae.jpg'), 'rb'), 'Danae, Correggio, ca. 1531')]   
        ),
],
[

])