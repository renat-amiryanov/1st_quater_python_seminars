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


def write_to_file(message, file_name='text.enc'):
    """
    Функция записи в файл

    :param message: Данные которые нужно записать в файл
    :param file_name: Имя файла для записи данных
    :return:
    """
    print(f'[+] - Выполняем запись шифрованного сообщения "{message}" в файл {file_name}')
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(message)
        print(f'[+] - Запись выполнена. ')
    except:
        print(f'[-] - Запись не выполнена ')


def read_from_file(file_name='text.enc'):
    """
    Функция чтения данных из файла

    :param file_name: Имя файла откуда из которого считываем данные
    :return: Считанные данные
    """
    print(f'[+] - Выполняем чтение из файла {file_name}')
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = f.read()
            print(f'[+] - Чтение данных завершено успешно. ')
            return data
    except:
        print(f'[-] - Чтение данных не выполнено ')
def brute_force():
    """
    Функция ручного подбора ключа для расшивровывания сообщения
    :return:
    """

    is_right = False
    print('Попытаемся расшифровать шифрованное сообщение. )')
    while not is_right:
        try:
            key = int(input('Введите ключ для расшифровки: '))

            with open('original.txt', 'r', encoding='utf-8') as f:
                orig_message = f.read()

            data = read_from_file()
            decrypt = ceaser_chipher.decrypt(data, key)
            print(f'Результат расшифровывания ключем {key}: {decrypt}.', end=' ')
            if orig_message == decrypt:
                print('Ключ вверный!')
                is_right = True
            else:
                print('Ключ не верный!')
        except:
            print('Проверьте корректность ввода ключа!')

    print('Выход из программы')

def encrypt():

    origin_text = input('Введите сообщение для шифрованиня: ')

    with open('original.txt', 'w', encoding='utf-8') as f:
        f.write(origin_text)

    is_correct_key = False
    while not is_correct_key:
        try:
            key = int(input('Введите ключ шифрования: '))
            is_correct_key = True
        except:
            print('Проверьте корректность ввода ключа!')

    enc_text = ceaser_chipher.encrypt(origin_text, key)
    write_to_file(enc_text)


encrypt()
brute_force()
