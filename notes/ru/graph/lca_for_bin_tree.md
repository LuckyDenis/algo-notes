Наименьший общий предок для бинарного дерева. LCA
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

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


bin_tree_root = Node(1)
bin_tree_root.left = Node(2)
bin_tree_root.left.left = Node(3)
bin_tree_root.left.left.left = Node(5)
bin_tree_root.left.right = Node(4)
bin_tree_root.right = Node(6)
bin_tree_root.right.left = Node(7)
bin_tree_root.right.right = Node(8)
bin_tree_root.right.right.left = Node(9)


def dfs(start):
    stack = [start]
    d = dict()
    p = dict()
    d[start.data] = 0
    p[start.data] = start.data
    n = 0
    max_h = 0
    while stack:
        n += 1
        v = stack.pop()
        if max_h < d[v.data]:
            max_h = d[v.data]

        if v.left:
            stack.append(v.left)
            d[v.left.data] = d[v.data] + 1
            p[v.left.data] = v.data
        if v.right:
            stack.append(v.right)
            d[v.right.data] = d[v.data] + 1
            p[v.right.data] = v.data

    return p, d, n, max_h


def preprocess(root):
    p, d, n, max_h = dfs(root)

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


print(lca(5, 4, *preprocess(bin_tree_root))) # 2
```