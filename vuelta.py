from graph import Node, Transition

from util import asset_path

vuelta_hotel = Node('Después de un largo día, vuelves al hotel y te consigues un regalo:', 
   [
        Transition.simple('Abrir regalo', Node.leaf(
            [lambda bot, id_test: bot.send_video(id_test, open(asset_path('gatico.mp4'), 'rb'), '')])
        ),
    ],
    [

    ])