"""
Задача 2.
Задайте последовательность чисел.
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
!!! Не использовать множества.
[1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]
"""


def get_unique_elements(values):
    """
    Функция которая возвращается список неповторяющихся элементов исходной последовательности
    :param values: Исходная последовательность
    :return: Взврат списка не повторящихся элементов
    """
    ret_values = []
    for i in range(len(values)):
        if ret_values.count(values[i]) == 0:
            ret_values.append(values[i])
    return ret_values


sequence = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
data = get_unique_elements(sequence)
print(sequence, data, sep=' -> ')
