from sympy import symbols,simplify
A,t = symbols('A t',positive = True)
def kauffman(crossings):
    if len(crossings) == 0 or (len(crossings) == 1 and len(crossings[0]) == 0):
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
        if len(crossings)==1:
            if sign(cross,crossings) == 1: # if the western and eastern arcs are loops        
                return -A **3 
            else: 
                return -A**-3    # if the northern and southern arcs are loops
        else:
            if sign(cross,crossings) == 1:
                return (A**5 + A)* kauffman(crossings[1:])
            else:
                return (A**-5 + A**-1)* kauffman(crossings[1:])  
    elif  (G==0 and F ==0) or (E == 0 and H == 0): # if the northern or southern arcs are loops           
        return simplify(kauffman(testB) * (-A**1 - A**-3) + A* kauffman(testA) )
    elif (G==0 and H ==0) or (E == 0 and F == 0): # if the western or eastern arcs are loops 
        return simplify(kauffman(testA) * (-A**3 - A**-1) + (A**-1)* kauffman(testB))
    else:
        return simplify(A* kauffman(testA) + (A**-1)* kauffman(testB))
    
def aSmoothing(originalcrossings,a,b,c,d,E,F,G,H):
    #connecting a (se) to b (ne) and d (sw) to c (nw)
    crossings = [crossing[:] for crossing in originalcrossings]
    if G == 0 and F == 0:
        h = crossings[H]
        h[h.index(d)] = a
    elif E == 0 and H == 0:
        f = crossings[F]
        f[f.index(b)] = c
    else:
        if E!= 0 or F != 0: 
            f = crossings[F]
            f[f.index(b)] = a
        if G != 0 or H !=0: 
            h = crossings[H]
            h[h.index(d)] = c
    del crossings[0]
    #relabeling
    arcs = sorted({x for crossing in crossings for x in crossing})
    mapping = {old:new+1 for new,old in enumerate(arcs)}
    crossings = [[mapping[x] for x in crossing] for crossing in crossings]
    return crossings

def bSmoothing(originalcrossings,a,b,c,d,E,F,G,H):  
#connecting a (se) to d (sw) and b (ne) to c (nw)
    crossings = [crossing[:] for crossing in originalcrossings]
    if G == 0 and H == 0:
        f = crossings[F]
        f[f.index(b)] = a
    elif E == 0 and F == 0:
        g = crossings[G]
        g[g.index(c)] = d
    else:
        if G != 0 or F!= 0: 
            g = crossings[G]
            g[g.index(c)] = b        
        if H !=0 or E != 0: 
            h = crossings[H]
            h[h.index(d)] = a
 
    del crossings[0]
    #relabeling
    arcs = sorted({x for crossing in crossings for x in crossing})
    mapping = {old:new+1 for new,old in enumerate(arcs)}
    crossings = [[mapping[x] for x in crossing] for crossing in crossings]
    return crossings
def get_components(crossings):
        """Determines the components of a ),(
           Returns a list of lists of (adjacently ordered) arc labels """
    
        components = []
        # hash giving both neighbouring arc labels of an arc 
        nbrs = {}
        for c in crossings:
            nbrs.setdefault(c[0], []).append(c[2])
            nbrs.setdefault(c[2], []).append(c[0])
        for c in crossings:
            nbrs.setdefault(c[1], []).append(c[3])
            nbrs.setdefault(c[3], []).append(c[1])

        visited = set()
        # iterate over all arcs
        for arc in nbrs:
            if arc in visited:
                continue
            stack = [arc]
            visited.add(arc)
            knot = []
            
            # do depth-first-search on the arc to find its knot
            while stack:
                curr = stack.pop()
                knot.insert(0,curr)
                for nbr in nbrs[curr]:
                    if nbr not in visited:
                        visited.add(nbr)
                        stack.append(nbr)
            components.append(knot)

        return components
def succ(arc,crossings):
    succs = {}
    for comp in get_components(crossings):
        for i in range(len(comp)):
            succs[comp[i-1]] = comp[i]
    return succs[arc]
def sign(crossing,crossings):
        if succ(crossing[3],crossings) == crossing[1]:
            if succ(crossing[1],crossings) == crossing[3]:
                if crossing[2] == crossing[3]:
                    return 1
                else:
                    return -1
            else:
                return 1
        
        else:
            return -1
def writhe(crossings):
    return sum([sign(cross,crossings) for cross in crossings])        
def arcConnect(crossings,arc):
    return [cross for cross in crossings if arc in cross]
def relabel(originalcrossings):
    crossings = []
    for component in get_components(originalcrossings):
        arcs = sorted({x for x in component})
        mapping = {old:new+1 for new,old in enumerate(arcs)}
        crossings.append([[mapping[x] for x in crossing] for crossing in originalcrossings])
    return crossings
def Jones(crossings):
    k = simplify((-A**-3)**(writhe(crossings))* kauffman(crossings))
    if len(get_components(crossings))==1:
        return simplify(k.subs(A**-4,t))
    else:
        return simplify(k.subs(A**-2,t))
def get_components(crossings):
        """Determines the components of a ),(
           Returns a list of lists of (adjacently ordered) arc labels """
    
        components = []
        # hash giving both neighbouring arc labels of an arc 
        nbrs = {}
        for c in crossings:
            nbrs.setdefault(c[0], []).append(c[2])
            nbrs.setdefault(c[2], []).append(c[0])
        for c in crossings:
            nbrs.setdefault(c[1], []).append(c[3])
            nbrs.setdefault(c[3], []).append(c[1])

        visited = set()
        # iterate over all arcs
        for arc in nbrs:
            if arc in visited:
                continue
            stack = [arc]
            visited.add(arc)
            knot = []
            
            # do depth-first-search on the arc to find its knot
            while stack:
                curr = stack.pop()
                knot.insert(0,curr)
                for nbr in nbrs[curr]:
                    if nbr not in visited:
                        visited.add(nbr)
                        stack.append(nbr)
            components.append(knot)

        return components


    
