Поиск кротчайшего пути. Алгоритм Дейкстры
-----------------------------------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Графы](../../../README.md#Графы)
|

> **Алгоритм Дейкстры** (англ. _Dijkstra’s algorithm_) — 
алгоритм на графах, изобретённый нидерландским 
учёным Эдсгером Дейкстрой в 1959 году. Находит кратчайшие 
пути от одной из вершин графа до всех остальных. 
Алгоритм работает только для графов без рёбер 
отрицательного веса.


Реализация
----------
* #### Перебор всех вершин

```python
def search_next_vertex(graph, visited, distances):
    v = None
    for j in graph:
        if visited[j]:
            continue
        elif v is None or distances[j] < distances[v]:
            v = j
    return v


def add_distance(v, graph, distances, paths):
    for u, cost in graph[v].items():
        if distances[v] + cost < distances[u]:
            distances[u] = distances[v] + cost
            paths[u] = v


def dijkstra(graph, start):
    distances = dict().fromkeys(graph.keys(), float('inf'))
    visited = dict().fromkeys(graph.keys(), False)
    paths = dict().fromkeys(graph.keys(), -1)

    distances[start] = 0
    for _ in graph:
        v = search_next_vertex(graph, visited, distances)

        if distances[v] == float('inf'):
            break
        visited[v] = True
        add_distance(v, graph, distances, paths)

    return distances, paths


g = {
    0: {2: 1},
    1: {5: 2, 6: 9},
    2: {0: 1},
    3: {},
    4: {},
    5: {1: 2, 6: 9},
    6: {1: 9, 5: 9, 7: 6},
    7: {6: 6}
}

dist, path = dijkstra(g, 5)
print(dist)
print(path)
# dict = {0: inf, 1: 2, 2: inf, 3: inf, 4: inf, 5: 0, 6: 9, 7: 15}
# path = {0: -1, 1: 5, 2: -1, 3: -1, 4: -1, 5: -1, 6: 5, 7: 6}
```