# coding: utf8


def find_palindrome(string):
    pal = [
        [0 for _ in range(len(string))] for _ in range(2)
    ]

    for z in range(2):
        left = 0
        right = 0
        for i in range(len(string)):
            if i < right:
                pal[z][i] = min(
                    right - i + (1 - z),
                    pal[z][left + right - i + (1 - z)]
                )
            left = i - pal[z][i]
            right = i + pal[z][i] - (1 - z)
            while True:
                if left - 1 < 0:
                    break
                if right + 1 > len(string) - 1:
                    break
                if string[left - 1] != string[right + 1]:
                    break
                pal[z][i] += 1
                left -= 1
                right += 1
    return pal
