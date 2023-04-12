'''
    Solicitar 3 valores inteiros e informar o maior deles.
'''
x = int(input('Informe um valor para X: '))
y = int(input('Informe um valor para Y: '))
z = int(input('Informe um valor para Z: '))

# Modo Clássico
maior = x
if (y > maior): maior = y
if (z > maior): maior = z
print(f'O maior número é {maior}')

# Modo Pythônico
maior = max(x,y,z)
print(f'O maior número é {maior}')
