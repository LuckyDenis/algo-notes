Бинарное дерево поиска
-------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Структуры данных](../../../README.md#Структуры-данных)
|

> **Бинарное дерево поиска** (англ. _binary search tree_, _BST_) — 
структура данных для работы с упорядоченными множествами. Бинарное 
дерево поиска обладает следующим свойством: 
если x — узел бинарного дерева с ключом k, 
то все узлы в левом поддереве должны иметь ключи, меньшие k, 
а в правом поддереве большие k.



Реализация
----------
* #### Без рекурсии
|Время (insert)|Время (search)|Время (delete) |Время (search_parent)|Время (search_min)|Время (search_max)|
|:------------:|:------------:|:-------------:|:-------------------:|:----------------:|:----------------:|
|O(log n)      |O(log n)      |O(log n)       |O(log n)             |O(log n)          |O(log n)          |
```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def insert(node, value):
    if not node:
        return Node(value)

    current = node
    while current:
        if current.value < value:
            if not current.right:
                current.right = Node(value)
                return node
            current = current.right
        else:
            if not current.left:
                current.left = Node(value)
                return node
            current = current.left


def search(node, value, fail_value=-1):
    current = node
    while current:
        if current.value == value:
            return current
        if current.value < value:
            current = current.right
        else:
            current = current.left
    return Node(fail_value)


def search_min(node):
    current = node
    while current.left:
        current = current.left
    return current


def search_max(node):
    current = node
    while current.right:
        current = current.right
    return current


def search_parent(node, value, fail_value=-1):
    current = node
    fail_node = Node(fail_value)
    successes = fail_node
    while current:
        if current.value == value:
            return successes

        successes = current
        if current.value < value:
            current = current.right
        else:
            current = current.left

    return fail_node


def delete_node_has_not_children(p, d):
    if d.left or d.right:
        return False

    if p.left is d:
        p.left = None

    if p.right is d:
        p.right = None
    return True


def delete_node_has_one_child(p, d):
    if d.left and d.right:
        return False
    if not d.left and not d.right:
        return False

    if not d.left:
        if p.left is d:
            p.left = d.right
        else:
            p.right = d.right
    else:
        if p.left is d:
            p.left = d.left
        else:
            p.right = d.left
    return True


def delete_node_has_two_children(d):
    if not d.left and not d.right:
        return False
    if d.left and not d.right:
        return False
    if d.right and not d.left:
        return False

    current = d.right
    current_p = d
    while current.left:
        current_p = current
        current = current.left

    d.value = current.value
    if delete_node_has_not_children(current_p, current):
        return True
    if delete_node_has_one_child(current_p, current):
        return True
    return False


def delete(node, d):
    p = search_parent(node, d.value)

    if delete_node_has_not_children(p, d):
        return True
    if delete_node_has_one_child(p, d):
        return True
    if delete_node_has_two_children(d):
        return True
    return False


root = insert(None, 8)
insert(root, 3)
insert(root, 1)
insert(root, 6)
insert(root, 4)
insert(root, 7)
insert(root, 10)
insert(root, 14)
insert(root, 13)


parent = search_parent(root, 7) # 6
print(parent.value)
parent = search_parent(root, 8) # -1
print(parent.value)
parent = search_parent(root, 23) # -1
print(parent.value)

min_node = search_min(root)
print(min_node.value) # 1
max_node = search_max(root)
print(max_node.value) # 14

find_node = search(root, 7)
print(find_node.value) # 7

not_find_node = search(root, 23) 
print(not_find_node.value) # -1
delete(root, search(root, 8))
```