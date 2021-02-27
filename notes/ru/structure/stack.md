Стек
----
| [Главная](../../../README.md#Список-алгоритмов-[russian])
| [Структуры данных](../../../README.md#Структуры-данных)
|

> **Стек** (англ. _stack_) — абстрактный тип данных, 
представляющий собой список элементов, организованных 
по принципу **LIFO** (англ. _last in — first out_, 
«последним пришёл — первым вышел»). Чаще всего 
принцип работы стека сравнивают со стопкой тарелок: 
чтобы взять вторую сверху, нужно снять тарелку, 
которая лежит на самом верху.


Реализация
----------
* #### На основе списка (динамический контейнер)
|Время (push)|Время (pop) | Время (is_empty) |
|:----------:|:----------:|:----------------:|
|O(n)        |O(n)        |O(n)              |

```python
class Stack:
    def __init__(self):
        self.store = []

    def push(self, item):
        self.store.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError()
        return self.store.pop()
    
    def is_empty(self):
        return self.store == []

    
n = 5
stack = Stack()
print(stack.is_empty())

for num in range(n):
    stack.push(num)
print(stack.is_empty())

for _ in range(n):
    print(stack.pop())
print(stack.is_empty())

```