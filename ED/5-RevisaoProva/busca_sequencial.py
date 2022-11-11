from ast import List

def busca_sequencial(chave_pesquisa: str, vetor: List):
  for i in range(len(vetor)):
    if chave_pesquisa == vetor[i]['ip']:
      return vetor[i]['nome']
    if vetor[i]['ip'] > chave_pesquisa:
      return -1
  return -1

def busca_sequencial_recursiva(chave: str, vetor: List, i: int = 0):
  if i >= len(vetor) or vetor[i]['ip'] > chave:
    return -1
  if chave == vetor[i]['ip']:
    return vetor[i]['nome']
  return busca_sequencial_recursiva(chave, vetor, i+1) 