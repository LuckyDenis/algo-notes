# coding: utf8
"""
Нахождение кратчайших путей от заданной вершины
до всех остальных вершин. Алгоритм Дейкстры.

Сложность: O(m * log(n))
"""


def djs(graph, start_vertex):
    costs = dict().fromkeys(graph.keys(), float("inf"))
    path = dict().fromkeys(graph.keys(), -1)

    costs[start_vertex] = 0
    queue = [start_vertex]

    while queue:
        v = queue.pop(0)
        for to, cost in g[v].items():
            if costs[v] + cost < costs[to]:
                queue.append(to)
                costs[to] = costs[v] + cost
                path[to] = v

    return costs, path


g = {
    0: {4: 3},
    1: {0: 1, 2: 3, 3: 5},
    2: {0: 7, 1: 2},
    3: {1: 4, 5: 5, 7: 8},
    4: {2: 2, 6: 6},
    5: {6: 9},
    6: {7: 1},
    7: {}
}

costs, path = djs(g, 0)
print(*costs.values(), sep=", ")
print(*path.values(), sep=", ")
