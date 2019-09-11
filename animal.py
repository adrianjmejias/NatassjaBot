from graph import Node, Transition



animal = Node('¿Cuál prefieres?', 
    [
        Transition.simple('Perro', Node.leaf([lambda : print('Perro')])),
        Transition.simple('Gato', Node.leaf([lambda : print('Gato')])),
        
    ],
    [

    ])