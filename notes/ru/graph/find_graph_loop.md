Проверка наличия цикла в графе
------------------------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Графы](../../../README.md#Графы)
|

> Дан граф, требуется проверить наличие цикла в этом графе.


Реализация
----------

* #### Ориентированный граф, покраска в три цвета

|Время   |
|:------:|
|O(V + E)|

|Цвет |Код цвета|
|:---:|:-------:|
|White|0        |
|Grey |1        |
|Black|2        |


```python
def dfs(graph, v, visited):
    visited[v] = 1
    for u in graph[v]:
        if visited[u] == 0:
            dfs(graph, u, visited)
        if visited[u] == 1:
            print('Edge:', v, '-', u, 'created loop')
        visited[v] = 2


g = {
    0: [1],
    1: [2],
    2: [3],
    3: [6],
    4: [2],
    5: [1],
    6: [2, 4, 5]
}


def find_graph_loop(graph):
    visited = dict().fromkeys(graph, 0)
    for v in graph:
        if visited[v] == 0:
            dfs(g, v, visited)


find_graph_loop(g)
"""
Edge: 6 - 2 created loop
Edge: 4 - 2 created loop
Edge: 5 - 1 created loop
"""
```


