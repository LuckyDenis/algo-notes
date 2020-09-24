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
        for to, cost in graph[v].items():
            if costs[v] + cost < costs[to]:
                queue.append(to)
                costs[to] = costs[v] + cost
                path[to] = v

    return costs, path
