from graph import Node, Transition

countries = Node('a que pais quieres ir?', 
    [
        Transition.simple('italia', Node.leaf([lambda : print('italia')])),
        Transition.simple('polonia', Node.leaf([lambda : print('polonia')])),
        Transition.simple('inglaterra', Node.leaf([lambda : print('inglaterra')])),
        Transition.simple('francia', Node.leaf([lambda : print('francia')])),
        Transition.simple('paises bajos', Node.leaf([lambda : print('paises bajos')]))
    ],
    [
        lambda: print('action1'),
        lambda: print('action2'),
        lambda: print('action2'),
        lambda: print('action2'),
        lambda: print('action2'),
        lambda: print('action2'),
        lambda: print('action2')
    ])