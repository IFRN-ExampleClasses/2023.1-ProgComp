msg = input('\nInforme o texto a ser criptografado: ')
key = 9

msg_cripto = ''
posicao    = 0

while posicao < len(msg):
    letra_asc     = ord(msg[posicao]) + key
    letra_cripto  = chr(letra_asc)
    msg_cripto   += letra_cripto
    posicao      += 1

print(f'\n\nMensagem Original.....:\n{msg}')
print(f'\n\nMensagem Criptografada:\n{msg_cripto}\n')