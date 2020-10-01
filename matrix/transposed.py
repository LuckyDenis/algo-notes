# coding: utf8
"""
По своей сути алгоритм повторят то что делает функция `zip`.
С использование функции `zip` алгоритм можно написать в 1 строчку:
    :code:
        [*zip(*matrix)]

Но эта реализация вернет список кортежей,
а кортеж не изменяемый тип данных.
"""


def transposed_mtx(mtx):
    rows = len(mtx)
    cols = len(mtx[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for r in range(rows):
        for c in range(cols):
            result[c][r] = mtx[r][c]
    return result
