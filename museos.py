from graph import Node, Transition

from vuelta import vuelta_hotel
from util import asset_path

museo1 = Node('Visitarás la Galería Borghese. ¿Qué quieres ver?', 
    [
        Transition.with_actions('Escultura', vuelta_hotel,
            [lambda bot, id_test: bot.send_photo(id_test, open(asset_path('LaVerdad.jpg'), 'rb'), 'La verità svelata dal Tempo, Bernini, 1645')]
        ),
        Transition.with_actions('Pintura', vuelta_hotel,
            [lambda bot, id_test: bot.send_photo(id_test, open(asset_path('Danae.jpg'), 'rb'), 'Danae, Correggio, ca. 1531')]
        ),
    ],
    [

    ])


museo2 = Node('Visitarás el Castillo de Wawel. ¿Qué quieres ver?', 
    [
        Transition.with_actions('Escultura', vuelta_hotel,
            [lambda bot, id_test: bot.send_photo(id_test, open(asset_path('DragondeWawel.jpg'), 'rb'), 'Smok Wawelski, Bronisław Chromy, 1970')]
        ),
        Transition.with_actions('Pintura', vuelta_hotel,
            [lambda bot, id_test: bot.send_photo(id_test, open(asset_path('JupiterMercurioylaVirtud.jpg'), 'rb'), 'Giove pittore di farfalle, Mercurio e la Virtù, Dosso Dossi, 1515-1518')]
        ),
    ],
    [

    ])


museo3 = Node('Visitarás el Museo Kröller-Müller. ¿Qué quieres ver?', 
    [
        Transition.with_actions('Escultura', vuelta_hotel,
            [lambda bot, id_test: bot.send_photo(id_test, open(asset_path('Jardindemail.jpg'), 'rb'), 'Jardin d’émail, Jean Dubuffet, 1974')]
        ),
        Transition.with_actions('Pintura', vuelta_hotel,
            [lambda bot, id_test: bot.send_photo(id_test, open(asset_path('RoadwithCypressandStar.jpg'), 'rb'), 'Cypres bij sterrennacht, Vincent van Gogh, 1890')]
        ),
    ],
    [

    ])


museo4 = Node('Visitarás el Museo Británico. ¿Qué quieres ver?', 
    [
        Transition.with_actions('Mausoleo', vuelta_hotel,
            [lambda bot, id_test: bot.send_photo(id_test, open(asset_path('RestosmausoleodeHalicarnaso.jpg'), 'rb'), 'Restos del mausoleo de Halicarnaso, Sátiro de Paros y Piteo, 353 a.C-350 a.C.')]
        ),
        Transition.with_actions('Grabado', vuelta_hotel,
            [lambda bot, id_test: bot.send_photo(id_test, open(asset_path('Elsuenodelarazonproducemonstruos.jpg'), 'rb'), 'El sueño de la razón produce monstruos, Francisco de Goya, 1799')]
        ),
    ],
    [

    ])


museo5 = Node('Visitarás el Petit Palais. ¿Qué quieres ver?', 
    [
        Transition.with_actions('Escultura', vuelta_hotel,
            [lambda bot, id_test: bot.send_photo(id_test, open(asset_path('Eve.jpg'), 'rb'), 'Ève, Aimé Jules Dalou, 1838')]
        ),
        Transition.with_actions('Pintura', vuelta_hotel,
            [lambda bot, id_test: bot.send_photo(id_test, open(asset_path('LeSommeil.jpg'), 'rb'), 'Le Sommeil, Gustave Courbet, 1866')]
        ),
    ],
    [

    ])