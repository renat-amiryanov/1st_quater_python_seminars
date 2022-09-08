"""
Напишите программу которая принимает на вход координаты точки (X и Y), причем X != 0 и Y != 0
и выдает номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)

Пример:
x = 34; y = -30 -> 4
x = 2; y = 4 -> 1
x = -34; y = -30 -> 3

"""


# while point_X == 0 and point_Y == 0:
point_X = int(input("Введите координату точки X: "))
point_Y = int(input("Введите координату точки Y: "))


def set_coordinates():
    points = []
    points.append(int(input("Введите координату точки X: ")))
    points.append(int(input("Введите координату точки Y: ")))
    return  points

print(set_coordinates())


coordinates = [point_X, point_Y]


def get_quarter(coords):
    return coords[0], coords[1]

data = get_quarter(coordinates)

print(coordinates)
print(type(data))
exit()
if point_X > 0 and point_Y > 0:
    print(f'X = {point_X}; y = {point_Y} -> 1')
elif point_X < 0 and point_Y > 0:
    print(f'X = {point_X}; y = {point_Y} -> 2')
elif point_X < 0 and point_Y < 0:
    print(f'X = {point_X}; y = {point_Y} -> 3')
elif point_X < 0 and point_Y < 0:
    print(f'X = {point_X}; y = {point_Y} -> 4')


