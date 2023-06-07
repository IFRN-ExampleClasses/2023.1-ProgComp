'''
    Fazer um programa que preencha uma lista com os números
    inteiros divisiveis por 3 entre 1 e 100
'''

# ------------------------------------------------------------
# Utilizando laço de repetição
numeros_1 = list()
for i in range(1, 101):
    if (i % 3 == 0):
        numeros_1.append(i)

print('\nNUMEROS_1')
print(numeros_1)

# ------------------------------------------------------------
# Utilizando LIST COMPREHENSION
numeros_2 = [i for i in range(1, 101) if (i % 3 == 0)]

print('\nNUMEROS_2')
print(numeros_2)