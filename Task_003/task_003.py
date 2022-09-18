# Создайте программу для игры в ""Крестики-нолики"".
#
# 
#

from itertools import count
import numpy as np
import os


# заполнениеи позиции поля
def show_pos(pos) -> str:
    match pos:
        case 0:
            result = ' '
        case 1:
            result = 'X'
        case _:
            result = 'O'
    return result


# отображенеи игрового поля
def show_field(fld: np):
    os.system('cls')

    line_str = '---------------' 
    print('    a   b   c')
    for i in range(0, 3):
        strk = f'{i+1} | '
        for j in range(0,3):
            strk += f'{show_pos(fld[i,j])} | '
        print(line_str)
        print(strk)
    print(line_str)


# проверка окончания игры
# 0 - игра не окончена
# 1 - победа 1го игрока
# 2 - победа второго
# 3 - ничья
def gamem_over(fl: np)-> int:
    if (sum(fl[0,:]) == 3 or sum(fl[1,:]) == 3 or sum(fl[2,:]) == 3 
        or sum(fl[:,0]) == 3 or sum(fl[:,1]) == 3 or sum(fl[:,2]) == 3
        or sum(np.diagonal(fl, 0)) == 3 or sum(np.diagonal(fl, 1)) == 3):
        return 1
    
    if (sum(fl[0,:]) == 12 or sum(fl[1,:]) == 12 or sum(fl[2,:]) == 12
        or sum(fl[:,0]) == 12 or sum(fl[:,1]) == 12 or sum(fl[:,2]) == 12
        or sum(np.diagonal(fl, 0)) == 12 or sum(np.diagonal(fl, 1)) == 12):
        return 2
    
    if (fl == 0).sum() == 0:
        return 3
    
    return 0


## MAIN ##

fields = np.zeros((3,3))

fields[0,0] = 1
fields[1,1] = 1
fields[2,2] = 1

fields[1,2] = 4


show_field(fields)

print(gamem_over(fields))