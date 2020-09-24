# coding: utf8
"""
Решето Эратосфена.
"""


def _make_sieve(num):
    """
    Создаем решето
    :param num: число до которого ищем простые числа
    :return: булевой список, где ai - число:
        True - простое, False - составное
    """
    nums = [False if i % 2 == 0 else True for i in range(num + 1)]
    nums[1] = False
    nums[2] = True

    i = 2
    while i * i <= num:
        if nums[i]:
            for j in range(i, num + 1, i):
                if j % i == 0 and j != i:
                    nums[j] = False
        i += 1
    return nums


def _select_simple_nums(nums):
    """
    :param nums: решето Эратосфена
    :return: список простых чисел
    """
    simple_nums = []
    for num, is_simple in enumerate(nums):
        if is_simple:
            simple_nums.append(num)
    return simple_nums


def simple_numbers(num):
    """
    Обертка.
    :param num: число до которого ищем простые числа
    :return: список простых чисел
    """
    sieve = _make_sieve(num)
    simple_nums = _select_simple_nums(sieve)
    return simple_nums
