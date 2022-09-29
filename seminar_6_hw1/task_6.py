"""
Задача 6ю
Сформировать список из N членов последовательности.
Для N = 5: 1, -3, 9, -27, 81 и т.д.
"""


def create_sequence():
    """
    Функция которая формирует список N членов последовательности

    """
    N = int(input('Введите N: '))
    sequence = list(map(lambda i: (-3) ** i, [i for i in range(N)]))
    sequence = list(map(str, sequence))
    print(f'Для {N = }: ', end='')
    print(', '.join(sequence))


create_sequence()