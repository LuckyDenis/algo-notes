Генерация правильных скобочных последовательностей
---------------------------------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Алгебра](../../../README.md#Алгебра)
|

> **Генерация скобочных последовательностей** 
(анлг. _generation all bracket sequences_) — 
класс комбинаторных объектов, представляющих 
собой последовательность скобочных символов.
Пусть нам известно число n. Надо вывести все 
правильные скобочные последовательности в 
лексикографическом порядке с n открывающимися 
скобками.

Реализация
----------
* #### Рекурсивный алгоритм
|Время|
|:---:|
|O((C<sub>n</sub><sup>n/2</sup> - C<sub>n</sub><sup>n/2 - 1</sup>) * n) |

```python
def generation(n, cnt_open=0, cnt_close=0, answer=''):
    if cnt_open + cnt_close == n:
        print(answer)
        return
    if cnt_open < n:
        generation(n, cnt_open + 1, cnt_close, answer + '(')
    if cnt_close < cnt_open:
        generation(n, cnt_open, cnt_close + 1, answer + ')')


generation(3) # ((())), (()()), (())(), ()(()), ()()()
```
