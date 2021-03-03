Дерево отрезков
---------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Структуры данных](../../../README.md#Структуры-данных)
|

> **Дерево отрезков** (англ. _Segment tree_) — 
это структура данных, позволяющая за асимптотику O(log n) 
реализовать любые операции, определяемые на множестве, 
на котором данная операция ассоциативна, и существует 
нейтральный элемент относительно этой операции, то есть 
на моноиде. Например, суммирование на множестве натуральных 
чисел, поиск минимума на любом числовом множестве, 
перемножение матриц на множестве матриц размера N∗N, 
объединение множеств, поиск наибольшего общего 
делителя на множестве целых чисел и многочленов.


Реализация
----------
* #### Без использования рекурсии, сумма отрезков

|Время (build)|Время (set) | Время (query_sum) |
|:-----------:|:----------:|:-----------------:|
|O(n)         |O(log n)    |O(log n)           |

```python
class SegmentTree:
    def __init__(self):
        self.monoid = 0
        self.n = 0
        self.tree = [self.monoid]

    def _make_tree_store(self, n):
        self.tree = [self.monoid for _ in range(2 * n - 1)]

    def build(self, items):
        self.n = len(items)
        self._make_tree_store(self.n)

        n = self.n
        for i in range(n):
            self.tree[n - 1 + i] = items[i]

        for i in range(n - 2, -1, -1):
            self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i + 2]

    def set(self, index, value):
        i = index + self.n - 1
        self.tree[i] = value

        while i > 0:
            i = (i - 1) // 2
            self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i + 2]

    def query_sum(self, i, j):
        result = self.monoid
        i += self.n - 1
        j += self.n - 2

        while i <= j:
            if i % 2 == 0:
                result += self.tree[i]
            if j % 2 == 1:
                result += self.tree[j]

            i = i // 2
            j = j // 2 - 1

        return result


arr = [5, 2, 6, 7, 8, 4, 4, 6, 9]

segment_tree = SegmentTree()
segment_tree.build(arr)
print(segment_tree.tree)  # [42, 20, 22, 7, 13, 12, 10, 5, 2, 6, 7, 8, 4, 4, 6, 9]
segment_tree.set(1, 100)
print(segment_tree.tree)  # [140, 118, 22, 105, 13, 12, 10, 5, 100, 6, 7, 8, 4, 4, 6, 9]
print(segment_tree.query_sum(2, 8))  # 35

```