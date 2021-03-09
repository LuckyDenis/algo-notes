Двоичная куча (min)
---------------------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Структуры данных](../../../README.md#Структуры-данных)
|

> **Двоичная куча**, **пирамида**, **сортирующее дерево** — 
такое двоичное дерево, для которого выполнены три условия: _1)_ 
Значение в любой вершине не меньше, чем значения её потомков. _2)_ 
Глубина всех листьев (расстояние до корня) отличается не более
чем на 1 слой. _3)_ Последний слой заполняется слева направо без «дырок».



Реализация
----------
* #### На основе списка (динамический контейнер), без рекурсии
|Время (build)|Время (append) | Время (pop_min)  | Время (shift_down) | Время (shift_up) | Время (merge) |
|:-----------:|:-------------:|:----------------:|:------------------:|:----------------:|:-------------:|
|O(n)         |O(log n)       |O(log n)          |O(log n)            |O(log n)          |O(n + m)       |

```python

def shift_down(heap, i):
    n = len(heap)

    while 2 * i + 1 < n:
        left = 2 * i + 1
        right = 2 * i + 2
        j = left
        if right < n and heap[right] < heap[left]:
            j = right

        if heap[i] <= heap[j]:
            break

        heap[i], heap[j] = heap[j], heap[i]
        i = j


def shift_up(heap, i):
    while i > 0 and heap[i] < heap[(i - 1) // 2]:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2


def pop_min(heap):
    min_item = heap[0]
    if len(heap) == 1:
        return min_item
    heap[0] = heap.pop()
    shift_down(heap, 0)
    return min_item


def append(heap, value):
    heap.append(value)
    shift_up(heap, len(heap) - 1)


def build(items):
    heap = [item for item in items]
    for i in range(len(heap) // 2, -1, -1):
        shift_down(heap, i)
    return heap


def merge(heap_a, heap_b):
    # аналог heap_a.extend(heap_b)
    for item in heap_b:
        heap_a.append(item)
    build(heap_a)


nums = [100, 10, 5, 30, 50]
binary_heap = build(nums)
print(binary_heap)
print(pop_min(binary_heap))
print(pop_min(binary_heap))
print(pop_min(binary_heap))
print(pop_min(binary_heap))
append(binary_heap, 45)
print(pop_min(binary_heap))
print(pop_min(binary_heap))
# 5, 10, 30, 50, 45, 100
```