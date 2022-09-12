"""
Задача1. Написать программу, которая принимает на вход вещественное число
и показывает сумму его цифр.
Учтите что числа могут быть отрицательными
Пример:
67.82 - 23
0.56 -11
"""


# Для проверки правильности пользовательского ввода
def check_user_input(message='Enter a number, please: '):
    is_correct = False
    while not is_correct:
        try:
            user_input = input(message)
            user_input = float(user_input)
            is_correct = True
        except:
            print('Incorrect input!')
    return user_input


def calculate_sum(n):
    n = abs(n)
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    return int(total)


def franken(value):
    value = str(value).replace('.', '')
    return int(value)


print(f'{67.82} -> {calculate_sum(franken(67.82))}')
print(f'{0.56} -> {calculate_sum(franken(0.56))}')

number = check_user_input()
print(f'{number} -> {calculate_sum(franken(number))}')

