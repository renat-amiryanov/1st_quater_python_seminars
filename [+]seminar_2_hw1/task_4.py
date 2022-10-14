"""
Задача 4.
Реализовать выдачу случайного числа. Не использовать random.randint и вообще библиотеку random
Можно использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) для задания случайности
учесть что есть диапазон от (минимальное) до (максимум)

"""

import time


def random(start, end):
    """
    Custom generator of random integer number
    :param start: Начало диапазона
    :param end: Конец диапазона
    :return: Случайное число в пределах заданного диапазона
    """
    is_in_range = False

    while not is_in_range:
        rand_number = time.time_ns()

        # выполняем сдвиг влево на 21 бит и выполняем побитовое Исключаеющее ИЛИ (XOR) и исходным значениме
        rand_number ^= (rand_number << 21)

        # выполняем сдвиг вправо на 35 бита и выполняем побитовое Исключаеющее ИЛИ (XOR) и исходным значениме
        rand_number ^= (rand_number >> 35)

        # выполняем сдвиг влево на 4 бита и выполняем побитовое Исключаеющее ИЛИ (XOR) и исходным значениме
        rand_number ^= (rand_number << 4)

        rand_number %= end

        if rand_number < start:
            rand_number += start

        if start <= rand_number < end:
            is_in_range = True
    return rand_number


for i in range(1, 10):
    time.sleep(0.015)
    print(f'{random(0, 25)}', end=' ')
