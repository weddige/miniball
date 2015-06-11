miniball
========

These are python bindings to Bernd Gärtners `miniball software`__.

Examples
--------

    import math
    import random
    import miniball

    P = [(random.uniform(0, 100), random.uniform(0, 100)) for i in range(10000)]
    mb = miniball.Miniball(P)
    print('Center', mb.center())
    print('Radius', math.sqrt(mb.squared_radius()))
    if not mb.is_valid():
        print('Possibly invalid!')


__ http://www.inf.ethz.ch/personal/gaertner/miniball.html