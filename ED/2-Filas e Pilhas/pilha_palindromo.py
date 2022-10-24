from pilha import Pilha

class PilhaPalindromo(Pilha):
    ## Insire numa pilha auxiliar, o que irá colocar na ordem inversa
    def inverter(self):
        pilha_aux = Pilha()
        atual = self.topo
        while atual is not None:
            pilha_aux.push(atual.carga)
            atual = atual.prox
        return pilha_aux

    # converte palavra para lista e insere cada caractere como um nó da pilha
    # para evitar que a palavra seja inserida na ordem inversa, foi necessário usar uma pilha auxiliar
    def inserir_palavra(self, palavra):
        pilha_aux = Pilha()

        for letra in list(palavra):
            pilha_aux.push(letra)

        while pilha_aux.topo is not None:
            self.push(pilha_aux.pop().carga)

    # método que é usado quando se compara uma pilha com outra (pilha == pilha2)
    def __eq__(self, pilha):
        atual = self.topo
        atual2 = pilha.topo
        while atual is not None and atual2 is not None:
            # Caso algum dos elementos da pilha for diferente, será retornado False
            if atual.carga != atual2.carga:
                return False
            atual = atual.prox
            atual2 = atual2.prox
        return True


def checa_palindromo(palavra):
    pilha = PilhaPalindromo()
    pilha.inserir_palavra(palavra.casefold().replace(" ", "")) # Remover espaços e uppercase
    print(pilha)
    # Palavra vazia é palíndromo
    if pilha.topo == None:
        return True
    return pilha == pilha.inverter()

if checa_palindromo("socorram me subi no onibus em marrocos"):
  print("Palíndromo!")
else:
  print("Não é palíndromo!")

if checa_palindromo("ovo2"):
  print("Palíndromo!")
else:
  print("Não é palíndromo!")
