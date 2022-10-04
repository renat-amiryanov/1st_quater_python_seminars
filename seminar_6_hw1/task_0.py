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
    for char in expr:
        if char.isdigit() or char in ['+', '-', '/', '*']:
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
        return False
    return True

def solve(expr):


    if not checker(expr):
        return 'некорректная запись скобок'
    


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


ex1 = "2+2"  # => 4;
ex2 = "2+3*4/3-2"  # => 7;
ex3 = "10/2*5"  # => 25;
# ex2 = 10 * 5 * #=> недостаточно числовых данных


print(solve("(2+((5-3)*(16-14))/3"), eval("(2+((5-3)*(16-14)))/3"))