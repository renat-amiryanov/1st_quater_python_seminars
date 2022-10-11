"""
Зададча.
Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив внее систему логирования
Нарисовать "архитектуру" (блок схема) для работы данного приложения
Эта задача командная

"""
import re

import complex_number

a = '3+2j'
b = '3+2j'
mult = complex_number.mult(a, b)
# add = complex_number.add(a, b)
# sub = complex_number.sub(a, b)

print(mult, complex(a)*complex(b))
# print(add, complex(a)+complex(b))
# print(sub,complex(a)-complex(b))

