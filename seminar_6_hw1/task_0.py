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
import math


def checker(expr):
    stack = []
    expr = expr.replace(' ', '')

    if expr[0] in '/*!@#$%^&*+' or expr[-1] in '/*!@#$%^&*+':
        return 'недостаточно числовых данных'

    for char in expr:
        if char.isdigit() or char in '+-/*':
            continue
        elif char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            current = stack.pop()
            if current == '(':
                if char != ')':
                    return False

    if stack:
        return 'некорректная запись скобок'
    return True


def solve(expr):
    expr = expr.replace(' ', '')
    expr = list(expr[::-1])

    def get_value():
        sign = 1
        if expr and expr[-1] == '-':
            expr.pop()
            sign = -1
        value = 0
        while expr and expr[-1].isdigit():
            value *= 10
            value += int(expr.pop())
        return sign * value

    def get_term():
        term = get_value()
        while expr and expr[-1] in '*/':
            op = expr.pop()
            value = get_value()
            if op == '*':
                term *= value
            else:
                term = term / value
        return term

    ans = get_term()
    while expr:
        op, term = expr.pop(), get_term()
        if op == '+':
            ans += term
        else:
            ans -= term
    return ans


test1 = '2+2'  # 2+2 => 4;
test2 = '1+2*3'  # 1+2*3 => 7;
test3 = '10/2*5'  # 10/2*5 => 25;
test4 = '10 * 5 '  # 10 * 5 * => недостаточно числовых данных
test5 = '-5 + 5'  # -5 + 5 => 0
test6 = 'два + три'  # два + три => неправильный ввод: нужны числа
test7 = '(2+((5-3)*(16-14)))/3'  # (2+((5-3)*(16-14)))/3 => 2
test8 = '(256 - 194'  # (256 - 194 => некорректная запись скобок

# print([ch for ch in test1])
# print([ch for ch in test2])
# print([ch for ch in test3])
# print([ch for ch in test4])


test1 = '2+2*10'  # 2+2 => 4;


def func(expr):
    r = ['']
    for i in expr.replace(" ", ''):
        if i.isdigit() and r[-1].isdigit():
            r[-1] = r[-1] + i
        else:
            r.append(i)
    return r[1:]


####

def parse_number(expr):
    number_temp = ''
    i =0
    while(i <len(expr) and str.isdigit(expr[i])):
        if str.isdigit(expr[0]):
            number_temp += expr[0]

print(parse_number(test1))