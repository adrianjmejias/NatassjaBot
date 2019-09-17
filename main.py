from graph import Node, Transition
from animal import animal 

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
    'Solo la churra pasa. Ingresa la contraseña', 
    [
        Transition(
            '', 
            lambda text: text == 'churra.21',
            normal_flow,
            []
        )
    ],
    [
   
    ])

init_node = password_node