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
    # The function's code goes here
    unvisited = [x for x in graph.keys()]
    visited = [initial]

    vertex_cost_prev: dict[str, tuple[float, str, float]] = {key: (float('inf'), '', 0) for key in graph.keys()}
    vertex_cost_prev[initial] = (0, '', 0)
    # print(vertex_cost_prev)

    return_graph: WeightedGraph = {}

    while unvisited:
        current = min(unvisited, key=lambda x: vertex_cost_prev[x][0])
        unvisited.remove(current)
        visited.append(current)

        for neighbor, cost in graph[current]:

            if neighbor in unvisited:
                new_cost = vertex_cost_prev[current][0] + cost

                # print(f'new cost: {new_cost}')
                # print(f'vertex_cost: {vertex_cost_prev[neighbor][0]}')
                if new_cost < vertex_cost_prev[neighbor][0]:
                    # print(f'current: {current}, neighbor: {neighbor}, cost: {cost}')
                    vertex_cost_prev[neighbor] = (new_cost, current, cost)

    for key, value in vertex_cost_prev.items():
        if value[1] != '':
            if return_graph.get(key) is not None:
                return_graph[key].add((value[1], value[2]))
            else:
                return_graph[key] = {(value[1], value[2])}
    for key, value in vertex_cost_prev.items():
        if value[1] != '':
            if return_graph.get(value[1]) is not None:
                return_graph[value[1]].add((key, value[2]))
            else:
                return_graph[value[1]] = {(key, value[2])}

    return {key: value[0] for key, value in vertex_cost_prev.items()}, return_graph


biggie: WeightedGraph = {
    'A': {('B', 4), ('E', 8)},
    'B': {('A', 4), ('E', 11), ('C', 8)},
    'C': {('B', 8), ('I', 2), ('G', 4), ('D', 7)},
    'D': {('C', 7), ('G', 14), ('H', 9)},
    'E': {('A', 8), ('B', 11), ('I', 7), ('F', 1)},
    'F': {('E', 1), ('I', 6), ('G', 2)},
    'G': {('F', 2), ('C', 4), ('D', 14), ('H', 10)},
    'H': {('D', 9), ('G', 10)},
    'I': {('C', 2), ('E', 7), ('F', 6)},
}
