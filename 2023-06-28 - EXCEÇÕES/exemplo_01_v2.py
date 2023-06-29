import sys

try:
    d1 = int(input('Informe D1: '))
    d2 = int(input('Informe D2: '))
except ZeroDivisionError:
    print('ERRO: Impossíve dividir por Zero (D2 != 0)...')
except:
    print(f'ERRO: {sys.exc_info()[0]}')
else:
    try:
        q  = d1 / d2
    except ValueError:
        print('\nERRO: Foi informado um valor que não é inteiro...')
    except:
        print(f'\nERRO: {sys.exc_info()[0]}')
    else:
        print(f'\n{d1} / {d2} = {q:.3f}')
        print('\nDivisão calculada com sucesso...')
finally:
    print('\nFim do Programa...')