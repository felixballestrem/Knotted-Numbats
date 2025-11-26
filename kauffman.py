def kauffman(crossings):
    if len(crossings) == 0:
        return 1
    test = crossings
    while len(crossings) != 0:
        cross = test[0]
        a = cross[0]
        b = cross[1]
        c = cross[2]
        d = cross[3]
        e = test.pre(a)
        h = test.succ(d)
        if crossingSign == 1:
            f = test.pre(c)
            g = test.succ(d)
        else:
            f = test.succ(c)
            g = test.pre(d)
        
