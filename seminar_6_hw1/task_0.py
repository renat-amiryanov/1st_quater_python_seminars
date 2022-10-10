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

    for i in range(len(expr)):
        if expr[i] == '(':
            stack.append(expr[i])
        elif expr[i] == ')':
            stack.pop()
    if stack:
        return False
    return True


# def is_correct_input(expr):


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


def get_op_priority(operation):
    """
    Функция которая возвращает приоритет операции

    """
    if operation == '^': return 4
    if operation == '*' or operation == '/': return 3
    if operation == '+' or operation == '-': return 2
    return 0


def compute(a, b, operation):
    """
    Функкция которая выполняет метематический операции
    """
    if operation == '^': return a ^ b
    if operation == '*': return a * b
    if operation == '/': return a / b
    if operation == '+': return a + b
    if operation == '-': return a - b


def solver(expression):
    # список для хранения номеров из выражения
    values = []

    # списко для хранениея операций
    operators = []
    i = 0

    if not checker(expression): return "некорректная запись скобок"
    if expression[-1] in '+-*/%^': return "недостаточно числовых данных"
    
    if expression[0] == '-':
        val = 0
        i = 1
        while i <= len(expression) and expression[i].isdigit():
            val = (val * 10) + int(expression[i])
            i += 1

        values.append(-1 * val)

    while i < len(expression):

        if expression[i] == ' ':
            i += 1
            continue

        elif expression[i] == '(':
            operators.append(expression[i])

        elif expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = (val * 10) + int(expression[i])
                i += 1
            values.append(val)
            i -= 1
        elif expression[i] == ')':
            while len(operators) != 0 and operators[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                operator = operators.pop()

                values.append(compute(val1, val2, operator))
            operators.pop()

        else:
            while (len(operators) != 0
                   and get_op_priority(operators[-1]) >= get_op_priority(expression[i])):
                val2 = values.pop()
                val1 = values.pop()
                operator = operators.pop()

                values.append(compute(val1, val2, operator))
            operators.append(expression[i])
        i += 1
    while len(operators) != 0:
        val2 = values.pop()
        val1 = values.pop()
        operator = operators.pop()

        values.append(compute(val1, val2, operator))
    return values[-1]


test1 = '2+2'  # 2+2 => 4;
test2 = '1+2*3'  # 1+2*3 => 7;
test3 = '10/2*5'  # 10/2*5 => 25;
test4 = '10 * 5 *'  # 10 * 5 * => недостаточно числовых данных
test5 = '-5 + 5'  # -5 + 5 => 0
test6 = 'два + три'  # два + три => неправильный ввод: нужны числа
test7 = '(2+((5-3)*(16-14)))/3'  # (2+((5-3)*(16-14)))/3 => 2
test8 = '(256 - 194'  # (256 - 194 => некорректная запись скобок
#
res = solver(test1)
print(f'{test1} => {res}')
res = solver(test2)
print(f'{test2} => {res}')
res = solver(test3)
print(f'{test3} => {res}')
res = solver(test5)
print(f'{test5} => {res}')
res = solver(test7)
print(f"{test7} => {res}")
res = solver(test4)
print(f"{test4} => {res}")
res = solver(test8)
print(f"{test8} => {res}")


