from graph import Node, Transition
from config import id_test
from museo1 import museo1, museo2


viaje = Node('¿A qué país quisieras ir?',
[
    Transition.with_actions('Italia', museo1,
            [lambda bot: bot.send_message(id_test, 'https://www.youtube.com/watch?v=nhdOMRyIPJg')]),
    #Transition.with_actions('Polonia', museo2,
     #       [lambda bot: bot.send_message(id_test, 'https://www.youtube.com/watch?v=iE4AZDDvxqE')]),
    #Transition.with_actions('Países Bajos', museo3,
     #       [lambda bot: bot.send_message(id_test, 'https://www.youtube.com/watch?v=kr4DNZz_8zI')]),
    #Transition.with_actions('Inglaterra', museo4,
      #      [lambda bot: bot.send_message(id_test, 'https://www.youtube.com/watch?v=vo-EsjZWqOE')]),
    #Transition.with_actions('Francia', museo5,
     #       [lambda bot: bot.send_message(id_test, 'https://www.youtube.com/watch?v=7bzliFUpceI')]),
],
[

])