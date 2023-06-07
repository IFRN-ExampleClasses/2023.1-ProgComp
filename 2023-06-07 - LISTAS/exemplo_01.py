'''
    Fazer um programa que preencha uma lista com os números
    inteiros entre 1 e 100, em seguida exclua os números 
    divisiveis por 3 mas os guarde em uma outra lista
'''

# ------------------------------------------------------------
# Preenchendo a lista com os números inteiros entre 1 e 100
valores = [i for i in range(1, 101)]
print('\nLista Completa')
print(valores)

# ------------------------------------------------------------
# Eliminar os valores da lista que são divisiveis por 3 e 
# guardá-los em outra lista
excluidos = list()
for i in valores:
    # Obtendo a posição (index) do valor na lista
    posicao = valores.index(i)
    # Verifica se é divisivel por 3
    if i % 3 == 0:
        # Exclui o valor e guarda ele em uma variavel
        valorExcluido = valores.pop(posicao)
        # Adiciona o valor excluido em uma outra lista
        excluidos.append(valorExcluido)

print('\nLista após exclusão')
print(valores)

print('\nLista valores excluidos')
print(excluidos)
