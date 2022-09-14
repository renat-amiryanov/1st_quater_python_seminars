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
    :param start:
    :param end:
    :return: random number between start and end
    """
    rand_number = time.time_ns()

    # выполняем сдвиг влево на 21 бит
    rand_number ^= (rand_number << 27)
    rand_number ^= (rand_number >> 9)
    rand_number ^= (rand_number << 86)

    rand_number %= end

    if rand_number < start:
        rand_number += start
    return rand_number


for i in range(1, 10):
    time.sleep(0.03)
    print(random(70, 100), end=', ')


