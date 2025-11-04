import random

right_num = random.randint(1, 100)


for i in range(3):
    number = int(input('Введите целое число: '))
    if number == right_num:
        print('Ты выиграл')
        break
    elif number < right_num and i < 2:
        print("Загаданное число больше")
    elif i < 2:
        print("Загаданное число меньше")

    if i == 1:
        if right_num % 2 == 0:
            print('число четное')
        else:
            print('число не четное')

print(f'правильное число - {right_num}')

