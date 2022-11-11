from typing import List

def selection_sort_alg(vetor: List):
    for i in range(len(vetor)):
        pos_menor = i
        menor = vetor[i]
        for j in range(i+1, len(vetor)):
            if vetor[j]['ip'] < menor['ip']:
                menor = vetor[j]
                pos_menor = j
        vetor[pos_menor] = vetor[i]
        vetor[i] = menor

def busca_binaria_recursiva(vetor: List, chave: str, primeiro=0, ultimo=None) -> int:
    
  if ultimo is None:
    ultimo = len(vetor)-1

  if primeiro == ultimo:
    if vetor[primeiro]['ip'] > chave:
        return primeiro
    else:
        return primeiro + 1
  if primeiro > ultimo:
    return primeiro

  meio = (primeiro + ultimo) // 2 

  if chave < vetor[meio]['ip']:
    return busca_binaria_recursiva(vetor, chave, primeiro, meio)
  elif chave > vetor[meio]['ip']:
    return busca_binaria_recursiva(vetor, chave, meio+1, ultimo)
  else:
    return meio

def insertion_sort_bin(lista: List):
    for i in range (1, len(lista)):
        chave = lista[i]
        j = i - 1
        loc = busca_binaria_recursiva(lista, chave['ip'])
        
        # Move os elementos maiores que a chave para uma posição
        # a mais do que a atual para abrir espaço
        while j >= loc:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave

def merge(esquerda, direita, vetor):
    i,j,k = 0,0,0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i]['ip'] <= direita[j]['ip']:
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


def mergesort(vetor):
    if len(vetor) < 2: return vetor
    meio = len(vetor) // 2
    ## Divisão
    esquerda = vetor[:meio]
    direita = vetor[meio:]
    mergesort(esquerda)
    mergesort(direita)
    ## Combinação
    merge(esquerda, direita, vetor)


def quicksort(vetor):
    if len(vetor) <= 1: return vetor
    pivo = vetor[0]['ip']
    iguais = [x for x in vetor if x['ip'] == pivo]
    menores = [x for x in vetor if x['ip'] < pivo]
    maiores = [x for x in vetor if x['ip'] > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)