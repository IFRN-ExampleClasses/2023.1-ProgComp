'''
    Fazer um programa que preencha uma lista com os números
    inteiros divisiveis por 3 entre 1 e 100, em seguida
    solicite um valor inteiro e diga se ele está na lista
    ou não e se existir, informar qual sua posição na lista
'''

# ------------------------------------------------------------
# Preenchendo a lista com os números divisiveis 
# por 3 entre 1 e 100
valores = [i for i in range(1, 101) if (i % 3 == 0)]
print(valores)

# ------------------------------------------------------------
# Solicitando um valor valor inteiro
numero = int(input('\nDigite um número... '))

# ------------------------------------------------------------
# Verificando se o valor digitado consta na lista
if numero in valores:
    posicao = valores.index(numero)
    print(f'\nO valor {numero} está na lista na posição {posicao}...')
else:
    print(f'\nO valor {numero} não está na lista...')
