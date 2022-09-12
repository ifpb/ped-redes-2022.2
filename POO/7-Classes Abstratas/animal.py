from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, nome) -> None:
        super().__init__()
        self.nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @abstractmethod
    def atacar(self):
        pass

    def __str__(self) -> str:
        return f"Nome: {self.nome}"

class Gato(Animal):

    def __init__(self, nome) -> None:
        super().__init__(nome)

    def atacar(self):
        print(f"{self.nome} arranha!")

class Cachorro(Animal):

    def __init__(self, nome) -> None:
        super().__init__(nome)

    def atacar(self):
        print(f"{self.nome} Morde!")

g = Gato("Katy")
g.atacar()
print(g)

c = Cachorro("Rex")
c.atacar()
print(c)