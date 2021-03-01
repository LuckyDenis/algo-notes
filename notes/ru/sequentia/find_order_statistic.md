Поиск k-ой порядковой статистики
--------------------------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Алгоритмы на последовательностях](../../../README.md#Алгоритмы-на-последовательностях)
|

> **k-ой порядковой статистикой** набора элементов линейно упорядоченного 
множества называется такой его элемент, который является k-ым элементом 
набора в порядке сортировки.


Реализация
----------
|Лучшее время|Среднее время|Худшее время    |Память   |
|:----------:|:-----------:|:--------------:|:-------:|
|O(n)        |O(n)         |O(n<sup>2</sup>)|O(1)     |


```python
def partition(arr, left, right):
    mid_item = arr[(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while arr[i] > mid_item:
            i += 1
        while arr[j] < mid_item:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return j


def find_order_statistic(arr, k):
    left = 0
    right = len(arr) - 1
    while True:
        mid = partition(arr, left, right)
        if mid == k - 1:
            return arr[mid]
        elif k < mid:
            right = mid
        else:
            left = mid + 1


nums = [12, -4, 0, 4, 5, 90, -8, 1, 1, 3, -4]
print(find_order_statistic(nums, 2))  # 12
print(nums) # [90, 12, 0, 4, 5, -4, -8, 1, 1, 3, -4] 
```