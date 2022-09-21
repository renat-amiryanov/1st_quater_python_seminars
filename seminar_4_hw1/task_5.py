"""

Задача 5.
Реализовать RLE алгоритм.
Реализовать модуль сжатия и восстановления данных
Входные данные и выходные данне хранатся в отдельных текстовый файлах.
Файл первый:
Сжатый файл:

"""
from libs import RLE

source_file = 'task_5_source.txt'
target_file = 'task_5_compressed.txt'
target_file1 = 'task_5_uncompressed.txt'


def compress_rle(source, target):
    """
    Функция сжатия данных RLE алгортмом

    :param source: Файл с исходными данными
    :param target: Файл с сжатыми данными
    :return:
    """
    print('Начало работы функции compress_rle()')
    with open(source, 'r', encoding='utf-8') as file:
        print(f'[+] - получаем данные с файла {source}')
        content = file.read()
        print(f'[+] - данные получены: {content}')
        print(f'[+] - сжимаем данные ')
        compressed_content = RLE.compress(content)
        print(f'[+] - данные сжаты: {compressed_content}')

    with open(target, 'w', encoding='utf-8') as file:
        print(f'[+] - пишем данные в файла {target}')
        file.write(compressed_content)
        print(f'[+] - данные записаны')
    print(f'Конец работы функции compress_rle()\n')
def uncompress_rle(source, target):
    """
    Функция восттановления данных сжатых RLE алгоритмом

    :param source: Файл с сжатыми данными
    :param target: Файл с восстановленными данным
    :return:
    """
    print('Начало работы функции uncompress_rle()')
    with open(source, 'r', encoding='utf-8') as file:
        print(f'[+] - полчаем данные с файла {source}')
        content = file.read()
        print(f'[+] - данные получены: {content}')
        print(f'[+] - восстанавливаем данные ')
        uncompressed_content = RLE.uncompress(content)
        print(f'[+] - данные восттановлены: {uncompressed_content}')

    with open(target, 'w', encoding='utf-8') as file:
        print(f'[+] - пишем данные в файла {target}')
        file.write(uncompressed_content)
        print(f'[+] - данные записаны')
    print(f'Конец работы функции uncompress_rle()\n')

compress_rle(source_file, target_file)
uncompress_rle(target_file, target_file1)