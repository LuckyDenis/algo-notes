Поиск подмассива с максимальной суммой. Алгоритм Джея Кадане
----------------------------------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Алгоритмы на последовательностях](../../../README.md#Алгоритмы-на-последовательностях)
|

> В информатике **задача о подмассиве с максимальной суммой** - 
это задача нахождения смежного подмассива с наибольшей суммой 
внутри заданного одномерного массива чисел A[1...n].


Реализация
----------
* #### Алгоритм Джея Кадане

|Время|Память|
|:---:|:----:|
|O(n) |O(1)  |

```python
def find_maximum_sub_array(nums):
    global_sum = nums[0]
    local_sum = 0
    left_idx = 0
    right_idx = 0
    minus_position = -1
    
    for i in range(len(nums)):
        local_sum += nums[i]
        if global_sum < local_sum:
            global_sum = local_sum
            left_idx = minus_position + 1
            right_idx = i
        
        if local_sum < 0:
            local_sum = 0
            minus_position = i
    
    return left_idx, right_idx, global_sum


print(find_maximum_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # (3, 6, 6)
```
