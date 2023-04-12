'''
    Dado que em cada disciplina semestral no IFRN o aluno obtêm notas
    em duas etapas (NE1 e NE2) e que a média parcial (MP) se dá através
    do cálculo de média ponderada (o peso da NE1 é 2 e da NE2 é 3), 
    faça um programa que solicite ao usuário as duas notas do aluno 
    e calcule a sua MP e informe a situação final do aluno 
    (APROVADO, PROVA FINAL ou REPROVADO).

    Leve em consideração as seguintes observações:
        - As notas são valores inteiros compreendidos entre 
          0 (inclusive) e 100 (inclusive);
        - Para o aluno ser aprovado a MP tem de ser igual ou 
          superior a 60;
        - Para o aluno ficar em prova final a MP tem de ser igual ou 
          superior a 20 e inferior a 60;
        - Para MP inferior a 20 o aluno está automaticamente reprovado.
'''

# Solicitando as Notas das Etapas
NE1 = int(input('Informe a nota da Etapa 1 (NE1): '))
NE2 = int(input('Informe a nota da Etapa 2 (NE2): '))

# Verificando se as notas são válidas
if (NE1>=0) and (NE1<=100) and (NE2>=0) and (NE2<=100):
    print(f'A Nota da Etapa 1 (NE1) do aluno foi {NE1}')
    print(f'A Nota da Etapa 2 (NE2) do aluno foi {NE2}')
    # Calculando a Média Parcial (MP)
    MP = (NE1*2 + NE2*3)/5
    print(f'A Média Parcial (MP) do Aluno é {MP:.0f}')
    # Verificando a Situação Parcial do Aluno
    if MP >= 60:
        print('O Aluno foi APROVADO...')
    elif MP >= 20:
        print('O Aluno está em PROVA FINAL...')
        # Solicitando a nota da Prova Final
        PF = int(input('Informe a nota da Prova Final (PF) :'))
        # Verificando se a nota é válida
        if (PF>=0) and (PF<=100):
            # Calculando as Médias
            MF1 = (MP + PF) / 2
            MF2 = (PF*2 + NE2*3) / 5
            MF3 = (NE1*2 + PF*3) / 5
            # Verificando qual a maior média
            MF = max(MF1, MF2, MF3)
            print(f'A Média Final (MF) do Aluno é {MF:.0f}')
            # Verificando a situação final do aluno
            if (MF>=60):
                print('O Aluno foi APROVADO...')
            else:
                print('O Aluno foi REPROVADO...')
        else:
            print('Nota da Prova Final é inválida...')
    else:
        print('O Aluno foi REPROVADO...')
else:
    print('Uma das notas é inválida...')
