#Nodo de la Lista 
class Node:
    def __init__(self,name,parent,g,h,f):
        self.name = name #Nombre de la ciudad
        self.g = g  #Coste del nodo inicial
        self.h = h #Estimación heurística
        self.f = f
        self.parent = parent

    def __lt__(self, otros): #Comparación de nodos
        return self.f < otros.f 