# Задача 3. Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

def reversing_number(input_value):
    # Функция которая переворачивает число
    revers = 0
    while input_value > 0:
        revers = revers * 10 + input_value % 10
        input_value //= 10
    return revers


def is_palindrome(number):
    # функция проверяющая является ли число палиндромом или нет
    if number < 0 or (number != 0 and number % 10 == 0):
        return False
    return number == reversing_number(number) or number == reversing_number(number) // 10


def display(num):
    print(f'Число {num} {"является палиндромом." if is_palindrome(num) else "не является палиндромом."}')
    while not is_palindrome(num):
        revers = reversing_number(num)
        print(f'Перевернутое число {revers} не равно исходному {num}')
        print(f'Складываем исходное и перевернутое число и проверяются на палиндром еще раз.')
        num = num + revers
    print(f'Число {num} {"является палиндромом." if is_palindrome(num) else "не является палиндромом."}')


num = int(input('Введите число для проверки палиндрома числа: '))

display(num)
