Разложение на множители (факторизация)
--------------------------------------
***
Разложение на множители, или <span style="color:yellow">Факторизация</span> целых чисел 
(англ. _integer factorization_) — представление числа 
в виде произведения его множителей.


Реализация
----------
***
* #### Наивная реализация

|Время|
|:---:|
|O(n) |
  
```python
def factorization(n):
    muls = []
    i = 2
    while i <= n:
        if n % i == 0:
            muls.append(i)
            n = n // i
        else:
            i = i + 1
    
    if n != 0:
        muls.append(n)

        
print(factorization(45)) # [3, 3, 5] 
```

* #### Улучшенная реализация

|Время|
|:---:|
|O(&radic;n)|
```python
from math import sqrt


def factorization(n):
    muls = []
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            muls.append(i)
            n = n // i
        else:
            i = i + 1
    
    if n != 0:
        muls.append(n)


print(factorization(45)) # [3, 3, 5] 
```