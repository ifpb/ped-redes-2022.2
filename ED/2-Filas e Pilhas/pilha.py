from no import No

class PilhaVaziaException(Exception):
    def __init__(self, msg):
        self.msg = msg

class Pilha:
    def __init__(self):
        self.__topo = None

    @property
    def topo(self):
        return self.__topo

    @topo.setter
    def topo(self, topo):
        self.__topo = topo

    def push(self, valor):
        novo = No(valor)
        if self.__topo is None:
            self.__topo = novo
            return
        novo.prox = self.__topo
        self.__topo = novo

    def pop(self):
        if self.__topo is None:
            raise PilhaVaziaException("Pilha vazia, não foi possível remover!")
        elemento = self.__topo
        self.__topo = self.__topo.prox
        return elemento
    
    def is_empty(self):
        return self.__topo is None

    def remover_ate_elemento(self, elemento):
        atual = self.topo
        while atual is not None and atual.carga is not elemento:
            if atual.prox is not None:
                self.topo = atual.prox
            atual = atual.prox

        ## remove o próprio elemento
        if atual is not None and atual.carga == elemento:
            self.topo = atual.prox

    ## Insere numa pilha auxiliar, o que irá colocar na ordem inversa
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

        while pilha_aux.cabeca is not None:
            self.push(pilha_aux.pop().carga)

    def __str__(self):
        return "[%s]" % (self.__topo)