# Calcular Volume do Cilindo

raio   = float(input('Informe o raio da base: '))
altura = float(input('Informe a altura do cilindo: '))

# Só calcular o volume se o raio e a altura forem positivos 
# Caso contrário, informar se foi apenas o raio, apenas a 
# altura ou se ambos foram inválidos (<=0)
volume = 3.14 * raio ** 2 * altura 
print(f'O volume do cilindo é {volume:.2f}')
