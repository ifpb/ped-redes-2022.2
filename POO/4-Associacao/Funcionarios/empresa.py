class Empresa:
    def __init__(self, nome, cnpj, tipoComercial):
        self.nome = nome
        self.cnpj = cnpj
        self.tipoComercial = tipoComercial
        self.departamentos = []
        self.funcionarios = []
        self.__endereco = Endereco()
        self.fornecedores = []

    def __str__(self):
        nomeFuncionarios = []
        for f in self.funcionarios:
            nomeFuncionarios.append(f"Nome: {f.nome} CPF: {f.cpf}")

        return f"Nome: {self.nome}, CNPJ: {self.cnpj}, tipo: {self.tipoComercial}, endereço: {self.endereco}"
#          departamentos: {self.departamentos}\
# , funcionários: {', '.join(nomeFuncionarios)}, fornecedores = {self.fornecedores}

    @property
    def endereco(self):
        return self.__endereco

class Departamento:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

class Fornecedor:
    def __init__(self, nome, cnpj, tipo):
        self.nome = nome
        self.cnpj = cnpj
        self.tipo = tipo

    def __str__(self):
        return self.nome

class Endereco:
    def __init__(self, rua="", cidade="", estado="", pais=""):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    def __str__(self):
        return f"{self.rua}, {self.cidade}, {self.estado}, {self.pais}"

class Funcionario:
    def __init__(self, nome, cpf, cargo):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.endereco = Endereco()

    def __str__(self):
        return self.nome


if __name__ == '__main__':
    empresa = Empresa("IFPB", "10320293209-2323", "Universidade")
    funcionario1 = Funcionario("Diego", "0230232232", "Professor")
    funcionario2 = Funcionario("Marcio", "1232132332", "Coordenador")
    empresa.funcionarios.append(funcionario1)
    empresa.funcionarios.append(funcionario2)

    # empresa.endereco = Endereco("Av. Primeiro", "Cidade", "Estado, "Pais")
    empresa.endereco.rua = "Av. Primeiro de Maio"
    empresa.endereco.cidade = "João Pessoa"
    empresa.endereco.estado = "Paraíba"
    empresa.endereco.pais = "Brasil"

    depto = Departamento("Pro-reitoria de Pesquisa")
    depto2 = Departamento("Pro-reitoria de Finanças")
    depto3 = Departamento("Pro-reitoria Administrativa")
    depto4 = Departamento("Pro-reitoria de Inovação")
    empresa.departamentos.append(depto)
    empresa.departamentos.append(depto2)
    empresa.departamentos.append(depto3)
    empresa.departamentos.append(depto4)

    fornecedor = Fornecedor("Lapis e Tintas Ltda.", "102302132213", "Utensílios educacionais")
    empresa.fornecedores.append(fornecedor)

    print(empresa)
    print([str(e) for e in empresa.departamentos ])