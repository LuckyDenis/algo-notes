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
* #### Используя рекурсию

|Запросы |
|:------:|
|O(log n)|

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


bin_tree_root = Node(10)
bin_tree_root.left = Node(8)
bin_tree_root.left.left = Node(7)
bin_tree_root.left.left.left = Node(6)
bin_tree_root.left.right = Node(9)
bin_tree_root.right = Node(12)
bin_tree_root.right.left = Node(11)
bin_tree_root.right.right = Node(14)
bin_tree_root.right.right.left = Node(13)


def lca(node, lt, rt):
    if lt < node.data and rt < node.data:
        return lca(node.left, lt, rt)
    if lt > node.data and rt > node.data:
        return lca(node.right, lt, rt)
    if lt == node.data or rt == node.data:
        return node.data
    return node.data


print(lca(bin_tree_root, 11, 13)) # 12
print(lca(bin_tree_root, 6, 9)) # 8
print(lca(bin_tree_root, 6, 13)) # 10
```