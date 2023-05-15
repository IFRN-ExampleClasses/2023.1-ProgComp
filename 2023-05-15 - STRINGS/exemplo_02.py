var = '202310140599905;João Grilo;50;70'

var_2 = var.split(';')

print(var_2)

print(f'Matrícula: {var_2[0]}')
print(f'Nome.....: {var_2[1]}')
print(f'Etapa 1..: {var_2[2]}')
print(f'Etapa 2..: {var_2[3]}')

media = (int(var_2[2])*2 + int(var_2[3])*3)/5
print(f'Média....: {int(media)}')
