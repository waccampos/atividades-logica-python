num = 0
inicio = 0
final = 0

num = int(input('diga qual e o numero que você quer fazer a tabuada: '))
inicio = int(input('diga o numero do inicio do intervalo : '))
final = int(input('diga o numero do final do intervalo : '))

for i  in range(inicio,final+1):
    print (num * i)