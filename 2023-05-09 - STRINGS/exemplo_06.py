combustivel = 'Gasolina'
valor_litro = '5,69'.replace(',', '.')

tanque = 40

valor_tanque = tanque * float(valor_litro)

print(f'{valor_tanque:.2f}')
