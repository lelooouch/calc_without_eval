def number_converter(number):
    num_m = []


    for i in range(len(str(number))-1, -1, -1):
        if i == 0:
            num_m.append(number)
        else:
            num_m.append((number // 10**i) * 10**i)
        number %= 10**i

    rim = []
    for item in num_m:
        if len(str(item)) == 4:
            rim.append('M' * (item//1000))
        elif len(str(item)) == 3:
            if item == 900:
                rim.append('CM')
            elif item == 400:
                rim.append('CD')
            else:
                rim.append('C' * (item // 100))
        elif len(str(item)) == 2:
            if item == 90:
                rim.append('XC')
            elif item == 40:
                rim.append('XL')
            else:
                rim.append('X' * (item // 10))
        else:
            if item == 9:
                rim.append('IX')
            elif item == 4:
                rim.append('IV')
            else:
                rim.append('I' * (item // 1))

    for i in range(len(rim)):
        rim[i] = rim[i].replace('CCCCC', 'D')
        rim[i] = rim[i].replace('XXXXX', 'L')
        rim[i] = rim[i].replace('IIIII', 'V')



    num_m.sort(reverse=True)
    return ''.join(rim)


def de_number_converter(number):
    num_m = []
    for item in number:
        k = []
        for i in range(len(item)):
            if item[i] == 'M':
                k.append(1000)
            elif item[i] == 'D':
                k.append(500)
            elif item[i] == 'C':
                k.append(100)
            elif item[i] == 'L':
                k.append(50)
            elif item[i] == 'X':
                k.append(10)
            elif item[i] == 'V':
                k.append(5)
            elif item[i] == 'I':
                k.append(1)

        for j in range(len(k)-1):
            if k[j] < k[j+1]:
                k[j] = k[j+1] - k[j]
                k[j+1] = 0

        num_m.append(sum(k))
    return num_m



num = int(input("Введите целое число от 1 до 9999: "))
print(number_converter(num))

numm = input("Введите римские числа через пробел: ").split()
print(de_number_converter(numm))
