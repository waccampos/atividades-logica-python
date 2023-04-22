hora_trabalhada = int(input('digite a quantidade de horas trabalhadas: '))
valor_hora = int(input('digite o valor de sua hora de trabalho: '))

salario_bruto = hora_trabalhada * valor_hora
INSS = lambda x :x * 0.10
FGTS = lambda x :x * 0.11

if (salario_bruto <= 900):
    ir = 'insento'
    taxa_ir = '0%'
elif (salario_bruto <= 1500):
    ir = salario_bruto * 0.05
    taxa_ir = '5%'
elif (salario_bruto <= 2500):
    ir = salario_bruto * 0.10
    taxa_ir = '10%'
else:
    ir = salario_bruto * 0.20
    taxa_ir = '20%'
    
print('====================== CALCULADORA DE SALARIO ======================')
print('SALARIO BRUTO: (',hora_trabalhada, ' * ' , valor_hora , ')    :' ,'R$ ',salario_bruto)
print('               (-) IR (',taxa_ir,')     :R$ ', ir)
print('               (-) INSS (10%)     :R$ ', INSS(salario_bruto))    
print('               (-) FGTS (10%)     :R$ ', FGTS(salario_bruto))
if ir == "insento":
    print('Total de descontos         :R$ ', (INSS(salario_bruto)))
    print('Salario Liquido            :R$ ', (salario_bruto - INSS(salario_bruto)))
else:    
    print('Total de descontos               :R$ ', ir + (INSS(salario_bruto)))
    print('Salario Liquido                  :R$ ', (salario_bruto - (ir + INSS(salario_bruto))))
print('====================================================================')