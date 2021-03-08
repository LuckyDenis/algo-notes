Подсчет инверсий без использования Таблицы Инверсий.
----------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Сортировки](../../../README.md#Сортировки)
|

> **Число инверсии** — это мощность множества инверсии. 
Это общепринятая мера сортировки перестановки или 
последовательности.


Реализация
----------
|Лучшее время|Среднее время|Худшее время    |Память   |Устойчивая|Обмены в среднем|
|:----------:|:-----------:|:--------------:|:-------:|:--------:|:--------------:|
|O(n log n)  |O(n log n)   |O(n log n)      |O(log n) |+         |O(n log n)      |

```python
cnt = 0


def merge_sort(arr):
    global cnt
    if len(arr) <= 1:
        return

    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            cnt += len(left) - i
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


nums = [5, 4, 2, 1]
merge_sort(nums)
print(cnt) # 6
```