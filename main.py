from graph import Node, Transition
from animal import animal 
from config import id_test
from disco import disco


normal_flow = Node(
    '¿Estás feliz o triste?', 
    [
        Transition.simple('Feliz', disco),
        Transition.simple('Triste', animal)
    ],
    [
    ])


password_node = Node(
    'Solo la churra pasa, ingresa la contraseña', 
    [
        Transition(
            '', 
            lambda text: text == 'churra123',
            normal_flow,
            []
        )
    ],
    [])

init_node = normal_flow