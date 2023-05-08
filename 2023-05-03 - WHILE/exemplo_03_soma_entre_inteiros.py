'''
    Fazer um programa que solicite 2 valores inteiros positivos 
    (X e Y, assumindo que Y > X) e imprima a soma de todos os 
    inteiros entre esses valores, incluindo eles.
'''

x = int(input('Informe um valor inteiro positivo para X: '))
y = int(input('Informe um valor inteiro positivo para Y: '))

if (x > y):
    x, y = y, x

soma = 0
while x <= y:
    soma += x
    x += 1

print(f'A soma dos inteiros entre {x} e {y} é {soma}')
