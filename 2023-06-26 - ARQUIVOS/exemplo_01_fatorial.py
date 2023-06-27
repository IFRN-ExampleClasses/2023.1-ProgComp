arquivo = open('fatorial.txt', 'w', encoding='utf-8')
arquivo.write('inteiro;fatorial\n')
x = 1
while x <= 10:
    fatorial = 1
    for i in range(1, x+1):
        fatorial *= i
    arquivo.write(f'{x};{fatorial}\n')
    x += 1
arquivo.close()