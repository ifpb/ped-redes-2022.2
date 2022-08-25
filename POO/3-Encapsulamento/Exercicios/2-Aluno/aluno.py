from decimal import DivisionByZero
from re import T


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.__notas = []

    def media(self):
        soma = 0.0
        for nota in self.__notas:
            soma += nota

        try:
            resultado = soma / len(self.__notas)
        except DivisionByZero:
            resultado = 0

        return resultado

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def matricula(self):
        return self.__matricula % 10000

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def notas(self):
        return self.__notas

    def adicionar_nota(self, nota):
        self.__notas.append(nota)

if __name__ == '__main__':
    aluno = Aluno("Maria", 1234567)
    print(aluno.matricula)
    aluno.adicionar_nota(10)
    aluno.adicionar_nota(5)
    aluno.adicionar_nota(7)
    print(aluno.media())