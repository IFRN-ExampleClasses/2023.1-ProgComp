import os

# Obtendo o diretório do programa
dirApp = os.path.abspath(__file__)
dirApp = os.path.dirname(dirApp) 

# Abrindo o arquivo de input em modo somente de leitura
arq_input = open(dirApp + '\\servidores_ifrn.csv', 'r', encoding='utf-8')

# Lendo a linha de cabecalho
lstCabecalhos = list()
lstCabecalhos.append(arq_input.readline()[:-1].split(';'))

# Lendo as linhas de dados
lstServidores = list()
while True:
    linha = arq_input.readline()[:-1]
    if not linha: break
    linha = linha.split(';')
    lstServidores.append(linha)

# Fechando o arquivo de input
arq_input.close()

# Mapeando as matrículas em uma lista
lstMatriculas = list(map(lambda m:m[9], lstServidores))

# Solicitando a matrícula ao usuário
matricula = input('Digite a Matrícula: ')

# Verificando se a matrícula consta na lista de matrículas
if matricula in lstMatriculas:
    pos = lstMatriculas.index(matricula)
    print(f'Nome........: {lstServidores[pos][5]}')
    print(f'Categoria...: {lstServidores[pos][0]}')
    print(f'Campus......: {lstServidores[pos][11]}')
else:
    print('Não Há Servidor Com Essa Matrícula...')