'''
    Programa para calcular os divisores de um número 
    inteiro positivo
'''
numero = int(input("Digite um número inteiro (>0): "))

if (numero <= 0):
    print('Inform um Inteiro Positivo...')
else:
    print(f'Divisores de {numero}: ', end='')
    divisor = 1
    while divisor <= numero:
        if numero % divisor == 0: print(divisor, end=', ')
        divisor += 1
