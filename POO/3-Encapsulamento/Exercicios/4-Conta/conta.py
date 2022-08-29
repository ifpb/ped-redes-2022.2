class ContaCorrente:
    def __init__(self, numero, titular, saldo=0.0):
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = titular

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        return False
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular
    
    def __del__(self):
        print(f"Conta numero {self.numero} removida da memória!")

    def __str__(self):
        return f"Número da conta: {self.numero}, Nome do titular: {self.titular}, Saldo: R$ {self.saldo:.2f}"

if __name__ == '__main__':
    
    contas = []

    for i in range(2):
        numero = input(f"Digite o número da conta {i+1}: ")
        titular = input(f"Digite o nome do titular da conta {i+1}: ")
        conta = ContaCorrente(numero, titular)
        contas.append(conta)

    while(True):

        print("Seja bem-vindo. Opções disponíveis: ")
        print("1-Depositar")
        print("2-Sacar")
        print("3-Saldo")
        print("4-Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            for i, conta in enumerate(contas):
                print(f"{i+1} - {conta.numero}")
            conta_selecionada = int(input("Qual conta deseja usar?"))-1
            try:
                conta = contas[conta_selecionada]
                valor_deposito = float(input("Quanto deseja depositar? "))
                conta.depositar(valor_deposito)
            except:
                print("Conta inválida!")

        elif opcao == 2:
            for i, conta in enumerate(contas):
                print(f"{i+1} - {conta.numero}")
            conta_selecionada = int(input("Qual conta deseja usar?"))-1
            try:
                conta = contas[conta_selecionada]
                valor = float(input("Quanto deseja sacar? "))
                resultado = conta.sacar(valor)
                if resultado:
                    print(f"Seu novo saldo é R$ {conta.saldo:.2f}")
                else:
                    print("Saldo insuficiente!")
            except:
                print("Conta inválida!")

        elif opcao == 3:
            for i, conta in enumerate(contas):
                print(f"{i+1} - {conta.numero}")
            conta_selecionada = int(input("Qual conta deseja usar?"))-1
            try:
                conta = contas[conta_selecionada]
                print(f"Seu saldo é R$ {conta.saldo:.2f}")
            except:
                print("Conta inválida!")

        elif opcao == 4:
            break

        else:
            print("Opção inválida!")

        print("\n")