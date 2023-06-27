import random

arquivo = open('notas.txt', 'w', encoding='utf-8')
arquivo.write('etapa1;etapa2\n')

for i in range(200):
    n1 = random.randint(0,100)
    n2 = random.randint(0,100)
    arquivo.write(f'{n1};{n2}\n')

arquivo.close()