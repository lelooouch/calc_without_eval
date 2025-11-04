import random


def random_password_generator(down_reg, up_reg, spec_simb, col_num, len_pas):
    password = []
    alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    spec = '№$%?*<>!'
    if down_reg == 'да' or down_reg == 'Да':
        password.append(random.choice(alphabet))
    if up_reg == 'да' or up_reg == 'Да':
        password.append(random.choice(alphabet).upper())
    if spec_simb == 'да' or spec_simb == 'Да':
        password.append(random.choice(spec))
    for i in range(col_num):
        password.append(str(random.randint(0, 9)))
    if len_pas > len(password):
        while len(password) != len_pas:
            if down_reg:
                password.append(random.choice(alphabet))
            elif up_reg:
                password.append(random.choice(alphabet).upper())
            else:
                password.append(random.choice(spec))
    random.shuffle(password)
    return ''.join(password)

down_reg = input("Будет ли в пароле наличие нижнего регистра?")
down_up = input("Будет ли в пароле наличие верхнего регистра?")
spec_simb = input("Будет ли в пароле наличие спец.символов регистра?")
col_num = int(input("Количество цифр в пароле:"))
len_pas = int(input("Длина пароля:"))

print(random_password_generator(down_reg, down_up, spec_simb, col_num, len_pas))


