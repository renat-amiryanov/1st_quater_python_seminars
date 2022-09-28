"""

Задача 2.
Создайте программу для игры с конфетами человек против человека.
Условие задачи:
На столе лежит 2021 конфета(или сколько вы зададите).
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет(или сколько вы зададите).
Тот, кто берет последнюю конфету - проиграл.
Предусмотрите последний ход, ибо там конфет остается меньше.

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"
"""

game_name = 'Игра в конфеты'
total_amount_of_candy = 2021  #
max_candies = 28
total_amount_of_candy = int(input("Задайте количество конфет: "))
max_candies = int(input("Задайте макс. количество конфет которое можно взять за 1 ход^ "))
players_number = int(input("Сколько игроков желает играть? "))
players = []
is_finish = False

for i in range(players_number):
    players.append(input(f'Введите имя {i} игрока: '))

print(f'На столе лежит {total_amount_of_candy} конфет.')

while not is_finish:
    for player in players:
        candies = int(input(f'{player} сколько конфет возьмешь: '))
        total_amount_of_candy -= candies
        print(f'На столе осталось {total_amount_of_candy} конфет.')
        #
        if 0 <= total_amount_of_candy <= 1:
            print(f'{player} проиграл.')
            is_finish = True

print('Конец программы')
