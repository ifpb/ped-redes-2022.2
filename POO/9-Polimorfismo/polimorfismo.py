class Pessoa:
    def __init__(self, nome, endereco, telefone) -> None:
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, telefone, valorCredito, valorDivida) -> None:
        super().__init__(nome, endereco, telefone)
        self.__valorCredito = valorCredito
        self.__valorDivida = valorDivida

    @property
    def valorCredito(self):
        return self.__valorCredito

    @valorCredito.setter
    def valorCredito(self, valorCredito):
        self.__valorCredito = valorCredito

    @property
    def valorDivida(self):
        return self.__valorDivida

    @valorDivida.setter
    def valorDivida(self, valorDivida):
        self.__valorDivida = valorDivida

    def obterSaldo(self):
        return self.valorDivida - self.valorCredito

    
class Empregado(Pessoa):
    def __init__(self, nome, endereco, telefone, codigoSetor, salarioBase, imposto) -> None:
        super().__init__(nome, endereco, telefone, imposto)
        self.__codigoSetor = codigoSetor
        self.__salarioBase = salarioBase
        self.__imposto = imposto

    @property
    def codigoSetor(self):
        return self.__codigoSetor

    @codigoSetor.setter
    def codigoSetor(self, codigoSetor):
        self.__codigoSetor = codigoSetor

    @property
    def salarioBase(self):
        return self.__salarioBase

    @salarioBase.setter
    def salarioBase(self, salarioBase):
        self.__salarioBase = salarioBase

    @property
    def imposto(self):
        return self.__imposto

    @imposto.setter
    def imposto(self, imposto):
        self.__imposto = imposto
    
    def calcularSalario(self):
        return self.salarioBase - (self.salarioBase - self.imposto)

class Operario(Empregado):
    def __init__(self, nome, endereco, telefone, codigoSetor, salarioBase, imposto, valorProducao, comissao) -> None:
        super().__init__(nome, endereco, telefone, codigoSetor, salarioBase, imposto)
        self.__valorProducao = valorProducao
        self.__comissao = comissao

    @property
    def valorProducao(self):
        return self.__valorProducao

    @property.setter
    def valorProducao(self, valorProducao):
        self.__valorProducao = valorProducao

    @property
    def comissao(self):
        return self.__comissao

    @property.setter
    def comissao(self, comissao):
        self.__comissao = comissao
    
    def calcularSalario(self):
        return super().calcularSalario() + self.comissao + self.valorProducao

class Vendedor(Empregado):
    def __init__(self, nome, endereco, telefone, codigoSetor, salarioBase, imposto, comissao) -> None:
        super().__init__(nome, endereco, telefone, codigoSetor, salarioBase, imposto, comissao)

    @property
    def comissao(self):
        return self.__comissao

    @property.setter
    def comissao(self, comissao):
        self.__comissao = comissao
        
    def calcularSalario(self):
        return super().calcularSalario() + self.comissao