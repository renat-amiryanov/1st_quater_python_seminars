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
def checker(expr):
    """
    Функция проверки корректности пар скобок () в выражении
    :param expr:
    :return:
    """
    stack = []

    for i in range(len(expr)):
        if expr[i] == '(':
            stack.append(expr[i])
        elif expr[i] == ')':
            if len(stack) != 0 and stack[-1] != '(':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


def is_correct_input(expr):
     for i in range(len(expr)):
         if expr[i].isalpha():
             return False
         return True
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
    Функция которая выполняет метематический операции
    """
    if operation == '^': return a ^ b
    if operation == '*': return a * b
    if operation == '/': return a / b
    if operation == '+': return a + b
    if operation == '-': return a - b


def solver(expression):
    # стэк для хранения чисел из выражения
    stc_numbers = []

    # стэк для хранения операторов и скобок (,+,-,*,/,^,)
    stc_symbols = []
    i = 0

    if not checker(expression): return "некорректная запись скобок"

    if expression[-1] in '+-*/%^': return "недостаточно числовых данных"
    if not is_correct_input(expression): return "неправильный ввод: нужны числа"
    
    if expression[0] == '-':
        val = 0
        i = 1
        while i <= len(expression) and expression[i].isdigit():
            val = (val * 10) + int(expression[i])
            i += 1
        stc_numbers.append(-1 * val)

    while i < len(expression):

        if expression[i] == ' ':
            i += 1
            continue

        elif expression[i] == '(':
            stc_symbols.append(expression[i])

        elif expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = (val * 10) + int(expression[i])
                i += 1
            stc_numbers.append(val)
            i -= 1
        elif expression[i] == ')':
            while len(stc_symbols) != 0 and stc_symbols[-1] != '(':
                val2 = stc_numbers.pop()
                val1 = stc_numbers.pop()
                operator = stc_symbols.pop()

                stc_numbers.append(compute(val1, val2, operator))
            stc_symbols.pop()

        else:
            while (len(stc_symbols) != 0
                   and get_op_priority(stc_symbols[-1]) >= get_op_priority(expression[i])):
                val2 = stc_numbers.pop()
                val1 = stc_numbers.pop()
                operator = stc_symbols.pop()

                stc_numbers.append(compute(val1, val2, operator))
            stc_symbols.append(expression[i])
        i += 1
    while len(stc_symbols) != 0:
        val2 = stc_numbers.pop()
        val1 = stc_numbers.pop()
        operator = stc_symbols.pop()

        stc_numbers.append(compute(val1, val2, operator))
    return stc_numbers[-1]


test1 = '2+2'  # 2+2 => 4;
test2 = '1+2*3'  # 1+2*3 => 7;
test3 = '10/2*5'  # 10/2*5 => 25;
test4 = '10 * 5 *'  # 10 * 5 * => недостаточно числовых данных
test5 = '-5 + 5'  # -5 + 5 => 0
test6 = 'два + три'  # два + три => неправильный ввод: нужны числа
test7 = '(2+((5-3)*(16-14)))/3'  # (2+((5-3)*(16-14)))/3 => 2
test8 = '(256 - 194'  # (256 - 194 => некорректная запись скобок

res = solver(test1)
print(f'{test1} => {res}')

res = solver(test2)
print(f'{test2} => {res}')

res = solver(test3)
print(f'{test3} => {res}')

res = solver(test4)
print(f"{test4} => {res}")

res = solver(test5)
print(f'{test5} => {res}')

res = solver(test7)
print(f"{test7} => {res}")

res = solver(test8)
print(f"{test8} => {res}")

user_input = input("Введите арифметического выражени: ")
result = solver(user_input)
print(f'{user_input} => {result}')
