from Node import Node  # Importamos la clase Node

from funcion import a_search, obtener_caminos, graph

# Función de algoritmo El Primero Mejor
def best_first_search(graph, inicio, final):
    # Inicializamos la lista abierta y cerrada
    lista_openset = []
    lista_closedset = []

    start_node = Node(inicio, None, 0, graph[inicio]['h'], graph[inicio]['h'])
    lista_openset.append(start_node)

    while lista_openset:
        # Obtenemos el nodo con menor heurística de la lista openset
        menor_heuristica = min(lista_openset, key=lambda node: node.h)
        lista_openset.remove(menor_heuristica)
        lista_closedset.append(menor_heuristica)

        # Si el nodo es el final, recuperamos el camino
        if menor_heuristica.name == final:
            return obtener_caminos(menor_heuristica), menor_heuristica.g

        # Obtenemos los nodos vecinos
        for vecino, costo in graph[menor_heuristica.name]['vecinos'].items():
            # Creamos el nodo vecino
            vecino_nodo = Node(vecino, menor_heuristica, menor_heuristica.g + costo, graph[vecino]['h'], graph[vecino]['h'])

            if vecino_nodo in lista_closedset:
                continue

            if vecino_nodo not in lista_openset:
                lista_openset.append(vecino_nodo)

    return None

# Soluciones distintas
try:
    resultado_a_m = a_search(graph, 'A', 'M')
    resultado_a_o = a_search(graph, 'A', 'O')
    
    caminosa_m, coste_a_m = resultado_a_m
    caminosa_o, coste_a_o = resultado_a_o
    
    if coste_a_m < coste_a_o:
        print(f"El camino más corto es: {caminosa_m} siendo su costo {coste_a_m}")
    else:
        print("El camino más corto es: ", caminosa_o)
        print("Coste: ", coste_a_o)

    # Ejecutar Best-First Search
    resultado_b_m = best_first_search(graph, 'A', 'M')
    resultado_b_o = best_first_search(graph, 'A', 'O')

    caminob_m, coste_b_m = resultado_b_m
    caminob_o, coste_b_o = resultado_b_o

    print(f"Best-First Search: Camino a M: {caminob_m} con coste {coste_b_m}")
    print(f"Best-First Search: Camino a O: {caminob_o} con coste {coste_b_o}")

except Exception as e:
    print("Error: Ingrese un nodo válido", e)