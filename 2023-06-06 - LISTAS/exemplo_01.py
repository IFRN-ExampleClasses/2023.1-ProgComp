'''
    Fazer um programa que preencha uma lista com 
    números inteiros entre 1 e 100
'''

# ------------------------------------------------------------
# Utilizando laço de repetição
numeros_1 = list()
for i in range(1, 101):
    numeros_1.append(i)

print('\nNUMEROS_1')
print(numeros_1)

# ------------------------------------------------------------
# Utilizando LIST COMPREHENSION
numeros_2 = [i for i in range(1, 101)]

print('\nNUMEROS_2')
print(numeros_2)