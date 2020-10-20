# coding: utf8


def z_function(text, patter, sep="$"):
    s = f"{patter}{sep}{text}"
    z_arr = [0]

    for i in range(1, len(s)):
        slc = s[i:]
        j = 0
        while j < len(s) - i:
            if slc[j] != s[j]:
                break
            j += 1
        z_arr.append(j)
