siglas = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']

capitais = ['Maceió', 'Salvador', 'Fortaleza', 'São Luís', 'João Pessoa', 
            'Recife', 'Teresina', 'Natal', 'Aracaju']


populacao = [1018948, 2872347, 2669342, 1101884, 809015, 1695727,
             868075, 890480, 657013]
            

nordeste = list()

for p in range(len(siglas)):
    nordeste.append([siglas[p], capitais[p], populacao[p]])

soma_populacao = 0
for c in nordeste:
    print(f'{c[1]:>15}/{c[0]} - População: {c[2]}')
    soma_populacao += c[2]

print('-'*60)
print(f'População Total: {soma_populacao}')