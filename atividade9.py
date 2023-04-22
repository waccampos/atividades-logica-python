dia = int(input('digite o o num do dia da semana: '))

while (dia < 1 or dia > 7):
    dia = int(input("valor invalido, digite novamente: ")) 
    
if dia == 1:
    print("domingo")
elif dia == 2:
    print("segunda")     
elif dia == 3:
    print("terça")     
elif dia == 4:
    print("quarta")     
elif dia == 5:
    print("quinta")     
elif dia == 6:
    print("sexta")     
elif dia == 7:
    print("sabado")     

        
