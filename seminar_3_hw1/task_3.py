"""
Задача 3.
Задайте список вещественных числе.
Напишите программу которая найдет разницу межде максимальным и минимальным значением дробной части элементов.
Пример:
[1.1, 1.2, 3.1, 5.17, 10.02] -> 0.18
[4.07, 5.1, 8.2444, 6.98] -> 0.91

"""

def get_fraction(values):
    """
    Функция которая получает дробную часть вещественного числа
    :param values:  Список вещественныщ числе
    :return:  Возврат списка дробных частей вещественных числе
    """
    return [round(v - int(v), 5) for v in values]


def display(float_numbers):

    fractions = get_fraction(float_numbers)
    difference = round((max(fractions)) - min(fractions), 10)
    print(float_numbers, difference, sep=' => ')


example1 = [1.1, 1.2, 3.1, 5.17, 10.02]
example2 = [4.07, 5.1, 8.2444, 6.98]

display(example1)
display(example2)


