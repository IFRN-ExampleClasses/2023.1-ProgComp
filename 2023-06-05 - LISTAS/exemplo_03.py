'''
    Fazer um programa que solicite um valor inteiro positivo
    e salve em uma lista os números divisiveis por 3 compreendidos
    entre 0 e o número informado
'''

div_3 = list()

limite = int(input('Informe um valor Inteiro Positivo: '))

if limite > 0:
    for valor in range(1, limite+1):
        if (valor % 3 == 0):
            div_3.append(valor)
    print(div_3)
else:
    print('Valor Informado Inválido...')