Наименьший общий предок для дерева. LCA
-----------------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Графы](../../../README.md#Графы)
|

> **Наименьший общий предок** (**нижайший общий предок**) вершин 
u и v в корневом дереве T — наиболее удалённая от корня дерева 
вершина, лежащая на обоих путях от u и v до корня, то есть 
являющаяся предком обеих вершин. Общепринятое сокращение — 
_LCA_ от англ. _lowest (least) common ancestor_.


Реализация
----------
* #### Используя метод двойного подъема

|Препроцессинг|Запросы |
|:-----------:|:------:|
|O(n log n)   |O(log n)|

```python
def dfs(graph, start):
    stack = [start]
    dist = dict().fromkeys(graph, -1)
    parent = dict().fromkeys(graph, -1)
    dist[start] = 0
    parent[start] = start
    n = 0
    max_h = 0
    while stack:
        n += 1
        v = stack.pop()
        if max_h < dist[v]:
            max_h = dist[v]
        for u in graph[v]:
            stack.append(u)
            dist[u] = dist[v] + 1
            parent[u] = v

    return parent, dist, n, max_h


def preprocess(graph, start):
    p, d, n, max_h = dfs(graph, start)

    dp = dict()
    for i in range(1, n + 1):
        if i not in dp:
            dp[i] = []
        dp[i].append(p[i])

    for j in range(1, max_h):
        for i in range(1, n + 1):
            dp[i].append(dp[p[i]][j - 1])

    return dp, d, p, max_h


def lca(v, u, dp, d, p, max_h):
    if d[v] > d[u]:
        v, u = u, v

    for i in range(max_h - 1, -1, -1):
        if d[dp[u][i]] - d[v] >= 0:
            u = dp[u][i]

    if v == u:
        return v

    for i in range(max_h - 1, -1, -1):
        if dp[v][i] != dp[u][i]:
            v = dp[v][i]
            u = dp[u][i]

    return p[v]


def main():
    g = {
        1: [2, 6],
        2: [3, 4],
        3: [5],
        4: [],
        5: [],
        6: [7, 8, 9],
        7: [],
        8: [10],
        9: [],
        10: []
    }
    dp, d, p, max_h = preprocess(g, 1)

    queries = [(5, 4), (7, 9), (5, 10)]
    for v, u in queries:
        print(lca(v, u, dp, d, p, max_h)) # 2, 6, 1


main()
```