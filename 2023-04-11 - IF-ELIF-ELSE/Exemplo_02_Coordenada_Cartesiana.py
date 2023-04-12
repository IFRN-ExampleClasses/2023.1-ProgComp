'''
    Solicitar as coordenadas de um ponto (X e Y) e informar em que 
    quadrante do plano cartesiano esse ponto se encontra.
'''

x = int(input('Informe a Coordenada X: '))
y = int(input('Informe a Coordenada Y: '))

if (x>0) and (y>0):
    print('Ponto no 1º Quadrante')
elif (x<0) and (y>0):
    print('Ponto no 2º Quadrante')
elif (x<0) and (y<0):
    print('Ponto no 3º Quadrante')
elif (x>0) and (y<0):
    print('Ponto no 4º Quadrante')
elif (x!=0) and (y==0):
    print('Ponto no Eixo X')
elif (x==0) and (y!=0):
    print('Ponto no Eixo Y')
else:
    print('Ponto na ORIGEM')

