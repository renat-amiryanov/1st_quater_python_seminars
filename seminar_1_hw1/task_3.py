"""
Напишите программу которая принимает на вход координаты точки (X и Y), причем X != 0 и Y != 0
и выдает номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)

Пример:
x = 34; y = -30 -> 4
x = 2; y = 4 -> 1
x = -34; y = -30 -> 3

"""

point_x = int(input("Введите координату точки X: "))
point_y = int(input("Введите координату точки Y: "))


def get_quarter(x, y):
    if x > 0 and y > 0:
        print(f'X = {x}; y = {y} -> 1')
    elif x < 0 and y > 0:
        print(f'X = {x}; y = {y} -> 2')
    elif x < 0 and y < 0:
        print(f'X = {x}; y = {y} -> 3')
    elif x > 0 and y < 0:
        print(f'X = {x}; y = {y} -> 4')
    elif x == 0 and y != 0:
        print(f'X = {x}; y = {y} -> Точка находится на оси Y')
    elif x != 0 and y == 0:
        print(f'X = {x}; y = {y} -> Точка находится на оси X')
    else:
        print(f'X = {x}; y = {y} -> Точка находится в начале координат')


get_quarter(point_x, point_y)
