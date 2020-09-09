# coding: utf8
"""
Вычисление факториала.
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


assert fact_tree(5) == 120
assert fact_tree(4) == 24

