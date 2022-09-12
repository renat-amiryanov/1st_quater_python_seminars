"""
Задача 2. Напишите программу которая принимает на вход число N и выдает набор произведений
(набор это список) чисел от 1 до N
Не используйте функцию math.factorial
добавьте проверку числа N чтобы пользователь не мог ввести буквы
пример:
N = 4 -> [1, 2, 6, 24]

"""


def check_user_input(message='Enter a numebr, please: '):
    is_correct = False
    while not is_correct:
        try:
            user_input = input(message)
            user_input = int(user_input)
            is_correct = True
        except:
            print('Incorrect input! It is not number. Please, try again.')
    return user_input


number = check_user_input()


def fact(n):
    if n == 1:
        return 1
    else:
        return


print(fact(number))
