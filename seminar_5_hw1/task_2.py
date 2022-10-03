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
import random


def check_user_input(num, num2, message=None):
    """
    Функция проверки корректности пользовательского ввода

    :param num: макс. кол-во конфет
    :param num2: кол-во конфет на столе
    :param message:
    :return:
    """
    msg1 = "Вы пытаетесь взять больше конфет чем возможно!"
    is_correct = False
    while not is_correct:
        try:
            value = int(input(message))
            if value > num or value > num2:
                print(msg1)
            else:
                is_correct = True
        except:
            print("Вы ввели не цифру!")
    return value


def candy_game():
    game_name = 'Игра в конфеты.'

    players = []
    is_finish = False
    game_mode = {1: "против человека", 2: "против бота"}

    print(game_name)
    selected_mode = int(input("Выберите режим игры 1 - против человека, 2 - против бота: "))
    print(f'Выбран режим игры {game_mode.get(selected_mode)}')

    if selected_mode == 1:
        players_number = int(input("Сколько игроков желает играть? "))
        for i in range(players_number):
            players.append(input(f'Введите имя {i} игрока: '))
    else:
        players.append('Bot')
        players.append(input(f'Введите имя игрока: '))

    total_amount_of_candy = int(input("Задайте количество конфет: "))
    max_candies = int(input("Задайте макс. количество конфет которое можно взять за 1 ход: "))

    print(f'На столе лежит {total_amount_of_candy} конфет.')
    print(f'Играют {", ".join(players)}')

    while not is_finish:
        for player in players:
            if player == 'Bot':
                candies = random.randint(1, max_candies) if max_candies < total_amount_of_candy else random.randint(1, total_amount_of_candy)
            else:
                candies = check_user_input(max_candies, total_amount_of_candy, f'{player} сколько конфет возьмешь: ')

            print(f'{player} взял {candies} конфет со стола.')
            total_amount_of_candy -= candies
            print(f'На столе осталось {total_amount_of_candy} конфет.')

            if 0 == total_amount_of_candy:
                print(f'{player} проиграл.')
                is_finish = True
                break

    print('Конец программы')


candy_game()
