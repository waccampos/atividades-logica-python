nums = list()
pares = 0
impares = 0 

for i in range(10):
    nums.append(int(input('digite um num')))

for i in (nums):
    if (i%2 == 0):
        pares = pares+ 1
    else:
        impares = impares + 1     

   
print('dentre os numeros digitados existe: ' + str(pares)+' numeros pares')
print('dentre os numeros digitados existe: ' + str(impares)+' numeros impares')         