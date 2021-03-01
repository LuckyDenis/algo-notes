Быстрая сортировка
------------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Сортировки](../../../README.md#Сортировки)
|

> **Быстрая сортировка** (англ. _quick sort_, _сортировка Хоара_) — 
один из самых известных и широко используемых алгоритмов сортировки. 
Среднее время работы O(n log n), что является асимптотически 
оптимальным временем работы для алгоритма, основанного на сравнении. 
Хотя время работы алгоритма для массива из n элементов в худшем 
случае может составить O(n<sup>2</sup>), на практике этот алгоритм 
является одним из самых быстрых сортировок.

Реализация
----------
* #### С использованием рекурсии

|Лучшее время|Среднее время|Худшее время    |Память   |Устойчивая|Обмены в среднем|
|:----------:|:-----------:|:--------------:|:-------:|:--------:|:--------------:|
|O(n log n)  |O(n log n)   |O(n<sup>2</sup>)|O(log n) |-         |O(n log n)      |

```python
def partition(arr, left, right):
    mid_item = arr[(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while arr[i] < mid_item:
            i += 1
        while arr[j] > mid_item:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return j


def quick_sort(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid)
        quick_sort(arr, mid + 1, right)


nums = [12, -4, 0, 4, 5, 90, -8, 1, 1, 3, -4]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
```

* #### Без использования рекурсии
|Лучшее время|Среднее время|Худшее время    |Память   |Устойчивая|Обмены в среднем|
|:----------:|:-----------:|:--------------:|:-------:|:--------:|:--------------:|
|O(n log n)  |O(n log n)   |O(n<sup>2</sup>)|O(log n) |-         |O(n log n)      |

```python
def partition(arr, left, right):
    mid_item = arr[(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while arr[i] < mid_item:
            i += 1
        while arr[j] > mid_item:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return j


def quick_sort(arr, left, right):
    stack = [(left, right)]
    while stack:
        lt, rt = stack.pop()
        if rt <= lt:
            continue
        mid = partition(arr, lt, rt)
        if mid - lt < rt - mid:
            stack.append((lt, mid))
            stack.append((mid + 1, rt))
        else:
            stack.append((mid + 1, rt))
            stack.append((lt, mid))


nums = [12, -4, 0, 4, 5, 90, -8, 1, 1, 3, -4]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
```