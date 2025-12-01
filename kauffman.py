from sympy import symbols,simplify

A= symbols('A')
def kauffman(crossings):
    #working cross by cross
    cross = crossings[0]
    #initiallising each element of cross
    a,b,c,d = cross
    
    #initiallising the index of the crossing that each element links to
    E = crossings.index(preCross(crossings,a))
    G = crossings.index(sucCross(crossings,c))
    if crossingSign(cross) == 1:
        F = crossings.index(preCross(crossings,b))
        H = crossings.index(sucCross(crossings,d))
    else:
        F = crossings.index(sucCross(crossings,b))
        H = crossings.index(preCross(crossings,d))
    if len(crossings) == 0 or a == b and b == c and c == d:
        #trivial case
        return 1    
    elif E == 0 and F == 0 or : # if the western or eastern arcs are loops
        
        return simplify(kauffman(bSmoothingWest(crossings)) * (-A**2 - A**-2))
    elif G==0 and H ==0: # TBC
        return simplify(kauffman(bSmoothingEast(crossings)) * (-A**2 - A**-2))
    elif E == 0 and H == 0 : 
        return simplify(kauffman(bSmoothingNorth(crossings)) * (-A**2 - A**-2))
    elif G==0 and F ==0  # if the western or eastern arcs are loops
        return simplify(kauffman(bSmoothingSouth(crossings)) * (-A**2 - A**-2))
    else:
        #skein moves
        testA = aSmoothing(crossings,a,b,c,d,E,F,G,H)
        testB = bSmoothing(crossings,a,b,c,d,E,F,G,H)
        :
        #remove crossing but have to redo conditiom to find unknots next to knots
        

        return simplify(A* kauffman(testA) + (A**-1)* kauffman(testB))
    
def aSmoothing(originalcrossings,a,b,c,d,E,F,G,H):
    #connecting a (se) to d (sw) and b (ne) to c (nw)
    crossings = [crossing[:] for crossing in originalcrossings]
    g = crossings[G]
    h = crossings[H]
    g[g.index(c)] = b
    h[h.index(d)] = a
    del crossings[0]
    #relabeling
    arcs = []
    for crossing in crossings: 
        for x in crossing:
            if x not in arcs: 
                arcs.append(x)
    arcs.sort()
    mapping = {old:new+1 for new,old in enumerate(arcs)}
    crossings = [[mapping[x] for x in crossing] for crossing in crossings]
    return crossings    
def bSmoothing(originalcrossings,a,b,c,d,E,F,G,H):
    #connecting a (se) to b (ne) and d (sw) to c (nw)
    crossings = [crossing[:] for crossing in originalcrossings]
    f = crossings[F]
    h = crossings[H]
    f[f.index(b)] = a
    h[h.index(d)] = c
    del crossings[0]
    #relabeling
    arcs = []
    for crossing in crossings: 
        for x in crossing:
            if x not in arcs: 
                arcs.append(x)
    arcs.sort()
    mapping = {old:new+1 for new,old in enumerate(arcs)}
    crossings = [[mapping[x] for x in crossing] for crossing in crossings]
    return crossings    
def crossingSign(cross):
    #assuming a is se, b is ne, c is nw and d is sw.
    a,b,c,d = cross
    if d == 1 or c ==1:
        if (c-a)*(b-d)>0:
            return -1
        else:
            return 1
    else:
        if (c-a)*(b-d)>0:
            return 1
        else:
            return -1
def writhe(crossings):
    return sum([crossingSign(cross) for cross in crossings])        
