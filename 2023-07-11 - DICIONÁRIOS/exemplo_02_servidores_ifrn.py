import os

# Obtendo o diretório do programa
dirApp = os.path.abspath(__file__)
dirApp = os.path.dirname(dirApp) 

# Abrindo o arquivo de input em modo somente de leitura
arq_input = open(dirApp + '\\servidores_ifrn.csv', 'r', encoding='utf-8')

# Lendo a linha de cabecalho
lstCabecalhos = list()
lstCabecalhos.extend(arq_input.readline()[:-1].split(';'))

# Lendo as linhas de dados
dictServidores = dict()
while True:
    linha = arq_input.readline()[:-1]
    if not linha: break
    linha = linha.split(';')
    dados = dict(zip(lstCabecalhos,linha))
    dictServidores[linha[9]] = dict(dados)

# Fechando o arquivo de input
arq_input.close()

# Filtrando apenas os docentes no dicionário
dictDocentes = dict()
filtro = lambda s:s[1]['categoria'] == 'docente'
dictDocentes = dict(filter(filtro, dictServidores.items()))

# Imprimindo os dados do dicionário
for k,v in dictDocentes.items():
    print(f'Matrícula: {k}')
    print(f'Dados....: {v}\n')