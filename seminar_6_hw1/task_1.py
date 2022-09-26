"""
Задача 1.
Определить, присутствует ли в заданном списке строк, некоторое число

"""


def my_func(words):
    """
    Фукнция которая определяет, присутствует ли в заданном списке строк, некоторое число
    :param words: Список строк
    :return:
    """

    return [word for word in words for ch in word if ch.isdigit()]

def display():
    user_input = str.split(input('Введите текст: '))
    res = my_func(user_input)
    if(len(res)!=0):
        print(f'Заданном списке строк имеются числа в словах {" ".join([str(el) for el in res])}')
    else:
        print('В заданном списке строк, числа отсутствуют.')

display()






