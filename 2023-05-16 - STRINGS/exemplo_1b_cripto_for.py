msg = input('\nInforme o texto a ser criptografado: ')
key = 9

msg_cripto = ''

for letra in msg:
    letra_asc     = ord(letra) + key
    letra_cripto  = chr(letra_asc)
    msg_cripto   += letra_cripto

print(f'\n\nMensagem Original.....:\n{msg}')
print(f'\n\nMensagem Criptografada:\n{msg_cripto}\n')