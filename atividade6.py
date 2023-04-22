numlitros = float(input('insira o total de litros: '))
tipodecobustiveis = input('insira o tipo de combustivel: A-álcool, G-gasolina: ')
valora = numlitros * 4
valorg = numlitros * 5

if (tipodecobustiveis == 'a'):
    if(numlitros <= 20):
        valora = valora - (valora * 0.03)
        print(valora)
    else:
        valora = valora - (valora * 0.05)
        print(valora)    
        
elif (tipodecobustiveis == 'g'):
    if(numlitros <= 20):
        valorg = valorg - (valorg * 0.04)
        print(valorg)
    else:
        valorg = valorg - (valorg * 0.06)    
        print(valorg)
else:
    print('insira uma opçao valida')        