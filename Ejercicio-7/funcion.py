from Node import Node #Importamos la clase Node

#Funcion de algoritmo A*
def a_search(graph,inicio,final):
    #Inicializamos la lista abierta y cerrada
    lista_openset = []
    lista_closedset = []

    #Creamos el nodo inicial
    start_node = Node(inicio,None,0,graph[inicio]['h'],graph[inicio]['h'])
    lista_openset.append(start_node)

    while lista_openset:
        #Obtenemos el nodo con menor peso de la lista openset
        menor_peso = lista_openset.pop(0)
        lista_closedset.append(menor_peso)

        #Si el nodo es el final , recuperamos el camino
        if menor_peso.name == final:
            return obtener_caminos(menor_peso),menor_peso.g
        
        #Obtenemos los nodos vecinos
        for vecino,costo in graph[menor_peso.name]['vecinos'].items():
            print(costo)
            #Calculamos el costo del nodo
            costo_g = menor_peso.g + costo
            print(f"costo_g {costo_g}")
            costo_h = graph[vecino]['h']
            costo_f = costo_g + costo_h

            #Creamos el nodo vecino
            vecino_nodo = Node(vecino,menor_peso,costo_g,costo_h,costo_f)

            if vecino_nodo in lista_closedset:
                continue

            if vecino_nodo not in lista_openset:
                lista_openset.append(vecino_nodo)
            else:
                for nodo in lista_openset:
                    if nodo.name == vecino_nodo.name and nodo.f > vecino_nodo.f:
                        lista_openset.remove(nodo)
                        lista_openset.append(vecino_nodo)
                        break
        lista_openset.sort() #Ordenamos la lista openset
    return None




def obtener_caminos(nodo):
    camino = []
    while nodo:
        camino.append(nodo.name)
        nodo = nodo.parent
    return camino[::-1] #Invertimos el camino


#Uso
graph = {
    'A': {'vecinos': {'B': 30,'C': 34,'D': 29}, 'h': 50},
    'B': {'vecinos': {'E': 23,'F': 19}, 'h': 30},
    'C': {'vecinos': {'G': 20}, 'h': 34},
    'D': {'vecinos': {'H': 31}, 'h': 29},
    'E': {'vecinos': {'I': 2, 'J': 8}, 'h': 23},
    'F': {'vecinos': {'J': 8}, 'h': 19},
    'G': {'vecinos': {'K': 10, 'L': 7}, 'h': 20},
    'H': {'vecinos': {}, 'h': 31},
    'I': {'vecinos': {}, 'h': 2},
    'J': {'vecinos': {'M': 0}, 'h': 8},
    'K': {'vecinos': {}, 'h': 10},
    'L': {'vecinos': {'N': 5, 'O': 0}, 'h': 7},
    'M': {'vecinos': {}, 'h': 0},
    'N': {'vecinos': {}, 'h': 5},
    'O': {'vecinos': {}, 'h': 0}
}

#Soluciones distintas
try:
    resultado_a_m = a_search(graph,'A','M')
    resultado_a_o = a_search(graph,'A','O')
    
    caminosa_m,coste_a_m = resultado_a_m
    caminosa_o,coste_a_o = resultado_a_o
    
    if coste_a_m < coste_a_o:
        print(f"El camino más corto es: {caminosa_m} siendo su costo {coste_a_m}")
    else:
        print("El camino más corto es: ",caminosa_o)
        print("Coste: ",coste_a_o)

except:
    print("Error: Ingrese un nodo válido")
                