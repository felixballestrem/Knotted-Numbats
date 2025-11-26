from sympy import symbols
def kauffman(crossings):
    if len(crossings) == 0:
        #trivial case
        return 1
    while len(crossings) != 0:
        #working cross by cross
        cross = crossings[0]
        #initiallising each element of cross
        a = cross[0]
        b = cross[1]
        c = cross[2]
        d = cross[3]
        #initiallising the crossing that each element links to
        E = crossings.preCross(a)
        G = test.sucCross(c)
        if crossingSign == 1:
            F = crossings.preCross(b)
            H = crossings.sucCross(d)
        else:
            f = crossings.sucCross(b)
            h = crossings.preCross(d)
        testA = aSmoothing(crossings,a,b,c,d,E,F,G,H)
        testB = bSmoothing(crossings,a,b,c,d,E,F,G,H)
        return 
        
def aSmoothing(crossings,a,b,c,d,E,F,G,H):
    crossings.index(E)
        
        
