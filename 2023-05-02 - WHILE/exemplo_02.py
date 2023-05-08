valor = int(input('Informe um valor inteiro positivo: '))

mult = 1

if (valor > 0):
    while (mult <= 10):
        print(f'{mult} x {valor} = {mult*valor}')
        mult += 1
else:
    print('Valor Informado Inválido...')
