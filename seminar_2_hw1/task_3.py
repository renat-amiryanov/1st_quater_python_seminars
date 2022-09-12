# Задача 3. Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

def is_palindrome(number: int):
    # Исключаем отрицительные числа, число 0, и числа 10, 20, ..., 100, ..., 110..
    if number < 0 or (number != 0 and number % 10 == 0):
        return False
    revers = 0
    while number > revers:
        revers = revers * 10 + number % 10
        number /= 10
    return number == revers or number == revers / 10


def reversing_number(input_value):
    revers = 0
    while input_value > revers:
        revers = revers * 10 + input_value % 10
        input_value /= 10
    return revers


num = 10201
print(is_palindrome(num))

