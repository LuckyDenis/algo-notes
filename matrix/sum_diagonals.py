# coding: utf8
"""
Подсчет суммы главной и побочной диагоналей для квадратной матрицы.
Сложность O(N)
"""


def sum_diagonals(mtx):
    n = len(mtx)
    s = 0
    for i in range(n):
        s += mtx[i][i]
        s += mtx[i][(i + 1) * -1]

    if n % 2 == 1:
        idx = n // 2
        s -= mtx[idx][idx]
    return s
