"""
Напишите программу которая принимает на вход координаты точки (X и Y), причем X != 0 и Y != 0
и выдает номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)

Пример:
x = 34; y = -30 -> 4
x = 2; y = 4 -> 1
x = -34; y = -30 -> 3

"""


x = int(input("Введите координату точки X: "))
y = int(input("Введите координату точки Y: "))


def get_quadrant_by_coordinates(x_coord, y_coord):
    if x_coord > 0 and y_coord > 0:
        print(f'X = {x_coord}; y = {y_coord} -> 1')
    elif x_coord < 0 and y_coord > 0:
        print(f'X = {x_coord}; y = {y_coord} -> 2')
    elif x_coord < 0 and y_coord < 0:
        print(f'X = {x_coord}; y = {y_coord} -> 3')
    elif x_coord > 0 and y_coord < 0:
        print(f'X = {x_coord}; y = {y_coord} -> 4')
    elif x_coord == 0 and y_coord != 0:
        print(f'X = {x_coord}; y = {y_coord} -> Точка находится на оси Y')
    elif x_coord != 0 and y_coord == 0:
        print(f'X = {x_coord}; y = {y_coord} -> Точка находится на оси X')
    else:
        print(f'X = {x_coord}; y = {y_coord} -> Точка находится в начале координат')


get_quadrant_by_coordinates(x, y)
