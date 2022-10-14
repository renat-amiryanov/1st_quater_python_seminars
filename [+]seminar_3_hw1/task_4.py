"""
Задача 4.
Написать программу, которая будет преобразовывать десятичное число в двоичное
Подумать как это можно решить с помощь рекурсии

Пример:
45 -> 101101
3 -> 11
2 -> 10
"""


def int_to_bin(data):
    bin_str = ''
    while not data == 0:
        res = data % 2
        data //= 2
        bin_str += str(res)
    return bin_str[::-1]


n = 45
print(n, '->', int_to_bin(n))

n = 3
print(n, '->', int_to_bin(n))

n = 2
print(n, '->', int_to_bin(n))

