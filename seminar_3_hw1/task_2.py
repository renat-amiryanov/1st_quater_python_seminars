"""
Задача 2.
Напишите программу которая найдет произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:
[2,3,4,5,6] => [12,15,16]
[2,3,5,6] => [12,15]

"""
numbers = [2, 3, 4, 5, 6]
nums = [2, 3, 5, 6]


def multiply_pairs(values: list) -> list:
    """
     Функция которая находит произведение пар чисел списка
    :param values:
    :return: Возврашается список произведений пар
    """
    left = 0
    right = len(values) - 1
    ret_values = []
    while left <= right:
        ret_values.append(values[left] * values[right])
        left += 1
        right -= 1
    return ret_values


def display(vals):
    res = multiply_pairs(vals)
    print(f'{vals} => {res}')


display(numbers)
display(nums)
display([1, 2, 4, 8, 16, 32, 16, 8, 4, 2, 1])
