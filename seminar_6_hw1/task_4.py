"""
4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
Примеры
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1
"""

lst1, s1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"  # 3
lst2, s2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу"  # 5
lst3, s3 = ["йцу", "фыв", "ячс", "цук", "йцукен"], "qwe"  # -1
lst4, s4 = ["123", "234", 123, "567"], "123"  # -1
lst5, s5 = [], "123"  # -1


def get_2nd_occurance_index(words, target):
    get_indices = lambda words, target: [i for i in range(len(words)) if words[i] == target]
    return [get_indices(words, target)[1] if len(get_indices(words, target)) > 1 else -1]


print(f'список: {lst1}, ищем: {s1}, ответ: {get_2nd_occurance_index(lst1, s1)}')
print(f'список: {lst2}, ищем: {s2}, ответ: {get_2nd_occurance_index(lst2, s2)}')
print(f'список: {lst3}, ищем: {s3}, ответ: {get_2nd_occurance_index(lst3, s3)}')
print(f'список: {lst4}, ищем: {s4}, ответ: {get_2nd_occurance_index(lst4, s4)}')
print(f'список: {lst5}, ищем: {s5}, ответ: {get_2nd_occurance_index(lst5, s5)}')
