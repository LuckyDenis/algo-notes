Бинарный поиск
--------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Алгоритмы на последовательностях](../../../README.md#Алгоритмы-на-последовательностях)
|

> **Целочисленный двоичный поиск** (**бинарный поиск**) 
(англ. _binary search_) — алгоритм поиска объекта по 
заданному признаку в множестве объектов, упорядоченных 
по тому же самому признаку, работающий за 
логарифмическое время.


Реализация
----------
* #### Правосторонняя

|Время   |
|:------:|
|O(log n)|

```python
def is_checker(a, b):
    return a <= b


def right_side_bin_search(nums, k):
    left = -1
    right = len(nums)
    while right - left > 1:
        mid = (left + right) // 2
        if is_checker(nums[mid], k):
            left = mid
        else:
            right = mid
    return left


items = [1, 2, 2, 2, 2, 3, 5, 8, 9, 11]
n = 2
print(right_side_bin_search(items, n)) # 4
```

* #### Левосторонняя

|Время   |
|:------:|
|O(log n)|

```python
def is_checker(a, b):
    return a < b


def left_side_bin_search(nums, k):
    left = -1
    right = len(nums)
    while right - left > 1:
        mid = (left + right) // 2
        if is_checker(nums[mid], k):
            left = mid
        else:
            right = mid
    return right


items = [1, 2, 2, 2, 2, 3, 5, 8, 9, 11]
n = 2
print(left_side_bin_search(items, n)) # 1
```

* #### Массив, отсортированный по возрастанию, был циклически сдвинут

|Время   |
|:------:|
|O(log n)|

```python
def bin_search(nums, k):
    left = -1
    right = len(nums)
    while right - left > 1:
        mid = (left + right) // 2
        if nums[mid] > nums[-1]:
            left = mid
        else:
            right = mid

    shift = left

    if k > nums[0]:
        left = -1
        right = right + 1
    if k < nums[n]:
        left = right
        right = n

    while right - left > 1:
        mid = (left + right) // 2
        if nums[mid] <= k:
            left = mid
        else:
            right = mid

    return shift + right


items = [8, 9, 11, 1, 2, 2, 2, 2, 3, 5]
n = 2
print(bin_search(items, n)) # 4
```