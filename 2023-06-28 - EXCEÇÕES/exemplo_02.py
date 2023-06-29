import sys

preco_dolar = [199.0, 34.9, 65.99]

cambio = 4.87

preco_real = list(map(lambda x: round(x * cambio,2), preco_dolar))


print(preco_dolar)
print(preco_real)

try:
    # Forçando um índice além do tamanho máximo das listas
    print('')
    for i in range(5):
        print(f'US${preco_dolar[i]} = R$ {preco_real}')
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:
    print('\nFim do Programa...')