from ast import List

def busca_binaria(chave: str, vetor: List) -> str:
  primeiro: int = 0
  ultimo: int = len(vetor)-1
  resultado = []

  while primeiro <= ultimo:
    meio = (primeiro + ultimo) // 2
    if chave.lower() == vetor[meio]['nome'].lower():
      ## Item encontrado
      resultado.append(vetor[meio]['ip'])
      vetor.pop(meio)
    elif chave.lower() < vetor[meio]['nome'].lower():
      ultimo = meio - 1
    else:
      primeiro = meio + 1
  
  return resultado

def busca_binaria_recursiva(chave: str, vetor: List, primeiro=0, ultimo=None, resultado=[]) -> str:
    
  if not ultimo:
    ultimo = len(vetor)-1

  meio = (primeiro + ultimo) // 2
  if chave.lower() == vetor[meio]['nome'].lower():
    resultado.append(vetor[meio]['ip'])
    del vetor[meio]
    return busca_binaria_recursiva(chave, vetor, primeiro, ultimo, resultado)
    
  if meio == 0 or primeiro == ultimo: 
    return resultado

  if chave.lower() < vetor[meio]['nome'].lower():
    return busca_binaria_recursiva(chave, vetor, primeiro, meio-1, resultado)
  else:
    return busca_binaria_recursiva(chave, vetor, meio+1, ultimo, resultado)