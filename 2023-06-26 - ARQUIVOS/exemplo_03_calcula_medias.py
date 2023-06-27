
arquivo = open('notas.txt', 'r', encoding='utf-8')
arq_medias = open('medias.txt', 'w', encoding='utf=-8')

cabecalho = arquivo.readline()[:-1]
arq_medias.write(f'{cabecalho};media_final\n')

while True:
    linha = arquivo.readline()[:-1]
    if not linha: break
    linha = linha.split(';')
    media = int(round((int(linha[0])*2+int(linha[1])*3)/5, 0))
    arq_medias.write(f'{linha[0]};{linha[1]};{media}\n')

arquivo.close()
arq_medias.close()