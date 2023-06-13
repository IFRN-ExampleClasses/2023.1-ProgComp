import valores

qt_elementos = len(valores.lista)
print(f'\nA lista possui {qt_elementos} elementos')

# Percorrer cada elemento da lista e se o elemento for
# par ele deverá ser adicionado a lista_pares e se for
# ímpar ele deverá ser adicionado a lista_impares
# Usando LIST COMPREHENSION
lista_pares   = [x for x in valores.lista if x % 2 == 0]
lista_impares = [x for x in valores.lista if x % 2 != 0]

print(f'\nA lista LISTA_PARES possui {len(lista_pares)} elementos')
print(f'\nA lista LISTA_IMPARES possui {len(lista_impares)} elementos')