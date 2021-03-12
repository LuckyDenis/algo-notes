Декартовое дерево
-----------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Структуры данных](../../../README.md#Структуры-данных)
|

> **Декартово дерево** или **дерамида** (англ. _Treap_)
— это структура данных, объединяющая в себе 
бинарное дерево поиска и бинарную кучу 
отсюда и второе её название: treap (tree + heap) 
и дерамида (дерево + пирамида), 
также существует название курево (куча + дерево).
Более строго, это бинарное дерево, в узлах 
которого хранятся пары (x, y), 
где x — это ключ, а y — это приоритет. 
Также оно является двоичным деревом поиска 
по x и пирамидой по y.


Реализация
----------

|Время (merge)|Время (split)|Время (build)|Время (insert)|Время (remove) |
|:-----------:|:-----------:|:-----------:|:------------:|:-------------:|
|O(log n)     |O(log n)     |O(n log n)   |O(log n)      |O(log n)       |

```python
class Node:
    def __init__(self, value, y=None):
        self.y = y
        self.size = 1
        self.x = value
        self.left = None
        self.right = None


def get_size(node):
    if not node:
        return 0
    return node.size


def update_size(node):
    if not node:
        return 0
    node.size = 1 + get_size(node.left) + get_size(node.right)


def merge(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1

    if t1.y > t2.y:
        t1.right = merge(t1.right, t2)
        update_size(t1)
        return t1
    else:
        t2.left = merge(t1, t2.left)
        update_size(t2)
        return t2


def split(t, x):
    if t is None:
        return None, None
    if t.x < x:
        t1, t2 = split(t.right, x)
        t.right = t1
        update_size(t)
        return t, t2

    else:
        t1, t2 = split(t.left, x)
        t.left = t2
        update_size(t)
        return t1, t


def insert(t, x, y=None):
    node = Node(x, y)
    if not t:
        return node
    t1, t2 = split(t, x)
    t = merge(t1, node)
    t = merge(t, t2)
    update_size(t)
    return t


def build(array):
    tree = None
    for xi, yi in array:
        tree = insert(tree, xi, yi)
    return tree


def remove(t, x):
    t1, t2 = split(t, x)
    t3, t4 = split(t2, x + 1)
    t = merge(t1, t4)
    update_size(t)
    return t


def print_tree(tree):
    order = []

    def _print_tree(node):
        if not node:
            return
        _print_tree(node.left)
        order.append((node.x, node.y))
        _print_tree(node.right)

    _print_tree(tree)
    return order


tuples = [(7, 10), (4, 6), (13, 8), (2, 4), (0, 3), (3, 3), (6, 2), (5, 1), (9, 7), (11, 3), (14, 4)]
t_tree = build(tuples)

print(print_tree(t_tree))
# [(0, 3), (2, 4), (3, 3), (4, 6), (5, 1), (6, 2), (7, 10), (9, 7), (11, 3), (13, 8), (14, 4)]
```