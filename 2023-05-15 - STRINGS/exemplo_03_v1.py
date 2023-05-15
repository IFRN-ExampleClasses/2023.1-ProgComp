var = '202310140599905;João Grilo;50;70#202310140599906;Chicó;80;30'

print(var)
print('')

var_2 = var.split('#')
print(var_2)
print('')

var_2[0] = var_2[0].split(';')
var_2[1] = var_2[1].split(';')
print(var_2)
