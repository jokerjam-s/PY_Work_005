# Создайте программу для игры с конфетами человек против человека.
# 
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

import os
import random

# Всего конфет
CANDIES = 2021
# ограничение на хапание конфет
CANDIES_LIMIT = 28

active_player = random.randint(1,2)
rest_candies = CANDIES

# игра с ботом
using_bot = False

# выяснить условия игры
if int(input('играть с ботом (1-да)?')):
    using_bot = True

while rest_candies > 0:
    # отображение информации
    os.system('cls')
    print(f'на столе {rest_candies} конфет, можно взять [1 .. {CANDIES_LIMIT}]')
    print(f'ход {active_player} игрока')

    # забор конфет
    if using_bot and active_player==2:
        # играет бот
    else:
        get_candies = int(input('сколько конфет берем: '))
    


    # проверка правил, выигрыша
    if get_candies not in range(1, CANDIES_LIMIT+1):
        print('неверный ход')
        os.system('pause')
    else:
        rest_candies -= get_candies
        if rest_candies > 0:
            if active_player == 1:
                active_player = 2
            else:
                active_player = 1
        else:
            print(f'выиграл {active_player} игрок')




