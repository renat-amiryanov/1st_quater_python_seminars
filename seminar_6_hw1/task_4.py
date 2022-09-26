"""
4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
Примеры
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1
"""


def display(words, search_word):
    res = [(i, word) for i,word in enumerate(words) if word == search_word]

lst1, s1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"
lst2, s2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу"
lst3, s3 = ["йцу", "фыв", "ячс", "цук", "йцукен"], "qwe"
lst4, s4 = ["123", "234", 123, "567"], "123"
lst5, s5 = [], "123"
# print(display(lst1, s1))
# print(display(lst2, s2))
# print(display(lst3, s3))
# print(display(lst4, s4))
# print(display(lst5, s5))

def getIndex(lst, s):
  count = 0
  for i, w in enumerate(lst):
    if w == s:
      count += 1
      if count == 2:
        return i
  else:
    return -1
# def display(words, search_word):
#     step1 = [(i, word) for i,word in enumerate(words)]
#     # find = [lambda w, s:  if w == s]
print(getIndex(lst2, s2))
