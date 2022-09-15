"""
Задача 2.
Напишите программу которая найдет произведение парт чисел списка.
Паро считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:
[2,3,4,5,6] => [12,15,16]
[2,3,5,6] => [12,15]

"""
numbers_list = [2, 3,4, 5, 6]

left = 0
right = len(numbers_list)-1

for i in range(left,right):
    print(left, right, numbers_list[left] * numbers_list[right])
    left +=1
    right -=1