num = []
maiornum = 0

for i in range(0,3):
    num.append(int(input('digite um num:')))
for i in num:
    if i > maiornum:
        maiornum = i
print(' o maior numero e :')
print(maiornum)   