# coding: utf8
"""
Факторилизация числа (разложение на простые множители)
"""


def factorize(n):
    simple_multipliers = []
    i = 2
    num = n
    while i * i <= num:
        if num % i == 0:
            simple_multipliers.append(i)
            num //= i
        else:
            i += 1
    simple_multipliers.append(num)
    if len(simple_multipliers) == 1:
        simple_multipliers.insert(0, 1)
    return simple_multipliers
