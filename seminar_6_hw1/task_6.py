"""
Задача 6ю
Сформировать список из N членов последовательности.
Для N = 5: 1, -3, 9, -27, 81 и т.д.
"""

n = 5
sequence = list(map(lambda i: (-3) ** i, [i for i in range(n)]))
sequence = list(map(str,sequence))
print(', '.join(sequence))