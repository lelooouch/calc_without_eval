from re import *

def f(mass):
    if len(mass) == 1:
        return mass[0]
    for i in range(len(mass)):
        if str(mass[i]) in '*$/':
            if mass[i] == '*':
                a = mass[i-1]
                b = mass[i+1]
                mass[i] = mass[i-1] * mass[i+1]
                mass.remove(a)
                mass.remove(b)
                return f(mass)
            elif mass[i] == '/':
                a = mass[i-1]
                b = mass[i+1]
                mass[i] = mass[i-1] / mass[i+1]
                mass.remove(a)
                mass.remove(b)
                return f(mass)
            elif mass[i] == '$':
                a = mass[i - 1]
                b = mass[i + 1]
                mass[i] = mass[i - 1] // mass[i + 1]
                mass.remove(a)
                mass.remove(b)
                return f(mass)

    for i in range(len(mass)):
        if str(mass[i]) in '+-':
            if mass[i] == '+':
                a = mass[i-1]
                b = mass[i+1]
                mass[i] = mass[i-1] + mass[i+1]
                mass.remove(a)
                mass.remove(b)
                return f(mass)
            else:
                a = mass[i - 1]
                b = mass[i + 1]
                mass[i] = mass[i - 1] - mass[i + 1]
                mass.remove(a)
                mass.remove(b)
                return f(mass)




a = input()
a = a.replace('//', '$')
reg = r'[0-9]+'
# 4342*893//43

num1 = []

for i in finditer(reg, a):
    num1.append(int(i.group()))

for _ in num1:
    a = a.replace(str(_), 'i')

zn = a.split('i')
ans = []
zn.pop(0)
zn.pop(-1)

for i in range(len(zn)):
    ans.append(num1[i])
    ans.append(zn[i])
ans.append(num1[-1])

print(f(ans))







