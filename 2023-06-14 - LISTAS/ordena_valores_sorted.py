import valores

print('-'*80)
print('Ordenando atraves do SORTED()')

print('\nOrdenando apenas os 50 primeiros elementos na listagem')
print(sorted(valores.lista[:50], reverse=True))
print('')

print('\nExibindo os50 primeiros elementos')
print(valores.lista[:50])
print('')

print('\nOrdenando de forma crescente todos os elementos ')
print('e armazenando em uma nova lista')
valores.lista = sorted(valores.lista)
print('')
print(valores.lista[:50])

