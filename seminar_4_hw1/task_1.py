"""
Задача 1.
Задайте натуральное число N.
Напишите программу, которая составит список простых множителей числа N.
N = 20 -> [2,5]
N = 30 -> [2, 3, 5]
"""

def is_prime(n):
    """
    Функция которая определяет число простое или не простое
    :param n: Проверяемое число на то, что является простым или нет
    :return: True если число простое, False - если не простое
    """
    d = 2
    while n % d != 0:
        d += 1
    return d == n

n = 30

def get_prime_multiplier(value):
    """

    :param value:
    :return:
    """
    for i in range(2, value):
        if not value % i and is_prime(i):
            yield i

n = 20
data = list(get_prime_multiplier(n))
print(f'N = {n} -> {data}')

n = 30
data = list(get_prime_multiplier(n))
print(f'N = {n} -> {data}')

n = 17092022
data = list(get_prime_multiplier(n))
print(f'N = {n} -> {data}')
