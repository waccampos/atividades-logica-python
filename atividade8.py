a = int(input('digite o avlor de a: '))
if a == 0:
    print('a equação não e do segundo grau')
else:
    b = int(input('digite o valor de b: '))
    c = int(input('digite o valor de c: '))
    
    delta = b**2 - 4 * a * c
    
    print(delta)    
    
    if (delta < 0 ):
        print('a equação não possui raizes')  
    else:
        x1 = (-b + delta ** (1/2)) / (2 * a)
        x2 = (-b - delta ** (1/2)) / (2 * a)
        if delta == 0:
            print('a equação so possui uma raiz real:')
            print(x1)
        else:
            print('a raiz 1 é:')
            print(x1)
            print('a raiz 2 é:')
            print(x2)
        