from abc import ABC, abstractmethod

class Pessoa(ABC):
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

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, telefone, valorCredito, valorDivida) -> None:
        super().__init__(nome, endereco, telefone)
        self.valorCredito = valorCredito
        self.valorDivida = valorDivida

    @property
    def valorCredito(self):
        return self.__valorCredito

    @valorCredito.setter
    def valorCredito(self, valorCredito):
        assert type(valorCredito) == int or type(valorCredito) == float, "valorCredito deve ser um número"
        self.__valorCredito = valorCredito

    @property
    def valorDivida(self):
        return self.__valorDivida

    @valorDivida.setter
    def valorDivida(self, valorDivida):
        assert type(valorDivida) == int or type(valorDivida) == float, "valorDivida deve ser um número"
        self.__valorDivida = valorDivida

    def obterSaldo(self):
        return self.valorCredito - self.valorDivida

class Empregado(Pessoa):
    def __init__(self, nome, endereco, telefone, codigoSetor, salarioBase, imposto, comissao) -> None:
        super().__init__(nome, endereco, telefone)
        self.codigoSetor = codigoSetor
        self.salarioBase = salarioBase
        self.imposto = imposto
        self.comissao = comissao

    @property
    def codigoSetor(self):
        return self.__codigoSetor

    @codigoSetor.setter
    def codigoSetor(self, codigoSetor):
        assert type(codigoSetor) == int, "codigoSetor deve ser um inteiro"
        self.__codigoSetor = codigoSetor

    @property
    def salarioBase(self):
        return self.__salarioBase

    @salarioBase.setter
    def salarioBase(self, salarioBase):
        assert type(salarioBase) == int or type(salarioBase) == float, "salarioBase deve ser um número"
        self.__salarioBase = salarioBase

    @property
    def imposto(self):
        return self.__imposto

    @imposto.setter
    def imposto(self, imposto):
        assert type(imposto) == float and imposto >=0 and imposto <= 1, "imposto deve ser um float entre 0 e 1"
        self.__imposto = imposto

    @property
    def comissao(self):
        return self.__comissao

    @comissao.setter
    def comissao(self, comissao):
        assert type(comissao) == float, "comissao deve ser um float entre 0 e 1"
        self.__comissao = comissao
    
    @abstractmethod
    def calcularSalario(self):
        return self.salarioBase - (self.salarioBase * self.imposto)

class Operario(Empregado):
    def __init__(self, nome, endereco, telefone, codigoSetor, salarioBase, imposto, comissao, valorProducao) -> None:
        super().__init__(nome, endereco, telefone, codigoSetor, salarioBase, imposto, comissao)
        self.valorProducao = valorProducao

    @property
    def valorProducao(self):
        return self.__valorProducao

    @valorProducao.setter
    def valorProducao(self, valorProducao):
        self.__valorProducao = valorProducao

    def calcularSalario(self):
        return super().calcularSalario() + (self.comissao * self.valorProducao)

class Vendedor(Empregado):
    def __init__(self, nome, endereco, telefone, codigoSetor, salarioBase, imposto, comissao, valorVendas) -> None:
        super().__init__(nome, endereco, telefone, codigoSetor, salarioBase, imposto, comissao)
        self.valorVendas = valorVendas

    @property
    def valorVendas(self):
        return self.__valorVendas

    @valorVendas.setter
    def valorVendas(self, valorVendas):
        assert type(valorVendas) == int or type(valorVendas) == float, "valorVendas deve ser um número"
        self.__valorVendas = valorVendas
        
    def calcularSalario(self):
        return super().calcularSalario() + (self.comissao * self.valorVendas)

if __name__ == '__main__':
    f = Fornecedor("Coca cola", "Los Angeles US", "12012131", 20000, 5000)
    print("Fornecedor =", f.nome)
    print("Saldo =", f.obterSaldo())

    o = Operario("Joao", "Rua boa", "998238283", 1, 900.00, 0.2, 0.2, 2000)
    v = Vendedor("Joao", "Rua boa", "998238283", 1, 1500.00, 0.2, 0.5, 3000.00)
    for p in [o, v]:
        print(f"Salário do {p.__class__.__name__} = { p.calcularSalario():.2f}")