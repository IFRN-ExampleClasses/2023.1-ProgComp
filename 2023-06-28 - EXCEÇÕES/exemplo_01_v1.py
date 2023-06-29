import sys

try:
    d1 = int(input('Informe D1: '))
    d2 = int(input('Informe D2: '))
    q  = d1 / d2
    print(f'\n{d1} / {d2} = {q:.3f}')
except ValueError:
    print('\nERRO: Foi informado um valor que não é inteiro...')
except ZeroDivisionError:
    print('\nERRO: Impossíve dividir por Zero (D2 != 0)...')
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
else:
    print('\nDivisão calculada com sucesso...')
finally:
    print('\nFim do Programa...')