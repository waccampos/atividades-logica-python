nota1 = float(input('digite a nota 1: '))
nota2 = float(input('digite a nota 2: '))
media = lambda nota1,nota2 : (nota1 + nota2)/2 
while nota1 < 0 or nota1 >10:
    nota1 = float(input('digite a nota 1 novamente: '))
while nota2 < 0 or nota2 >10:
    nota2 = float(input('digite a nota 2 novamente: '))
    
if media(nota1,nota2) <= 4:
    print('vc foi reprovado com a nota', media(nota1,nota2))
elif media(nota1,nota2) > 4 and media(nota1,nota2) < 7:
    print('vc esta na recuperação com a nota', media(nota1,nota2))
else:
    print('vc foi aprovado com a nota', media(nota1,nota2))