def text_analiz(text):
    glas = 'уеыаоэяию'
    ne_glas = 'йцкнгшщзхфвпрлджчсмтб'

    col_glas = 0
    col_ne_glas = 0
    for i in text:
        if i in glas:
            col_glas += 1
        elif i in ne_glas:
            col_ne_glas += 1
    print(f'Количество гласных - {col_glas}')
    print(f'Количество согласных - {col_ne_glas}')

    col_prob = text.count(' ')
    print(f'Количество пробелов - {col_prob}')


    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    slow = {}
    top = []
    for k in alphabet:
        slow[k] = text.count(k)

    top.append(max(slow, key=slow.get))
    del slow[max(slow, key=slow.get)]
    top.append(max(slow, key=slow.get))
    del slow[max(slow, key=slow.get)]
    top.append(max(slow, key=slow.get))
    del slow[max(slow, key=slow.get)]

    print(f'Топ букв - {top[0]}, {top[1]}, {top[2]}')

    text = ' '.join(text.split())
    col_slow = text.count(' ') + 1

    print(f'Количество слов - {col_slow}')

text = input('Введите текст: ')
text_analiz(text)
