'''
    Calculando o valor de PI utlizando a Série de Nilakantha

    PI = 3 + (4/2*3*4) - (4/4*5*6) + (4/6*7*8) - (4/8*9*10) ...
'''

# Solicitando a quantidade de casas decimais
casas_dec = int(input('Informe a quantidade de casas decimais (>0): '))

# Valor inicial de PI
pi = 3

if casas_dec < 0:
    print('Informe um valor inteiro positivo...')
else:
    posicao_dec = 1
    while posicao_dec <= casas_dec:
        decimal = 4 / ((2*posicao_dec) * (2*posicao_dec+1) * (2*posicao_dec+2))
        if (posicao_dec%2 == 0): decimal *= -1
        pi += decimal
        posicao_dec += 1

print(pi)