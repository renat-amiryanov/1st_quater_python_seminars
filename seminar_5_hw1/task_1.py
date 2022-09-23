"""
Задача 1.
Написать программу удаляющую из текста все слова содержащие "абв"
абвгдейка - это передача

"""


def demo():
    """
    Демонстрационная функция
    :return:
    """
    text = 'абвгдейка - это передача'
    sub_str = 'абв'
    value = [t for t in text.split() if sub_str not in t]
    print(f'"{text}" => "{" ".join(value)}"')


def remove_strings_contains_sub_string(string, sub_string):
    """
    Функция которая удаляет слова из текста содержащие заданную подстроку

    :param string:
    :param sub_string:
    :return:
    """
    value = [s for s in string.split() if sub_string not in s]
    return ' '.join(value)


demo()


def do_it():

    print('Программа удаления из текста все слова содержашие подстроку.')
    message = input("Введите текст: ")
    sub = input("Введите подстроку: ")

    if not message and not sub:
        print("Ничего не введено. Программа завершает свою работу.")
        return

    before = len(message.split())
    output = remove_strings_contains_sub_string(message, sub)
    after = len(output.split())

    print(f"Кол-во удалленных: {before - after} ")
    print("Результат: ", end='')
    print(''.join([output if len(output) > 0 else 'Все слова удалены.']))
    print("Конец программы.")


do_it()

