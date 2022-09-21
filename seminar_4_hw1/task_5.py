"""

Задача 5.
Реализовать RLE алгоритм.
Реализовать модуль сжатия и восстановления данныхю
Входные данные и выходные данне хранатся в отдельных текстовый файлах.
Файл первый:
Сжатый файл:

"""
from libs import RLE
text = 'AAABBB555FFF'
compressed_text = RLE.compress(text)
uncompressed_text = RLE.uncompress(compressed_text )
print(f'{text=}')
print(f'{compressed_text=}')
print(f'{uncompressed_text=}')
print(text == uncompressed_text)

