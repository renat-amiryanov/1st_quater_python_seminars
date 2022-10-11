"""
Зададча.
Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив внее систему логирования
Нарисовать "архитектуру" (блок схема) для работы данного приложения
Эта задача командная

"""
import complex_number

a = '3+2i'
b = '3+2'
# mult = complex_number.mult(a, b)
# add = complex_number.add(a, b)
# sub = complex_number.sub(a, b)

# print(mult)
# print(add)
# print(sub)

def f(expr):
    sign = []
    numbers = []
    i = 0
    while i < len(expr):
        if expr[i] == '-':
            sign.append(expr[i])
        elif expr[i].isdigit() and sign:
            val = sign.pop() + expr[i]
            numbers.append(val)
        elif expr[i].isdigit():
            j = 0
            val=0
            while j < len(expr) and expr[j].isdigit():
                val = (val * 10) + int(expr[j])
                j += 1
            numbers.append(val)
        i += 1
    return numbers


print(f(b))