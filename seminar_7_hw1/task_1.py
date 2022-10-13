"""
Зададча.
Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив внее систему логирования
Нарисовать "архитектуру" (блок схема) для работы данного приложения
Эта задача командная

"""
import re

import complex_number

a = '10_руб.'
b = '5+7j'
# mult = complex_number.mult(a, b)
# add = complex_number.add(a, b)
# sub = complex_number.sub(a, b)

# print(mult, complex(a)*complex(b))
# print(add, complex(a)+complex(b))
# print(sub,complex(a)-complex(b))


text = '-10+10'

container = []
val = 0
sing = 1
print(f'{container=}')
for t in text:

    if t.isdigit():
        val = sing * val * 10 + int(t)
    else:
        print(val)
        continue
        container.append(val)
print(f'{container=}')
