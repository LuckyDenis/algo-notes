Проверка слова на палиндром
---------------------------
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Строки](../../../README.md#Строки)
|

> **Палиндром** — число, буквосочетание, слово 
или текст, одинаково читающееся в обоих 
направлениях. Например, число 101; 
слова «топот» в русском языке и фин. 
saippuakivikauppias (продавец мыла; торговец 
щёлоком) — самое длинное слово-палиндром в мире. 
Иногда палиндромом называют любой симметричный 
относительно своей середины набор символов.


Реализация
----------
* #### С двумя индексами

|Время   |Память  |
|:------:|:------:|
|O(n / 2)|O(1)    |


```python
def is_palindrome(string):
    left_idx = 0
    right_idx = len(string) - 1
    while left_idx < right_idx:
        if string[left_idx].lower() != string[right_idx].lower():
            return False
        left_idx += 1
        right_idx -= 1
    return True


print(is_palindrome('tenet')) # True
print(is_palindrome('hello')) # False
```