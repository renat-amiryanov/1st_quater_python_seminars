# Написать программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет


def check_uset_input():
    while True:
        try:
            value = int(input('Enter number: '))
            break
        except:
            print("You must enter a digits!")
    return value


def is_holyday(day):
    if 1 <= day <= 5:
        return False
    elif 6 <= day <= 7:
        return True


number_day_of_week = check_uset_input()

if is_holyday(number_day_of_week):
    print(f'{number_day_of_week} -> да')
else:
    print(f'{number_day_of_week} -> нет')
