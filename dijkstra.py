# ----------------------------------------------------------
# Lab #6: Dijkstra’s Shortest-Path Tree
#
# Date: 18-Oct-2022
# Authors:
#           A01745446 Sergio Manuel Gonzalez Vargas
#           A01720627 Rodrigo Alfredo Mendoza España
# ----------------------------------------------------------

WeightedGraph = dict[str, set[tuple[str, float]]]


def dijkstra_spt(
        initial: str,
        graph: WeightedGraph) -> tuple[dict[str, float], WeightedGraph]:

    # get visited and unvisited nodes
    unvisited = [x for x in graph.keys()]
    visited = [initial]

    # get all nodes and assign them an infinite distance except the initial node
    vertex_cost_prev: dict[str, tuple[float, str, float]] = {key: (float('inf'), '', 0) for key in graph.keys()}
    vertex_cost_prev[initial] = (0, '', 0)

    # dictionary for nodes, its neightbours and cost
    return_graph: WeightedGraph = {}

    # while there are unvisited nodes get the lowest cost nodes and assign them to the vertex_cost_prev dictionary
    while unvisited:
        current = min(unvisited, key=lambda x: vertex_cost_prev[x][0])
        unvisited.remove(current)
        visited.append(current)

        for neighbor, cost in graph[current]:

            if neighbor in unvisited:
                new_cost = vertex_cost_prev[current][0] + cost

                if new_cost < vertex_cost_prev[neighbor][0]:
                    vertex_cost_prev[neighbor] = (new_cost, current, cost)

    # iterate through the vertex_cost_prev dictionary and create the return_graph, which is a dictionary of nodes and its neighbours and cost
    for key, value in vertex_cost_prev.items():
        if value[1] != '':
            if return_graph.get(key) is not None:
                return_graph[key].add((value[1], value[2]))
            else:
                return_graph[key] = {(value[1], value[2])}
            
    # iterate through it but assign the neighbours as the key of the dictionary
    for key, value in vertex_cost_prev.items():
        if value[1] != '':
            if return_graph.get(value[1]) is not None:
                return_graph[value[1]].add((key, value[2]))
            else:
                return_graph[value[1]] = {(key, value[2])}

    return {key: value[0] for key, value in vertex_cost_prev.items()}, return_graph