# coding: utf8
"""
Вычисление факториала.

Алгоритм основан на том соображении,
что длинные числа примерно одинаковой
длины умножать эффективнее, чем длинное
число умножать на короткое (как в наивной реализации).
То есть нам нужно добиться, чтобы при вычислении
факториала множители постоянно были примерно одинаковой длины.
"""


def sub_tree(left, right):
    if left > right:
        return 1
    if left == right:
        return left
    if right - left == 1:
        return left * right

    middle = (left + right) // 2
    return sub_tree(left, middle) * sub_tree(middle + 1, right)


def fact_tree(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1 or n == 2:
        return n
    return sub_tree(2, n)
