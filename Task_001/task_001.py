# Напишите программу, удаляющую из текста все слова, содержащие "абв".
#
# текст будем брать из файла в виде строки, словом считается набор символов, отделенный от 
# других пробелами
#

with open('text.txt') as data:
    txt = data.readline()

# исходный текст
print(txt)

# список слов
words = txt.split(' ')

# новый текст
new_txt = " ".join(filter(lambda s: s.find('абв')<0, words))

print(new_txt)

