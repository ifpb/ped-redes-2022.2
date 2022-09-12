from abc import ABC, abstractmethod
from enum import Enum

class GrauInstrucao(Enum):
    ENSINO_MEDIO = "Ensino Médio"
    ENSINO_SUPERIOR = "Ensino Superior"
    MESTRE = "Mestre"
    DOUTOR = "Doutor"
    ESPECIALISTA = "Especialista"
    def __str__(self):
        return self.value

class Funcionario(ABC):
    def __init__(self, nome, salario_base, grau_instrucao):
        self.nome = nome
        self.salario_base = salario_base
        self.grau_instrucao = grau_instrucao
        self._bonificacao = 0.0
        self.add_bonificacao()

    def contracheque(self):
        return self.salario_base + self._bonificacao

    @abstractmethod
    def add_bonificacao(self):
        pass

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario):
        assert type(salario) == int or type(salario) == float, "Salário deve ser numérico"
        assert salario > 0, "Salário do funcionário precisa ser maior do que 0"
        self.__salario_base = salario

    @property
    def grau_instrucao(self):
        return self.__grau_instrucao

    @grau_instrucao.setter
    def grau_instrucao(self, grau_instrucao):
        assert type(grau_instrucao) == GrauInstrucao, "Grau de instrução deve ser do tipo enum GrauInstrucao"
        self.__grau_instrucao = grau_instrucao
    
    @property
    def bonificacao(self):
        return self._bonificacao

    def __str__(self):
        return "Sou um objeto da class %s, me chamo %s e ganho %4.2f" % (type(self).__name__, self.__nome, self.contracheque())

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, grau_instrucao):
        super().__init__(nome, salario_base, grau_instrucao)
    
    def add_bonificacao(self):
        if (self.grau_instrucao == GrauInstrucao.DOUTOR):
            self._bonificacao += self.salario_base * 0.5
        elif (self.grau_instrucao == GrauInstrucao.MESTRE):
            self._bonificacao += self.salario_base * 0.25
        elif (self.grau_instrucao == GrauInstrucao.ESPECIALISTA):
            self._bonificacao += self.salario_base * 0.15
    

class Presidente(Funcionario):
    def __init__(self, nome, salario_base, grau_instrucao):
        super().__init__(nome, salario_base, grau_instrucao)

    def add_bonificacao(self):
        if (self.grau_instrucao == GrauInstrucao.DOUTOR):
            self._bonificacao = (self.salario_base * 5) - self.salario_base
        else:
            self._bonificacao = (self.salario_base * 3) - self.salario_base

class Diretor(Gerente):
    def __init__(self, nome, salario_base, grau_instrucao):
        super().__init__(nome, salario_base, grau_instrucao)

    def add_bonificacao(self):
        super().add_bonificacao()
        self._bonificacao += self.salario_base * 0.3