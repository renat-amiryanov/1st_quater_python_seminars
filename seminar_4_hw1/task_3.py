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

import re

file_name = 'students_scores.txt'
score = 5.
# with open(file_name, 'r', encoding='utf-8') as file:
#     data = list()
#     for line in file:
#         print(line.replace('\n',''))
#         data.append(line.splitlines())
#         # data.append(re.split('(\d+)', line))
#
#
# print(data)

file_string = '''Ангела Меркель 5\nАндрей Валетов 5\nФредди Меркури 3\nАнастасия Пономарева 4'''

print(file_string)
print(file_string.split('\n'))

print(file_string2)

