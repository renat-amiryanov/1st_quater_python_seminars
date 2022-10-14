"""
Задача 3.
В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов,
которые имеют средний балл более «4».
Нужно перезаписать файл.

Пример:
Ангела Меркель 5
Андрей Валетов 5
Фредди Меркури 3
Анастасия Пономарева 4

Программа выдаст:
АНГЕЛА МЕРКЕЛЬ 5
АНДРЕЙ ВАЛЕТОВ 5
Фредди Меркури 3
Анастасия Пономарева 4
"""


def read_from_file(file):
    """
    Функция чтения из файла данных и возврата данных в словаре

    :param file:Имя фойла откуда читаем данные
    :return: возврат словаря
    """
    data = {}
    with open(file, 'r', encoding='utf-8') as file:
        for f in file:
            f = f.split(' ')
            f[-1] = f[-1].replace('\n', '')
            file = " ".join(f[0:2])
            mark = f[2]
            data[file] = mark
    return data


def modify_data(dic):
    """
    Функция измения на прописные буквы фамилии тех студентов,
    которые имеют средний балл более «4».

    :param dic: Исходный словарь с данными
    :return: Изменненый словарь
    """
    data_dic = {}

    for key, value in dic.items():
        if int(value) > 4:
            student = key.upper()
            data_dic[student] = value
        else:
            data_dic[key] = value
    return data_dic


def write_to_file(file, dic):
    """
    Функция записи данных в файл
    :param file: Имя файла для записи
    :param dic: Словать который пишем в файл
    :return:
    """
    with open(file, 'w', encoding='utf-8') as file:
        for key, value in dic.items():
            file.write(f'{key} {value}\n')


def display(file):
    with open(file, 'r', encoding='utf-8') as file:
        for f in file:
            print(f.rsplit('\n')[0])
        print()


file_with_data = 'students_scores.txt'
display(file_with_data)
data_from_file = read_from_file(file_with_data)
modified_data = modify_data(data_from_file)
write_to_file(file_with_data, modified_data)
display(file_with_data)
