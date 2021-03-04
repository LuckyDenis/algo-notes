Префиксная сумма
----------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Структуры данных](../../../README.md#Структуры-данных)
|

> В информатике **префиксная сумма**, **кумулятивная сумма**, 
инклюзивное сканирование или просто сканирование 
последовательности чисел x<sub>0</sub>, x<sub>1</sub>, x<sub>2</sub>, 
… называется последовательность чисел y<sub>0</sub>, y<sub>1</sub>, 
y<sub>2</sub>, …, являющаяся префиксной суммой от входной 
последовательности.

|y<sub>0</sub> = x<sub>0</sub> | y<sub>1</sub> = x<sub>0</sub> + x<sub>1</sub> | y<sub>2</sub> = x<sub>0</sub> + x<sub>1</sub>+ x<sub>2</sub> |
|:----------------------------:|:---------------------------------------------:|:------------------------------------------------------------:|

Например:

|Входные числа|Префиксная сумма|
|:-----------:|:--------------:|
|1            |1               |
|2            |3               |
|3            |6               |
|4            |10              |
|5            |15              |
|6            |21              |
|...          |...             |


Реализация
----------
* #### Реализация на массиве

|Время (build)| Время (query_sum) |
|:-----------:|:-----------------:|
|O(n)         |O(1)               |


```python
class PrefixSumArray:
    def __init__(self):
        self.prefix_sum = [0]
    
    def build(self, nums):
        for i in range(len(nums)):
            self.prefix_sum.append(nums[i] + self.prefix_sum[-1])
            
    def query_sum(self, left, right):
        return self.prefix_sum[right] - self.prefix_sum[left]


arr = [5, 2, 6, 7, 8, 4, 4, 6, 9]
prefix_sum_array = PrefixSumArray()
prefix_sum_array.build(arr)

for lt, rt in (4, 6), (0, 7):
    print(prefix_sum_array.query_sum(lt, rt))  # 12, 36
```