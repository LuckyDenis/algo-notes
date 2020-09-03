# coding: utf8
"""
Минимальное остовное дерево. Алгоритм Прима.

Сложность: O(m * log(n))
"""


def prima_mst(graph, start_vertex):
    costs = dict().fromkeys(graph.keys(), float("inf"))
    path = dict().fromkeys(graph.keys(), -1)

    queue = [[start_vertex, 0]]
    for _ in graph:
        v = queue.pop(0)[0]
        for to, cost in g[v].items():
            if cost < costs[to]:
                if [to, costs[to]] in queue:
                    queue.remove([to, costs[to]])
                path[to] = v
                costs[to] = cost
                queue.append([to, costs[to]])

    return costs, path


g = {
    0: {1: 1, 2: 6, 3: 8},
    1: {0: 1, 2: 7, 5: 2, 6: 2},
    2: {0: 6, 1: 7, 4: 5, 5: 6, 6: 4},
    3: {0: 8},
    4: {2: 5},
    5: {1: 2, 2: 6, 6: 5, 7: 9},
    6: {1: 2, 2: 4, 5: 5, 7: 1},
    7: {5: 9, 6: 1}
}


cost, path = prima_mst(g, 0)
print(*cost.values(), sep=", ")
print(*path.values(), sep=", ")
