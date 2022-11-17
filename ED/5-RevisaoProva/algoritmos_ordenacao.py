from typing import List

def selection_sort_alg(vetor: List, criterio='ip'):
    for i in range(len(vetor)):
        pos_menor = i
        menor = vetor[i]
        for j in range(i+1, len(vetor)):
            if vetor[j][criterio] < menor[criterio]:
                menor = vetor[j]
                pos_menor = j
        vetor[pos_menor] = vetor[i]
        vetor[i] = menor

def busca_binaria_recursiva(vetor: List, chave: str, primeiro=0, ultimo=None, criterio='ip') -> int:
    
  if ultimo is None:
    ultimo = len(vetor)-1

  if primeiro == ultimo:
    if vetor[primeiro][criterio] > chave:
        return primeiro
    else:
        return primeiro + 1
  if primeiro > ultimo:
    return primeiro

  meio = (primeiro + ultimo) // 2 

  if chave < vetor[meio][criterio]:
    return busca_binaria_recursiva(vetor, chave, primeiro, meio, criterio)
  elif chave > vetor[meio][criterio]:
    return busca_binaria_recursiva(vetor, chave, meio+1, ultimo, criterio)
  else:
    return meio

def insertion_sort_bin(lista: List, criterio='ip'):
    for i in range (1, len(lista)):
        chave = lista[i]
        j = i - 1
        loc = busca_binaria_recursiva(lista, chave[criterio], 0, None, criterio)
        
        # Move os elementos maiores que a chave para uma posição
        # a mais do que a atual para abrir espaço
        while j >= loc:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave

def merge(esquerda, direita, vetor, criterio='ip'):
    i,j,k = 0,0,0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i][criterio] <= direita[j][criterio]:
            vetor[k] = esquerda[i]
            i, k = i+1, k+1
        else:
            vetor[k] = direita[j]
            j,k = j+1,k+1
                    
    while i < len(esquerda):
        vetor[k] = esquerda[i]
        i, k = i+1, k+1

    while j < len(direita):
        vetor[k] = direita[j]
        j,k = j+1,k+1


def mergesort(vetor, criterio='ip'):
    if len(vetor) < 2: return vetor
    meio = len(vetor) // 2
    ## Divisão
    esquerda = vetor[:meio]
    direita = vetor[meio:]
    mergesort(esquerda, criterio)
    mergesort(direita, criterio)
    ## Combinação
    merge(esquerda, direita, vetor, criterio)


def quicksort(vetor, criterio):
    if len(vetor) <= 1: return vetor
    pivo = vetor[0]
    iguais = [x for x in vetor if x[criterio] == pivo[criterio]]
    menores = [x for x in vetor if x[criterio] < pivo[criterio]]
    maiores = [x for x in vetor if x[criterio] > pivo[criterio]]
    return quicksort(menores, criterio) + iguais + quicksort(maiores, criterio)