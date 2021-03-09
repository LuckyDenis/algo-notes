Поиск точек сочленения
----------------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Графы](../../../README.md#Графы)
|

> **Точкой сочленения** 
(англ. _cut vertex_ или _articulation point_)
называется такая вершина, удаление которой 
делает граф несвязным.


Реализация
----------

|Время   |
|:------:|
|O(V + E)|

```python
def search_art_points(graph):
    t = [0]
    visited = dict().fromkeys(graph, False)
    into = dict().fromkeys(graph, 0)
    out = dict().fromkeys(graph, 0)
    art_points = set()

    def dfs(v, p=None):
        visited[v] = True
        into[v] = t[0]
        out[v] = t[0]
        t[0] += 1
        children = 0
        for u in graph[v]:
            if p and u == p:
                continue
            if visited[u]:
                out[v] = min(out[v], into[u])
            else:
                dfs(u, v)
                children += 1
                out[v] = min(out[v], out[u])
                if p is not None and out[u] >= into[v]:
                    art_points.add(v)
        if p is None and children > 1:
            art_points.add(v)

    for uv in graph:
        if not visited[uv]:
            dfs(uv)

    return art_points


gph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4, 10],
    4: [2, 3, 5],
    5: [4, 6, 7, 8],
    6: [5],
    7: [5, 8],
    8: [5, 7, 9],
    9: [8],
    10: [11, 12],
    11: [10, 12],
    12: [10, 11]
}

print(search_art_points(gph))
# {3, 4, 5, 8, 10}
```