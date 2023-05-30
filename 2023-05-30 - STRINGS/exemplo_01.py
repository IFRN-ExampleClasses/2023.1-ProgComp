# Imprime de 3 em 3 caracteres
texto = 'Instituto Federal de Educação, Ciência e Tecnologia do RN'

posInicial = 0

while posInicial <= len(texto) - 3:
    print(texto[posInicial:posInicial + 3])
    posInicial += 1