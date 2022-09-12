"""
Задача 2. Напишите программу которая принимает на вход число N и выдает набор произведений
(набор это список) чисел от 1 до N
Не используйте функцию math.factorial
добавьте проверку числа N чтобы пользователь не мог ввести буквы
пример:
N = 4 -> [1, 2, 6, 24]

"""


def check_user_input(message='Enter a number, please: '):
    is_correct = False
    while not is_correct:
        try:
            user_input = input(message)
            user_input = int(user_input)
            is_correct = True
        except:
            print('Incorrect input! It is not number. Please, try again.')
    return user_input


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def get_factorial_sequence(n):
    return [factorial(i) for i in range(1, n + 1)]


number = check_user_input()
factorial_sequence = get_factorial_sequence(number)
print(f'N = {number} -> {factorial_sequence}')


