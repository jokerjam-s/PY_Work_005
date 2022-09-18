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


# ход бота
def bot_run(candies: int, smart: bool = False) -> int:
        
    if smart:
        # умный бот
        if candies <= CANDIES_LIMIT:    # забрать остаток
            result = candies
        else:
            result = CANDIES_LIMIT      # берем макс. лимит по умолчанию

            # для победы c максимальным забором конфет нужно иметь нечетное к-во ходов
            cnt_step = candies // CANDIES_LIMIT 
            if candies % CANDIES_LIMIT > 0:
                cnt_step += 1
            
            if cnt_step % 2 == 0:    # ситуация проигрышная, пробуем изменить
                if candies - CANDIES_LIMIT < CANDIES_LIMIT:
                    result = candies - CANDIES_LIMIT - 1
    else:
        # глупый бот
        result = random.randint(1,CANDIES_LIMIT)

    return result
    

## MAIN ##
# игра с ботом
bot_using = False
bot_smart = False

# жеребъевка
active_player = random.randint(1,2)
# начальное количество конфет
rest_candies = CANDIES

# выяснить условия игры
if int(input('играть с ботом (1-да)?')) == 1:
    bot_using = True
if bot_using:
    if int(input('бот умный (1-да)?')) == 1:
        bot_smart = True

info = 'бот' if bot_using else 'человек'
# ход игры
while rest_candies > 0:
    # отображение информации
    os.system('cls')
    print(f'игрок 1 - человек, игрок 2 - {info}')
    print(f'на столе {rest_candies} конфет, можно взять [1 .. {CANDIES_LIMIT}]')
    print(f'ход {active_player} игрока')

    # забор конфет
    if bot_using and active_player==2:
        # играет бот
        get_candies = bot_run(rest_candies, bot_smart)
        print(f'бот взял {get_candies} конфет')
        os.system('pause')
    else:
        # игает человек
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




