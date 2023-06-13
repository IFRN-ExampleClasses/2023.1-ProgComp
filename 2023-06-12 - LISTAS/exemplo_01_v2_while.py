import valores

qt_elementos = len(valores.lista)
print(f'\nA lista possui {qt_elementos} elementos')

lista_pares = list()
lista_impares = list()

# Percorrer cada elemento da lista e se o elemento for
# par ele deverá ser adicionado a lista_pares e se for
# ímpar ele deverá ser adicionado a lista_impares
pos = 0
while pos <= len(valores.lista):
    if (valores.lista[pos] % 2 == 0):
        lista_pares.append(valores.lista[pos])
    else:
        lista_impares.append(valores.lista[pos])
    pos += 1

print(f'\nA lista LISTA_PARES possui {len(lista_pares)} elementos')
print(f'\nA lista LISTA_IMPARES possui {len(lista_impares)} elementos')