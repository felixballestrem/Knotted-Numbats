from sympy import symbols,simplify

A= symbols('A')
def kauffman(crossings):
    if len(crossings) == 0:
        #trivial case
        return 1
    #working cross by cross
    cross = crossings[0]
    #initiallising each element of cross
    a,b,c,d = cross
    connections = [0 if len(arcConnect(crossings,i)) ==1 else crossings.index(arcConnect(crossings,i)[0]) if arcConnect(crossings,i)[1] == cross else crossings.index(arcConnect(crossings,i)[1]) for i in cross]
    E,F,G,H = connections
    testA = aSmoothing(crossings,a,b,c,d,E,F,G,H)
    testB = bSmoothing(crossings,a,b,c,d,E,F,G,H)
    if E==0 and F == 0 and G == 0 and H== 0:
        # if both arcs are loops
        if crossingSign(cross,crossings) == 1: # if the western and eastern arcs are loops        
            return -A **-3
        else: 
            return -A**3     # if the northern and southern arcs are loops        
    elif (G==0 and H ==0) or (E == 0 and F == 0): # if the western or eastern arcs are loops        
        return simplify(kauffman(testB) * (-A**1 - A**-3) + A* kauffman(testA) )
    elif (G==0 and F ==0) or (E == 0 and H == 0): # if the northern or southern arcs are loops    
        return simplify(kauffman(testA) * (-A**3 - A**-1) + (A**-1)* kauffman(testB))
    else:
        return simplify(A* kauffman(testA) + (A**-1)* kauffman(testB))
    
def aSmoothing(originalcrossings,a,b,c,d,E,F,G,H):
    #connecting a (se) to d (sw) and b (ne) to c (nw)
    crossings = [crossing[:] for crossing in originalcrossings]
    if G != 0: 
        g = crossings[G]
        if crossingSign([a,b,c,d],crossings) ==-1:
            g[g.index(c)] = b
        else:
            g[g.index(b)] = c
        
    if H !=0: 
        h = crossings[H]
        h[h.index(d)] = a
    del crossings[0]
    #relabeling
    arcs = sorted({x for crossing in crossings for x in crossing})
    mapping = {old:new+1 for new,old in enumerate(arcs)}
    crossings = [[mapping[x] for x in crossing] for crossing in crossings]
    return crossings

def bSmoothing(originalcrossings,a,b,c,d,E,F,G,H):
    #connecting a (se) to b (ne) and d (sw) to c (nw)
    crossings = [crossing[:] for crossing in originalcrossings]
    if F != 0: 
        f = crossings[F]
        f[f.index(b)] = a
    if H !=0: 
        h = crossings[H]
        h[h.index(d)] = c
    del crossings[0]
    #relabeling
    arcs = sorted({x for crossing in crossings for x in crossing})
    mapping = {old:new+1 for new,old in enumerate(arcs)}
    crossings = [[mapping[x] for x in crossing] for crossing in crossings]
    return crossings
def links(crossings):
    linkList = []
    arcs = sorted({x for crossing in crossings for x in crossing})
    visited = set()
    for arc in arcs:
        if arc in visited:
            continue
        i = arc
        link = []
        while i not in link: 
            visited.add(i)
            link.append(i)
            for cross in crossings:
                if i in cross:
                    a,b,c,d = cross
                    if i ==a:
                        iTemp = c
                    elif i ==b:
                        iTemp = d
                    elif i ==c:
                        iTemp = a
                    else:
                        iTemp = b
                    if iTemp not in link:
                        i = iTemp
                        break
        linkList.append(link)
    return(linkList)
def crossingSign(cross,crossings):
    #assuming a is se, b is ne, c is nw and d is sw.
    a,b,c,d = cross
    linkList = links(crossings)
    bLink = [link for link in linkList if b in link][0]
    if bLink.index(b) == 0:
        if (b-d)*(c-a)>0:
            return -1
        else:
            return 1
    else:
        if (b-d)*(c-a)>0:
            return 1
        else:
            return -1
def writhe(crossings):
    return sum([crossingSign(cross,crossings) for cross in crossings])        
def arcConnect(crossings,arc):
    return [cross for cross in crossings if arc in cross]
def Jones(crossings):
    print(kauffman(crossings),writhe(crossings))
    return simplify((-A**3)**(writhe(crossings))* kauffman(crossings))
