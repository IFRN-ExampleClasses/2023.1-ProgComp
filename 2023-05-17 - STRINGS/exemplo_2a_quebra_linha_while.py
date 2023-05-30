msg = input('\nInforme o texto a ser criptografado: ')

posicao = 0
msg_quebra = ''
while posicao < len(msg):
    letra = msg[posicao]
    if letra == ' ': letra = '\n'
    msg_quebra += letra
    posicao += 1

print(msg_quebra)