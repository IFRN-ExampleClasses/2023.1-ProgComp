'''
    Programa para verificar se um número inteiro positivo
    é primo ou não
'''
numero = int(input("Digite um número inteiro (>0): "))

if (numero <= 0):
    print('Inform um Inteiro Positivo...')
else:
    divisor    = 1
    qt_divisor = 0
    while divisor <= numero:
        if numero % divisor == 0: qt_divisor += 1
        divisor += 1
        if (qt_divisor > 2): break
    if (qt_divisor == 2):
        print(f'\n{numero} é primo...')
    else:
        print(f'\n{numero} não é primo...')
