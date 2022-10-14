# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

"""

x   y   z       ¬(X ⋁ Y ⋁ Z)    ¬X ⋀ ¬Y ⋀ ¬Z
--------------------------------------------------------------------
0   0   0       1                1
0   0   1       1                1
0   1   0       1                1
0   1   1       1                1
1   0   0       1                1
1   0   1       1                1
1   1   0       1                1
1   1   1       0                0

"""
def display_table_of_thruth():
    print(f'x\ty\tz', end='\t\t')
    print('¬(X ⋁ Y ⋁ Z)', end='\t')
    print('¬X ⋀ ¬Y ⋀ ¬Z', end='\t')
    print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')

    print('-' * 77)
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                print(f'{x}\t{y}\t{z}', end='\t\t')
                expr1 = 1 if not (x and y and z) else 0
                print(expr1, end='\t\t\t\t')
                expr2 = 1 if (not x) or (not y) or (not z) else 0
                print(expr2, end='\t\t\t\t')
                print(1 if expr1 == expr2 else 0)

display_table_of_thruth()

