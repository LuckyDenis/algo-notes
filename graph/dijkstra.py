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

    queue = [[start_vertex, 0]]
    while queue:
        v = queue.pop(0)[0]
        for to, cost in g[v].items():
            if costs[v] + cost < costs[to]:
                if [to, costs[to]] in queue:
                    queue.remove([to, costs[to]])
                path[to] = v
                costs[to] = costs[v] + cost
                queue.append([to, costs[to]])
    return costs, path


g = {
    0: {2: 1, 3: 1},
    1: {2: 4, 5: 6},
    2: {0: 1, 1: 4, 4: 9, 5: 2, 6: 1},
    3: {0: 1, 7: 4},
    4: {2: 9},
    5: {1: 6, 2: 2, 6: 3},
    6: {2: 1, 5: 3, 7: 9},
    7: {3: 4, 6: 9}
}

costs, path = djs(g, 0)
print(*costs.values(), sep=", ")
print(*path.values(), sep=", ")
