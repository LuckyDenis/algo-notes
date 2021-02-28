Система непересекающихся множеств
---------------------------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Структуры данных](../../../README.md#Структуры-данных)
|

> **Система непересекающихся множеств** 
(англ. _disjoint-set_, или _union–find data structure_) 
— структура данных, которая позволяет администрировать 
множество элементов, разбитое на непересекающиеся подмножества. 
При этом каждому подмножеству назначается его представитель — 
элемент этого подмножества. Абстрактная структура данных 
определяется множеством трёх операций: union, find, make_set.
Применяется для хранения компонент связности в графах, 
в частности, алгоритму Краскала необходима подобная 
структура данных для эффективной реализации.


> Роберт Тарьян доказал в 1975 г. замечательный факт: время работы как Find, 
так и Unite на лесе размера N есть O(α(N)). Под α(N) в математике обозначается 
обратная функция Аккермана. 
Эта функция известна тем, что у нее очень быстрый рост. 
Поэтому обратная функция Аккермана не превысит 5. Следовательно, её можно 
принять за константу и считать O(α(N)) ≅ O(1).


Реализация
----------
* #### Реализация с использованием рангов

|Время (make_set) |Время (find) |Время (union)|Память   |
|:---------------:|:-----------:|:-----------:|:-------:|
|O(1)             |O(1)         |O(1)         |O(2 * n) |

```python
class UnionFind:
    def __init__(self):
        self.rank = dict()
        self.parent = dict()

    def make_set(self, x):
        self.rank[x] = 0
        self.parent[x] = x
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y):
        if self.find(x) == self.find(y):
            return
        
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


union_find = UnionFind()
for i in range(1, 5 + 1):
    union_find.make_set(i)

print(union_find.find(4)) # 4

union_find.union(1, 4)
union_find.union(3, 5)

print(union_find.find(4)) # 4
print(union_find.find(1)) # 4
print(union_find.find(2)) # 2

union_find.union(5, 2)
print(union_find.find(5)) # 2
print(union_find.find(3)) # 2
```