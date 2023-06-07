'''
    Fazer um programa que solicite o nome de 5 alunos,
    suas respectivas notas (Etapa 1 e Etapa 2), calcule
    sua média (adotando o cálculo da média do IFRN) e 
    no final exiba os dados informados e a média de cada
    aluno.
'''

nome_aluno   = list()
nota_etapa_1 = list()
nota_etapa_2 = list()

cont_aluno = 1
while cont_aluno <= 5:

    print(f'\nDados do Aluno {cont_aluno}')
    nome = input('Informe o Nome do Aluno: ')
    nota_1 = int(input('Informe a Nota da Etapa 1: '))
    # TODO: Fazer validação de nota_1 >= 0 e <= 100
    nota_2 = int(input('Informe a Nota da Etapa 2: '))
    # TODO: Fazer validação de nota_1 >= 0 e <= 100

    nome_aluno.append(nome)
    nota_etapa_1.append(nota_1)
    nota_etapa_2.append(nota_2)

    cont_aluno += 1

# Exibindo os dados informados
print(nome_aluno)
print(nota_etapa_1)
print(nota_etapa_2)
