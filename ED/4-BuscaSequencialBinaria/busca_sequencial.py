from ast import List

def busca_sequencial(chave_pesquisa: str, vetor: List):
  resultado = []
  for i in range(len(vetor)):
    if chave_pesquisa.lower() in vetor[i]['nome'].lower():
      resultado.append(vetor[i]['ip'])
    elif vetor[i]['nome'].lower() > chave_pesquisa.lower():
      return resultado
  return resultado

def busca_sequencial_recursiva(chave: str, vetor: List, i: int = 0, resultado=[]):
  if i >= len(vetor) or (chave.lower() not in vetor[i]['nome'].lower() and vetor[i]['nome'].lower() > chave.lower()):
    return resultado
  if chave.lower() in vetor[i]['nome'].lower():
    resultado.append(vetor[i]['ip'])
  return busca_sequencial_recursiva(chave, vetor, i+1, resultado) 