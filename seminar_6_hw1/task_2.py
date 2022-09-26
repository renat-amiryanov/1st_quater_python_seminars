"""
Задача 2.
Найти сумму чисел списка стоящих на нечетной позиции
"""

numbers = [10, 21, 4, 45, 66, 93, 11]
numbers1 = [1, 2, 3, 5]


def sum_odds(lst):
    """
    Функция которая возвращает сумму чисел находящихся на нечетных позициях списка
    (предполагается что будет передаваться список из чисел)
    :param lst: Список состоящий из чисел
    :return: Возврат суммы элементов находящих на нечетных позициях
    """
    return sum([el for el in lst if lst.index(el) % 2 != 0])


print(f'{numbers} => {sum_odds(numbers)}')
print(f'{numbers1} => {sum_odds(numbers1)}')
