import random

mass = ['ножницы', 'камень', 'бумага']
count = [0, 0]
for i in range(3):
    print(f'Раунд {i + 1}')

    flag = True
    while flag:
        your_hod = input('Введите ваш ход (камень, ножницы или бумага): ')
        hod_comp = random.choice(mass)

        if hod_comp == your_hod:
            print('ничья!')

        elif your_hod == 'камень':
            if hod_comp == 'ножницы':
                count[0] += 1
                print('Ты выиграл')
            else:
                count[1] += 1
                print('Ты не выиграл')
            flag = False

        elif your_hod == 'ножницы':
            if hod_comp == 'бумага':
                count[0] += 1
                print('Ты выиграл')
            else:
                count[1] += 1
                print('Ты не выиграл')
            flag = False

        else:
            if hod_comp == 'камень':
                count[0] += 1
                print('Ты выиграл')
            else:
                count[1] += 1
                print('Ты не выиграл')
            flag = False

        print(f'Счет: {count[0]}:{count[1]}')



