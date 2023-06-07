'''
    Fazer um programa que preencha uma lista com os números
    inteiros entre 1 e 100, em seguida exclua os números 
    divisiveis por 3
'''

# ------------------------------------------------------------
# Preenchendo a lista com os números inteiros entre 1 e 100
valores = [i for i in range(1, 101)]
print('\nLista Completa')
print(valores)

# ------------------------------------------------------------
# Eliminar os valores da lista que são divisiveis por 3
for i in valores:
    if i % 3 == 0:
        valores.remove(i)

print('\nLista após exclusão')
print(valores)


