from graph import Node, Transition

countries = Node('a que pais quieres ir?', 
    [
        Transition('italia', lambda name: name == 'italia', Node.leaf([
            lambda : print('italia')
        ])),
        Transition('polonia', lambda name: name == 'polonia', Node.leaf([
            lambda : print('polonia')
        ])),
        Transition('inglaterra', lambda name: name == 'inglaterra', Node.leaf([
            lambda : print('inglaterra')
        ])),
        Transition('francia', lambda name: name == 'francia', Node.leaf([
            lambda : print('francia')
        ])),
        Transition('paises bajos', lambda name: name == 'paises bajos', Node.leaf([
            lambda : print('paises bajos')
        ]))
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