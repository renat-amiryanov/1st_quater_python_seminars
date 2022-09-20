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


file_name = 'students_scores.txt'
score = 5

# def file_reader(file):
#     data = {}
#     with open(file, 'r', encoding='utf-8') as file:
#         for f in file:
#             f = f.split(' ')
#             f[-1] = f[-1].replace('\n', '')
#             file = " ".join(f[0:2])
#             mark = f[2]
#             data[file] = mark
#     return data

# def chage(dic):
#     chan = {}
#     for key, value in dic.items():
#         if int(value) > 4:
#             student = key.upper()
#             chan[student] = value
#         else:
#             chan[key] = value
#     return chan

# def file_writer(file,dic):
#     with open(file,'w', encoding='utf-8') as file:
#         for key, value in dic.items():
#             file.write(f'{key} {value}\n')

# print(file_reader(file_name))
# print(chage(file_reader(file_name)))
# file_writer('students_scores.txt', chage(file_reader(file_name)))

with open(file_name, 'r', encoding='utf-8') as wa_file:
    lines = [line.rstrip() for line in wa_file]
    print(lines)

