# Написать программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет


def is_holyday(day):
    if 1 <= day <= 5:
        return False
    elif 6 <= day <= 7:
        return True
    

def is_holyday2(day):
    week_days = [1, 2, 3, 4, 5, 6, 7]
    if day in week_days[0:4]:
        return False
    elif day in week_days[5:]:
        return True
    else:
        return


number_day_of_week = int(input('Введите цифру (от 1 до 7), обозначающую день недели: '))


if is_holyday(number_day_of_week):
    print(f'{number_day_of_week} -> да')
else:
    print(f'{number_day_of_week} -> нет')


