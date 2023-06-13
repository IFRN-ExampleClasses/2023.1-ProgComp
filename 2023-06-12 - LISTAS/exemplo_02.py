import valores

qt_elementos = len(valores.lista)
print(f'\nA lista possui {qt_elementos} elementos')

# Solicitar um valor inteiro e informar se ele consta 
# na lista e se constar, informar quantas vezes ele aparece

valor = int(input('Digite um valor inteiro: '))

if valor in valores.lista:
    print(f'O valor {valor} está na lista...')
    ocorrencias = valores.lista.count(valor)
    print(f'O valor informado consta {ocorrencias} na lista...')
else:
    print(f'O valor {valor} não está na lista...')
