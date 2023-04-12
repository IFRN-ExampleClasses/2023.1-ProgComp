'''
    Solicitar um número inteiro e informar se ele é par, ímpar ou nulo
'''
numero = int(input('Inform um número inteiro: '))

if numero == 0:
    print('Número = 0')
elif numero%2 == 0:
    print('Número PAR')
else:
    print('Número ÍMPAR')

print('Fim do Programa...')

