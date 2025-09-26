from re import *

a = input()
a = a.replace('//', '$')
reg = r'[0-9]+'
reg2 = r'[*|+|$|/|-]'
# 132-4342*893//43
num1 = []
num_1 = []
num2 = []
num_2 = []

for i in finditer(reg, a):
    num1.append(int(i.group()))
    num_1.append(int(i.group()))


'''
for j in finditer(reg2, a):
    num2.append(j.group())
    num_2.append(j.group())
'''


first = []
#for i in range(len(num2)):
i = 0
while '*' not in num2 or '$' not in num2 or '/' not in num2:
    if num2[i] in '*/$':
        if num2[i] == '*':
            num1[i] = num1[i] * num1[i+1]
            num1.remove(num1[i+1])
            #num2.remove(num2[i])
            i += 1
        elif num2[i] == '/':
            num_1[i] = num1[i] / num1[i + 1]
            num_1.remove(num1[i + 1])
            num2.remove(num2[i])
            i += 1
        elif num2[i] == '$':
            print(i, num1)
            num_1[i] = num1[i] // num1[i + 1]
            print(i, num1)
            num_1.remove(num1[i + 1])
            num2.remove(num2[i])
            i += 1


print(first)






