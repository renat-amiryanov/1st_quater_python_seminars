"""
Задача 5.
Задайте число.
Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""


def fib(value):
    """
    Функция генератор которая возвращает значение как только встречается ключеове слово yield
    из цикла
    :param value:
    :return:
    """
    f1, f2 = 1, 1
    yield 0
    for i in range(value):
        yield f1
        f1, f2 = f2, f1 + f2


def nega_fib(value):
    """
    :param value:
    :return:
    """
    f1, f2 = 1, -1
    for i in range(value):
        yield f1
        f1, f2 = f2, f1 - f2


k = 8
fib = list(fib(k))
n_fib = list(nega_fib(k))[::-1]
print(f'{k=}: {n_fib + fib}')
