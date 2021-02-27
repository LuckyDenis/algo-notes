Разложение на множители (факторизация)
--------------------------------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Алгебра](../../../README.md#Алгебра)
|

> Разложение на множители, или **Факторизация** целых чисел 
(англ. _integer factorization_) — представление числа 
в виде произведения его множителей.


Реализация
----------
* #### Наивная реализация

|Время|
|:---:|
|O(n) |
  
```python
def factorization(n):
    multipliers = []
    i = 2
    while i <= n:
        if n % i == 0:
            multipliers.append(i)
            n = n // i
        else:
            i = i + 1
    
    if n != 0:
        multipliers.append(n)
    
    return multipliers

        
print(factorization(45)) # [3, 3, 5] 
```

* #### Улучшенная реализация

|Время|
|:---:|
|O(&radic;n)|
```python
from math import sqrt


def factorization(n):
    multipliers = []
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            multipliers.append(i)
            n = n // i
        else:
            i = i + 1
    
    if n != 0:
        multipliers.append(n)
    
    return multipliers


print(factorization(45)) # [3, 3, 5] 
```