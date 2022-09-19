# Создайте программу для игры в ""Крестики-нолики"".
#
#
#

import random
import numpy as np
import os

# заполнение ячейки поля
def show_pos(pos) -> str:
    match pos:
        case 0:
            result = ' '
        case 1:
            result = 'X'
        case _:
            result = 'O'
    return result


# отображение игрового поля
def show_field(fld: np):
    os.system('cls')

    line_str = '  -------------'
    print('игрок 1 - Х, игрок 2 - O')
    print('    a   b   c')
    for i in range(0, 3):
        strk = f'{i+1} | '
        for j in range(0, 3):
            strk += f'{show_pos(fld[i,j])} | '
        print(line_str)
        print(strk)
    print(line_str)


# проверка окончания игры
# 0 - игра не окончена
# 1 - победа 1го игрока
# 2 - победа второго
# 3 - ничья
def game_over(fl: np) -> int:
    # проверить победу 1го игрока
    win = sum(np.diagonal(fl, 0)) == 3 or sum(np.diagonal(fl, 1)) == 3
    for i in range(0, 3):
        win = win or sum(fl[:, i]) == 3 or sum(fl[i, :]) == 3
    if win:
        return 1

    # проверить победу 2го игрока
    win = sum(np.diagonal(fl, 0)) == 12 or sum(np.diagonal(fl, 1)) == 12
    for i in range(0, 3):
        win = win or sum(fl[:, i]) == 12 or sum(fl[i, :]) == 12
    if win:
        return 2

    # проверить ничью
    if (fl == 0).sum() == 0:
        return 3

    # играем дальше
    return 0

# игрок делает ход
def make_step(gamer_no: int):
    print(f'ход {gamer_no} игрока')
    field = input('введите коорд. поля:')
    if field[0].isdigit() and field[1].isalpha():
        x = int(field[0])-1
        y = ord(field[1]) - ord('a')
    elif field[1].isdigit() and field[0].isalpha():
        x = int(field[1])-1
        y = ord(field[0]) - ord('a')
    else:
        x = -1
        y = -1
    return x, y


## MAIN ##

fields = np.zeros((3, 3))

# выбор игрока
active_gamer = random.randint(1, 2)

while game_over(fields) == 0:
    show_field(fields)
    row, col = make_step(active_gamer)

    if row not in range(0, 3) or col not in range(0, 3):
        print('неверные координаты!')
        os.system('pause')
    elif fields[row, col] != 0:
        print('неверный ход!')
        os.system('pause')
    else:
        fields[row, col] = 1 if active_gamer == 1 else 4
        active_gamer = 1 if active_gamer == 2 else 2


show_field(fields)
result = game_over(fields)
if result in (1,2):
    print(f'победа игрока {result}')
else:
    print('ничья')

