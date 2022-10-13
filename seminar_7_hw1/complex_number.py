import re


def mult(a, b):
    """
    Функция умножения комплексных чисел
    """
    # (a+bi)(c+di) = (ac-bd)+(ad+bc)i
    x = [int(x) for x in re.findall('[-+]?\d+', a)]

    y = [int(y) for y in re.findall('[-+]?\d+', b)]
    print(x, x[0] * y[0] - x[1] * y[1])
    print(y, x[0] * y[1] + x[1] * y[0])
    return str(x[0] * y[0] - x[1] * y[1]) + str(x[0] * y[1] + x[1] * y[0]) + 'j'


def add(a, b):
    """
    Функция сложения комплексных чисел
    """
    # (a+bi)+(c+di) = (a+c)+(b+c)i
    x = [int(x) for x in re.findall('[-+]?\d+', a)]
    y = [int(y) for y in re.findall('[-+]?\d+', b)]
    return str(x[0] + y[0]) + str(x[1] + y[1]) + 'j'


def sub(a, b):
    """
    Функция вычитания комплексных чисел
    """
    #(a+bi)-(c+di) = (a-c)+(b-c)i
    x = [int(x) for x in re.findall('[-+]?\d+', a)]
    y = [int(y) for y in re.findall('[-+]?\d+', b)]
    return str(x[0] - y[0]) + '-' + str(x[1] - y[1]) + 'j'


def div(a, b):
    """
    Функция деления комплексных чисел
    """
    # (a+bi)/(c+di) = (ac+bd)/(c^2+d^2)+(bc-ab)/(c^2+d^2)i
    pass
