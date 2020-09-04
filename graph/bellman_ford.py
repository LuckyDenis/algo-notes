# coding: utf8
"""
Нахождение кратчайших путей от заданной вершины
до всех остальных вершин. Алгоритм Форда-Беллмана.

Сигнализирует о наличии отрицательных ребер.
Сложность: O(m * log(n))
"""


def bellman_ford(g, start_vertex):
    dist = dict().fromkeys(g.keys(), float("inf"))
    path = dict().fromkeys(g.keys(), -1)
    queue = [start_vertex]
    dist[start_vertex] = 0

    while queue:
        v = queue.pop(0)
        for to, cost in g[v].items():
            if dist[v] + cost < dist[to]:
                queue.append(to)
                dist[to] = dist[v] + cost
                path[to] = v

    for v in g:
        for w in g[v]:
            if dist[w] + g[v][w] < dist[w]:
                print(f"Отрицательный вес ребра между вершинами: {v} и {w}.")

    return dist, path


g = {
    0: {3: 7, 4: -7},
    1: {2: 6, 3: 1},
    2: {1: -6, 5: 9},
    3: {0: 7, 1: 1},
    4: {0: 7, 7: 9},
    5: {2: 9},
    6: {},
    7: {4: 9}
}


dist, path = bellman_ford(g, 0)
print(dist)
print(path)


g = {
    0: {3: 7, 4: 7},
    1: {2: 6, 3: 1},
    2: {1: 6, 5: 9},
    3: {0: 7, 1: 1},
    4: {0: 7, 7: 9},
    5: {2: 9},
    6: {},
    7: {4: 9}
}

dist, path = bellman_ford(g, 0)
print(dist)
print(path)
