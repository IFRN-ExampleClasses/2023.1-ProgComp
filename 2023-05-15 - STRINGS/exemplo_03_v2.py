var = '202310140599905;João Grilo;50;70#202310140599906;Chicó;80;30'

print(var)
print('')

var_2 = var.split('#')
print(var_2)
print('')

indice = 0
while indice < len(var_2):
    var_2[indice] = var_2[indice].split(';')
    indice += 1    

print(var_2)
print('')

print(var_2[0])
print('')

indice = 0
while indice < len(var_2):
    print(f'Matrícula: {var_2[indice][0]}')
    print(f'Nome.....: {var_2[indice][1]}')
    print(f'Etapa 1..: {var_2[indice][2]}')
    print(f'Etapa 2..: {var_2[indice][3]}')
    
    media = (int(var_2[indice][2])*2 + int(var_2[indice][3])*3)/5
    print(f'Média....: {int(media)}')
    print('')
    indice += 1

