"""
Задача 1.
Задайте список из нескольких чисел.
Напишите программу которая найдет сумму элементов списка,стояших на нечетной позиции
Пример:
[2, 3, 5, 9, 1] -> на нечетных позициях элементы 3 и 9, ответ: 12

"""

numbers = [2, 3, 5, 9, 1]


def get_element_on_odd_indexes(value: list):
    """
    Функция возвращает список элементов стоящих на нечетной позиции
    :param value:
    :return: Возвращает списко элементов
    """
    elements = []
    for i in value:
        if not value.index(i) % 2 == 0:
            elements.append(i)
    return elements


elements = get_element_on_odd_indexes(numbers)
sum_of_elements = sum(elements)
print(f'{numbers} -> на нечетных позициях элементы {elements}, ответ: {sum_of_elements}')
