import re


siglas = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']

capitais = ['Maceió', 'Salvador', 'Fortaleza', 'São Luís', 'João Pessoa', 
            'Recife', 'Teresina', 'Natal', 'Aracaju']


populacao = [1018948, 2872347, 2669342, 1101884, 809015, 1695727,
             868075, 890480, 657013]
            
# Gerando uma lista onde cada elemento é uma "sub-lista"
# no formato [sigla, capital, populacao]
nordeste = list()
for p in range(len(siglas)):
    nordeste.append([siglas[p], capitais[p], populacao[p]])

print(nordeste, '\n')

# Ordenar a lista nordeste pela populacao (9-0)
nordeste.sort(key=lambda n:n[2], reverse=True)

# Exibindo os dados da lista nordeste
print('\nCapitais do Nordeste - Ordenadas Maior População')
soma_populacao = 0
for c in nordeste:
    print(f'{c[1]:>15}/{c[0]} - População: {c[2]}')
    soma_populacao += c[2]
print('-'*60)
print(f'População Total: {soma_populacao} ({len(nordeste)} Capitais)\n')

# Filtrar as capitais com população >= 1000000
filtro = lambda n:n[2] >= 1000000
nordeste_filtro = list(filter(filtro, nordeste))
#print(nordeste_filtro)

# Exibindo os dados da lista nordeste
print('\nCapitais do Nordeste - População >= 1000000')
soma_populacao = 0
for c in nordeste_filtro:
    print(f'{c[1]:>15}/{c[0]} - População: {c[2]}')
    soma_populacao += c[2]
print('-'*60)
print(f'População Total: {soma_populacao} ({len(nordeste_filtro)} Capitais)\n')
