"""
Написать программу, которая по заданному номеру четверити, показывает диапазон возможных координат точек в этой четверти
( x и y )

"""


def get_range_by_quadrant(quadrant):
    try:
        quadrant = int(quadrant)
        if quadrant == 1:
            print(f'{quadrant} четверть содержит положительные значения x и положительные значения y')
        elif quadrant == 2:
            print(f'{quadrant} четверть содержит отрицательные значения x и положительные значения y')
        elif quadrant == 3:
            print(f'{quadrant} четверть содержит отрицательные значения x и отрицительные значения y')
        elif quadrant == 4:
            print(f'{quadrant} четверть содержит положительные значения x и отрицательные значения y')
    except:
        print(f'Не верное значение четверти "{quadrant}". ')


get_range_by_quadrant(1)
get_range_by_quadrant('2')
get_range_by_quadrant(3)
get_range_by_quadrant(4)
get_range_by_quadrant('one')
