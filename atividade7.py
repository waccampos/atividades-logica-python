tipocarne = input("selecione o tipo da sua carne F -> para File duplo/A -> para alcatra/P -> para picanha: ")
qtd = float(input('digite a quantidade de carne que vc deseja: '))
num = 0
desconto = lambda valor: valor - (valor * 0.05)

if tipocarne == 'f':
    if qtd > 0 and qtd <= 5:
        valor = qtd * 4.90
    else:
        valor = qtd * 5.80
if tipocarne == 'a':
    if qtd > 0 and qtd <= 5:
        valor = qtd * 5.90
    else:
        valor = qtd * 6.80
if tipocarne == 'P':
    if qtd > 0 and qtd <= 5:
        valor = qtd * 6.90
    else:
        valor = qtd * 7.80
else:
    print('digite um valor valido')        
    
cartao = input('digite : c .se vc utilizara o cartao tinocoo')    

if cartao == 'c':
    print(desconto(valor))
else:
    print(valor)    