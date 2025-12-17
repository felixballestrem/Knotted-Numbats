class Diagram:
    def __init__(self, pd):
        # matrix is a 2d list of segment numbers
        self.pd = pd
        self.components = self.get_components()
        
        self.succs = {}
        for comp in self.components:
            for i in range(len(comp)):
                self.succs[comp[i-1]] = comp[i]
    
      
    def succ(self, arc):
        return self.succs[arc]


    def sign(self,crossing):
        if self.succ(crossing[3]) == crossing[1]:
            if self.succ(crossing[1]) == crossing[3]:
                if crossing[2] == crossing[3]:
                    return 1
                else:
                    return -1
            else:
                return 1
        
        else:
            return -1

  
    def get_components(self):
        """Determines the components of a PD
           Returns a list of lists of (adjacently ordered) arc labels """
    
        components = []
        # hash giving both neighbouring arc labels of an arc 
        nbrs = {}
        for c in self.pd:
            nbrs.setdefault(c[0], []).append(c[2])
            nbrs.setdefault(c[2], []).append(c[0])
        for c in self.pd:
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
    
    
        
    
        
        
