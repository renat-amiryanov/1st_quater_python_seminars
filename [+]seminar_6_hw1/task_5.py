"""
Задача 5.
Найти произведение пар чисел в списке.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
"""

def multiply_pairs():
    n = int(input('Введите размер списка: '))
    lst_numbers = list(map(int, input(f'Введите последовальность из {n} цифр через пробел: ').split()))[:n]
    print(f'Список чисел: {lst_numbers}')

    def gen(lst):
        left, right = 0, len(lst) - 1
        while left <= right:
            yield lst[left] * lst[right]
            left += 1
            right -= 1

    multi_lst = [multi for multi in gen(lst_numbers)]
    print(f'Список произведений пар чисел: {multi_lst}')


multiply_pairs()
