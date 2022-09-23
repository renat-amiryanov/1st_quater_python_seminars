"""
Задача 1.
Написать программу удаляющую из текста все слова содержащие "абв"
абвгдейка - это передача

"""


def demo():
    text = 'абвгдейка - это передача'
    sub_str = 'абв'
    li_c = [t for t in text.split() if sub_str not in t]
    print(f'{text} =>', *li_c)


demo()
