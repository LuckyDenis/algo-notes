Топологическая сортировка
-------------------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Графы](../../../README.md#Графы)
|

> Под **топологической сортировкой** (англ. _topological sort_) 
ориентированного ациклического графа понимается сортировка 
элементов, для которых определен частичный порядок, то есть 
упорядочивание задано не для всех, а только для 
некоторых пар элементов. Задача топологической 
сортировки графа состоит в следующем: указать такой 
линейный порядок на его вершинах, чтобы любое ребро 
вело от вершины с меньшим номером к вершине с большим 
номером. Очевидно, что если в графе есть циклы, 
то такого порядка не существует.


Реализация:
----------
* #### С подсчетом входящих рёбер, без рекурсии

|Время   |
|:------:|
|O(V + E)|

```python
def top_sort(graph):
    v_sort = []
    into = dict()
    for v in graph:
        if v not in into:
            into[v] = 0
        for u in graph[v]:
            if u not in into:
                into[u] = 0
            into[u] += 1

    queue = []
    for to in into:
        if into[to] == 0:
            queue.append(to)

    while queue:
        v = queue.pop(0)
        v_sort.append(v)
        for u in graph[v]:
            into[u] -= 1
            if into[u] == 0:
                queue.append(u)

    return v_sort


g = {
    1: [4, 5],
    2: [1, 5],
    3: [],
    4: [3],
    5: [4, 6],
    6: [3]
}


print(top_sort(g)) # [2, 1, 5, 4, 6, 3]
```

* #### С использованием обхода в глубину, рекурсия

|Время   |
|:------:|
|O(V + E)|

```python
def top_sort(graph):
    order = []
    enter = set(graph)
    visited = dict.fromkeys(graph, 0)

    def dfs(v):
        visited[v] = 1
        for u in graph[v]:
            if visited[u] == 0:
                enter.discard(u)
                dfs(u)
        order.insert(0, v)
        visited[v] = 2

    while enter:
        dfs(enter.pop())
    return order


g = {
    1: [4, 5],
    2: [1, 5],
    3: [],
    4: [3],
    5: [4, 6],
    6: [3]
}
print(top_sort(g)) # [2, 1, 5, 6, 4, 3]
```
