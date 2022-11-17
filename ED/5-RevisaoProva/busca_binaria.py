from ast import List

def busca_binaria(chave: str, vetor: List) -> str:
  primeiro: int = 0
  ultimo: int = len(vetor)-1

  while primeiro <= ultimo:
    meio = (primeiro + ultimo) // 2
    if chave == vetor[meio]['ip']:
      ## Item encontrado
      return vetor[meio]['nome']
    elif chave < vetor[meio]['ip']:
      ultimo = meio - 1
    else:
      primeiro = meio + 1
  
  return -1

def busca_binaria_recursiva(chave: str, vetor: List, primeiro=0, ultimo=None) -> str:
    
  if not ultimo:
    ultimo = len(vetor)-1

  meio = (primeiro + ultimo) // 2
  if chave == vetor[meio]['ip']:
    return vetor[meio]['nome']

  if meio == 0 or primeiro == ultimo: 
    return -1

  if chave < vetor[meio]['ip']:
    return busca_binaria_recursiva(chave, vetor, primeiro, meio-1)
  else:
    return busca_binaria_recursiva(chave, vetor, meio+1, ultimo)