# Solicitar o ano de nascimento e calcular sua idade

ano_nascimento = int(input('Informe o seu ano de nascimento: '))

# Só calcular e exibir a idade caso o ano de nascimento seja
# no máximo 2023
if (ano_nascimento <= 2023) and (ano_nascimento >= 1900):
    idade = 2023 - ano_nascimento
    print(f'Você tem {idade} anos')
    # Considerando que a pessoa maior de idade tem no minimo
    # 18 anos, informe se a pessoa é maior de idade ou não
    if idade >= 18:
        print('Maior de Idade...')
    else:
        print('Menor de Idade...')
else:
    print('Só aceita anos entre 1900 e 2023...')
