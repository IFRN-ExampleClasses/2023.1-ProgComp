variavel = 'ABCDEF'

# 1A2B3C4D5E6F
nInicial = 1
nFinal   = len(variavel)

textoFinal = ''
while nInicial <= nFinal:
    textoFinal = textoFinal + str(nInicial) + variavel[nInicial-1]
    nInicial += 1

print(textoFinal)