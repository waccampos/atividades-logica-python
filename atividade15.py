i = int(input('digite a sua idade'))
s = input('digite "m" para masculino e "f" para falso')
while s != "m" and s != 'f':
    s = input('digite "m" para masculino e "f" para falso')

if i <= 9:
    if s == "m":
        print('e uma criança do sexo masculino e tem ', i ,"anos") 
    else:
        print('e uma criança do sexo feminino e tem ', i ,"anos") 
else:
    if s == 'm':
        print('e um adulto do sexo masculino e tem ', i ,"anos") 
    else:
        print('e um adulto do sexo feminino e tem ', i ,"anos") 