


def mult(a, b):
    """
    Функция умножения комплексных чисел
    """

    x = [int(x) for x in a.replace('i', '').split('+')]
    y = [int(y) for y in b.replace('i', '').replace('j', '').replace('-', '+-').split('+')]
    return str(x[0] * y[0] - x[1] * y[1]) + '+' + str(x[0] * y[1] + x[1] * y[0]) + 'i'


def add(a, b):
    """
    Функция сложения комплексных чисел
    """
    x = [int(x) for x in a.replace('i', '').replace('j', '').split('+')]
    y = [int(y) for y in b.replace('i', '').replace('j', '').split('+')]
    return str(x[0] + y[0]) + '+' +str(x[1] + y[1]) + 'i'


def sub(a, b):
    """
    Функция вычитания комплексных чисел
    """
    x = [int(x) for x in a.replace('i', '').replace('j', '').split('+')]
    y = [int(y) for y in b.replace('i', '').replace('j', '').split('+')]
    return str(x[0] + y[0]) + str(x[1] + y[1]) + 'i'


def div(a, b):
    """
    Функция деления комплексных чисел
    """
    pass
