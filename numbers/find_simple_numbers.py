# coding: utf8
"""
Решето Эратосфена.
"""


def find_simple_nums(num):
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


def get_simple_nums(nums):
    simple_nums = []
    for num, is_simple in enumerate(nums):
        if is_simple:
            simple_nums.append(num)
    return simple_nums


# 2, 3, 5, 7, 11, 13, 17, 19
print(*get_simple_nums(find_simple_nums(21)), sep=", ")
