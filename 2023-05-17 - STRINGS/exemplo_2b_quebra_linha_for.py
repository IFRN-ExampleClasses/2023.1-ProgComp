msg = input('\nInforme o texto a ser criptografado: ')

msg_quebra = ''
for letra in msg:
    if letra == ' ': letra = '\n'
    msg_quebra += letra

print(msg_quebra)