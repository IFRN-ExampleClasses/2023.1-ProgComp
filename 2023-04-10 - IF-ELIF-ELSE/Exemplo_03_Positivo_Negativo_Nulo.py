# Solicitar um número inteiro e dizer se ele é positivo, 
# negativo ou nulo;

numero = int(input('Informe um valor inteiro: '))

# Modo Pythônico
if numero > 0:
    print('Número POSITIVO...')
elif numero < 0:
    print('Número NEGATIVO...')
else:
    print('Número NULO...')

# Modo Clássico
'''
if numero > 0:
    print('Número POSITIVO...')
else:
    if  numero < 0:
        print('Número NEGATIVO...')
    else:
        print('Número NULO...')
'''