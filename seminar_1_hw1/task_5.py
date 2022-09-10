# Напишите программу которая принимает на вход координаты двух точек
# и находит расстояние между ними 2D пространстве.
# Пример
# A (3, 6); B(2, 1) -> 5.09
# A (7, -5); B(1, -1) -> 7.21

import math


def calculate_distance(a, b):
    # return math.dist(a, b)
    return math.sqrt(sum((a - b) ** 2.0 for a, b in zip(a, b)))


first_point = [float(input("Введите координату x первой точки")), float(input("Введите координату y первой точки"))]
second_point = [float(input("Введите координату x второй точки")), float(input("Введите координату y второй точки"))]
print(f'A {first_point}, B {second_point} -> {calculate_distance(first_point, second_point)}')

for x in zip([first_point, second_point]):
    print(type(x))
