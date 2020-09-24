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
        for to, cost in graph[v].items():
            if cost < costs[to]:
                if [to, costs[to]] in queue:
                    queue.remove([to, costs[to]])
                path[to] = v
                costs[to] = cost
                queue.append([to, costs[to]])

    return costs, path
