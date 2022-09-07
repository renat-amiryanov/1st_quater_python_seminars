# Написать программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет


def check_user_input():
    while True:
        try:
            value = int(input('Введите цифру, обозначающую день недели: '))
            break
        except:
            print("Вы ввели не цифру!")
    return value


def is_holiday(day):
    if 1 <= day <= 5:
        return 'busy-day'
    elif 6 <= day <= 7:
        return 'holiday'
    else:
        return 'dummy-day'


print('''Программа, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.''')

number_day_of_week = check_user_input()

if is_holiday(number_day_of_week) == 'holiday':
    print(f'{number_day_of_week} -> да')
elif is_holiday(number_day_of_week) == 'busy-day':
    print(f'{number_day_of_week} -> нет')
elif is_holiday(number_day_of_week) == 'dummy-day':
    print(f'{number_day_of_week} -> такого номера дня недели не существует')
