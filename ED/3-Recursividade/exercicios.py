def contem_par(lista, c=0):
    if c >= len(lista):
        return False
    if lista[c] % 2 == 0:
        return True
    return contem_par(lista, c+1)

def todos_impares(lista: list):
    if len(lista) == 0:
        return True
    if lista.pop() % 2 == 0:
        return False
    return todos_impares(lista)

def max(lista, maior=None, c=0):
    if len(lista) == 0:
        return -1
    if c >= len(lista):
        return maior
    if not maior:
        maior = lista[0]
    if lista[c] > maior:
        maior = lista[c]
    return max(lista, maior, c+1)

def pos_max(lista, maior=None, maior_indice=0, c=0):
    if len(lista) == 0:
        return -1
    if c >= len(lista):
        return maior_indice
    if not maior:
        maior = lista[0]
    if lista[c] > maior:
        maior = lista[c]
        maior_indice = c
    return pos_max(lista, maior, maior_indice, c+1)

print("pos max")
print(max([1, 2, 3, 4, 100, 1, 2]))
print(pos_max([1, 2, 3, 4, 100, 1, 2]))

print("Contem par")
lista_pares = [1, 2, 3, 4, 5, 6, 10]
print(contem_par(lista_pares))
print("lista pares")
print(lista_pares)
print("Todos ímpares")
lista = [1, 2, 3, 4, 5, 6, 10]
print(todos_impares(lista))
print("lista impares")
lista_impares = [1, 1, 3, 7, 9, 11, 13]
print(todos_impares(lista_impares.copy()))
print(lista_impares)