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
lstDados      = list()
while True:
    linha = arq_input.readline()[:-1]
    if not linha: break
    linha = linha.split(';')
    lstDados.append(linha)

# Fechando o arquivo de input
arq_input.close()

# Montando um conjunto (SET) contendo cada tipo de servidor
tipos = set(map(lambda t:t[0], lstDados))

# Montando uma lista com [TIPO_SERVIDOR, QUANTIDADE]
lstTipos = list()
for tipo in tipos:
    filtro = lambda f:f[0] == tipo
    lstFiltro = list(filter(filtro, lstDados))
    lstTipos.append([tipo, len(lstFiltro)])

# Escrevendo o arquivo de saída
arq_output = open(dirApp + '\\tipos_servidores.csv', 'w', encoding='utf-8')

arq_output.write('tipo_servidor;quantidade\n')

for x in lstTipos:
    arq_output.write(f'{x[0]};{x[1]}\n')

arq_output.close()
