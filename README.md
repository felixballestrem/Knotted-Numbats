# Knotted-Numbats
The code repository for the Knotted Numbats Group project. 

By importing the PlanarDiagram() class from the PD_class.py file and storing the planar diagram (pd) as PlanarDiagram(pd), we can compute the jones polynomial in the kauffman.py file by calling jones(PlanarDiagram(pd)) where pd is the planar diagram notation of the knot

example usage:  
in the kauffman.py file:  
from ____ import PlanarDiagram  
... code  
pd = []  
jones = jones(PlanarDiagram(pd))  

