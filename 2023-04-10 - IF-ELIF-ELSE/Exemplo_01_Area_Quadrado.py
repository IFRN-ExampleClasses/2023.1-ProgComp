# Calcular Área do Quadrado
lado = float(input('Informe o lado do quadrado: '))

if lado > 0:
    area = lado ** 2
    print(f'A área do quadrado de lado {lado:.2f} é {area:.2f}')
else:
    print('Informe um valor positivo... (lado > 0) ')
