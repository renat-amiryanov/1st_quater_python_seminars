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
players_number = int(input("Сколько игроков желает играть? "))
players = []
for i in range(players_number):
    players.append(input(f'Введите имя {i} игрока: '))
is_finish = False
while not is_finish:
    for player in players:
        candies = int(input(f'{player} конфет возьмешь: '))
        total_amount_of_candy -= candies
        if total_amount_of_candy == 0:
            print(f'{player} проиграл.')
            print('Конец программы')
            is_finish = True


