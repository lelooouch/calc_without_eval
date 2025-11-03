def shifr(text, num):
    alphabet_eng = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    new_text = []
    if text[0] in alphabet_eng:
        for i in range(len(text)):
            a = alphabet_eng.index(text[i]) + num
            if a > 25:
                a = a % 25 - 1 
            new_text.append(alphabet_eng[a])
        return ''.join(new_text)
    else:
        for i in range(len(text)):
            a = alphabet_rus.index(text[i]) + num
            if a > 32:
                a = a % 32 - 1 
            new_text.append(alphabet_rus[a])
        return ''.join(new_text)


def de_shifr(text, num):
    alphabet_eng = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    new_text = []
    if text[0] in alphabet_eng:
        for i in range(len(text)):
            a = alphabet_eng.index(text[i]) - num
            if a < 0:
                a = a % 25 + 1 
            new_text.append(alphabet_eng[a])
        return ''.join(new_text)
    else:
        for i in range(len(text)):
            a = alphabet_rus.index(text[i]) - num
            if a < 0:
                a = a % 32 + 1 
            new_text.append(alphabet_rus[a])
        return ''.join(new_text)

text = input("введите строку:")
num = int(input("введите число:"))

if text.isalpha():
    print(f'Зашифрованное - {shifr(text, num)}')
    print(f'Расшифрованное - {de_shifr(text, num)}')
else:
    print('ошибка')

