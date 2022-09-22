"""
Задача 4.
Шифр Цезаря - способ шифрования где каждая бука смещается на определенно количество
символов влево или вправо. При расшифровке происходит обратная операция.
К примеру, слово "абба"  можно зашифровать "бввб" - сдвиг на 1 вправо, "вггв" -  сдвиг на вправо 2
Написать функцию которая записывает в файл шифрованный текст, а так же функцию которая спрашивает ключ,
считывает текст и дешивровывает его.
"""

# Импортируем  модуль
from libs import ceaser_chipher


def display(msg):
    print(f'Расшифрованный текст: {msg}')


def write_to_file(message, file_name='text.enc'):
    """
    Функция записи в файл

    :param message: Данные который нужно записать в файл
    :param file_name: Имя файла для записи данных
    :return:
    """
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(message)


def read_from_file(file_name='text.enc'):
    """
    Функция чтения данных из файла

    :param file_name: Имя файла откуда еа
    :return:
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()


def brute_force():
    while True:
        key = int(input('Введите ключ для расшифровки: '))
        data = read_from_file()
        decrypt = ceaser_chipher.decrypt(data, key)
        display(f'Ключ {key} ->{decrypt}')

origin_text = input('Введите текст который хотите зашифровать: ')
key = int(input('Введите ключ шифрования: '))
enc_text = ceaser_chipher.encrypt(origin_text, key)
write_to_file(enc_text)
brute_force()
