# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
#

import itertools as itl
import os

# кодирование
def encode_rle(data: str) -> str:
    encode_str = []
    for ch, sm in itl.groupby(data):
        encode_str.extend(str(len(tuple(sm))) + ch)
    
    return ''.join(encode_str)


# декодирование
def decode_rle(data: str) -> str:
    # в строке должно быть четное число символов
    if len(data) % 2 != 0 or len(data) == 0:
        return ''

    decode_str = []
    for i in range(0,len(data),2):
        if data[i].isdigit():
            decode_str.extend(list(itl.repeat(data[i+1], int(data[i]))))
    
    return ''.join(decode_str)


## MAIN ## 
os.system('cls')

strk = 'aaaasssDDDDddddffdffff'
print(f'Строка        : {strk}')

enc_str = encode_rle(strk)
print(f'Код           : {enc_str}')

dec_str = decode_rle(enc_str)
print(f'Расшифровка   : {dec_str}')

