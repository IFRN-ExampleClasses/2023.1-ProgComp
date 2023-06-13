import random

lista = list()

# Usando FOR
for i in range(10000):
    lista.append(random.randint(100, 100000))

# Usando WHILE
contador = 1
while contador <= 10000:
    lista.append(random.randint(100, 100000))
    contador += 1

# Usando LC
lista = [random.randint(100,100000) for _ in range(10000)]