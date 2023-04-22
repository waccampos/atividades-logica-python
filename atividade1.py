respostaprofessor = list()
respostaaluno = list()
condicao = True
contadordealunos = 0
maior = 0
menor = 11
media = 0
soma = 0
nota = 0

print('------------menu professor-------------')
print('diga quais alternatiavs corretas')
for i in range(10):
    respostaprofessor.append(input(str(i+1) + 'ª) digite a letra correta (a) (b) (c) (d): '))
        
while( condicao ):
    nota = 0  
    respostaaluno = [] 
    contadordealunos = contadordealunos + 1
    print('')
    print('------------menu aluno-------------')
    for i in range(10):
        respostaaluno.append(input(str
        (i+1) + 'ª) digite a letra correta (a) (b) (c) (d): '))
# correçao    
    for i in range (10):
        if respostaaluno[i] == respostaprofessor[i]:
            nota = nota + 1 

# atulização de informaçoes pedidas            
    if (nota > maior):
        maior = nota
    if (nota < menor):
        menor = nota      
        
    soma = soma + nota      
    print('este alunoo tirou a nota', nota)   
                  
    a = input('outro aluno irá utilizar o sistema? ')
    if ( a == 'sim'):
        condicao = True      
    else:
        condicao = False   
              
media = soma / contadordealunos

print('a quantidade de alunos na sala: ', contadordealunos)
print('nota media: ' , media)
print('maior nota: ' , maior)
print('menor nota: ' , menor)