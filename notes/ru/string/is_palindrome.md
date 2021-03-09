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
def is_valid(ch):
    return ch.isalpha()


def is_palindrome(string):
    n = len(string)
    left = 0
    right = n - 1
    while left < right:
        while left < n and not is_valid(string[left]):
            left += 1
        while right > 0 and not is_valid(string[right]):
            right -= 1

        if string[left].lower() != string[right].lower():
            return False

        left += 1
        right -= 1

    return True


print(is_palindrome('tenet, Tenet'))  # True
print(is_palindrome('hello'))  # False

```