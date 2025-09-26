from re import *

a = input()
a = a.replace('//', '$')
reg = r'[0-9]+'
reg2 = r'[*|+|$|/|-]'
# 132-4342*893//43
num = []
num2 = []
for i in finditer(reg, a):
    num.append(i.group())
for j in finditer(reg2, a):
    num2.append(j.group())


