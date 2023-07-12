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

# Obtendo o tamanho do nome com maior quantidade de carateres
maior_nome = max(dictDocentes.values(), key=lambda x: len(x['nome']))
maior_nome = maior_nome['nome']
maior_nome = len(maior_nome)

# Obtendo o tamanho da matricula com maior quantidade de carateres
maior_matricula = max(dictDocentes.values(), key=lambda x: len(x['matricula']))
maior_matricula = maior_matricula['matricula']
maior_matricula = len(maior_matricula)

for k,v in dictDocentes.items():
    pontos_nome       = '.'*(maior_nome-len(v["nome"]))
    espacos_matricula = ' '*(maior_matricula-len(k))
    print(f'{v["nome"]}{pontos_nome} {k} {espacos_matricula}..... {v["campus"]}')
