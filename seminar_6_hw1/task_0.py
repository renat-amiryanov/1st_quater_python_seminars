"""
Задание с семинара
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,. приоритет операций стандартный.
Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
*Пример:
2+2 => 4;
1+2*3 => 7;
10/2*5 => 25;
10 * 5 * => недостаточно числовых данных
-5 + 5 => 0
два + три => неправильный ввод: нужны числа
(2+((5-3)*(16-14)))/3 => 2
(256 - 194 => некорректная запись скобок
"""
expr1 = "2+2"
expr2 = "1+2*3"
expr2 = "10/2*5"

expr4 = "(2+((5-3)*(16-14)))/3"

# print(eval(expr4))
#
# size = len(expr4)
# empty_element = 0
# storage = []
# top = 0
# print(storage)
# char = '2'
# print('[({'.find(char))
#
# storage.insert(0, 2)
# print(storage)
#
# storage.insert(0, 2)
# print(storage)

expr4 = "(2+((5-3)*(16-14)))/3"
expr1 = "((2+2)/2)"
expr10 = ''


def check(expr: str):
    storage = []
    for i in range(len(expr)):
        cur_char = expr[i]
        if '('.find(cur_char) != -1:
            storage.append(cur_char)
        elif cur_char == ')':
            storage.pop()

    if len(storage) == 0:
        return -1



