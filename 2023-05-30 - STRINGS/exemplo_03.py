variavel = 'ABCDEF'

# 6F5E4D3C2B1A
nInicial = 1
nFinal   = len(variavel)

textoFinal = ''
while nInicial <= nFinal:
    textoFinal = str(nInicial) + variavel[nInicial-1] + textoFinal
    nInicial += 1

print(textoFinal)