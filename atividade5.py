num1 = int(input('digite a base: '))
num2 = int(input('digite o expoente: '))
res = num1
i = 0

for i in range(num2-1):
    res = res * num1
print(res)    