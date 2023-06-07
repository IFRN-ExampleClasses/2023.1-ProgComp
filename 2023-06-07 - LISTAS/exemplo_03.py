'''
    Fazer um programa que preencha uma lista com os números
    primos inteiros entre 1 e 100 e em seguida gere uma 
    segunda lista com o fatorial de cada um dos elementos da
    primeira lista
'''

# ------------------------------------------------------------
# Gerando uma lista com os números primos entre 1 e 100
numeros_primos = list()
for x in range(2, 101):
    # Verificar se x é primo
    divisores = 0
    for divisor in range(1, x + 1):
        if (x % divisor == 0): divisores += 1
        if divisores > 2: break
    # Adicionando o valor de x na lista de números primos
    if divisores == 2: numeros_primos.append(x)

print('\nLista dos números primos')
print(numeros_primos)


# ------------------------------------------------------------
# Gerando uma lista com os fatoriais dos números primos
fatoriais_primos = list()
for x in numeros_primos:
    fatorial_x = 1
    for i in range(2, x + 1): fatorial_x *= i
    fatoriais_primos.append(fatorial_x)

print('\nLista dos fatoriais dos números primos')
print(fatoriais_primos)