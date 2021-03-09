Поиск мостов
------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Графы](../../../README.md#Графы)
|

> **Мостом** называется такое ребро, 
удаление которого делает граф несвязным или, 
точнее, увеличивает число компонент связности.


Реализация
----------

|Время   |
|:------:|
|O(V + E)|

```python
def search_all_bridge(graph):
    t = [1]
    visited = dict().fromkeys(graph, False)
    into = dict().fromkeys(graph, 0)
    out = dict().fromkeys(graph, 0)
    bridges = []

    def dfs(v, p=None):
        visited[v] = True
        into[v] = t[0]
        out[v] = t[0]
        t[0] += 1

        for u in graph[v]:
            if p and u == p:
                continue
            if visited[u]:
                out[v] = min(out[v], into[u])
            else:
                dfs(u, v)
                out[v] = min(out[v], out[u])
                if out[u] > into[v]:
                    bridges.append((v, u))

    for vu in graph:
        if not visited[vu]:
            dfs(vu)

    return bridges


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

print(search_all_bridge(gph))
# [(5, 6), (8, 9), (4, 5), (3, 10)]
```