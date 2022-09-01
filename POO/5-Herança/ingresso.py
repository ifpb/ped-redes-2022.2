class Ingresso:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def imprimirValor(self):
        print(f"R$ {self.valor:.2f}")
    
class IngressoVIP(Ingresso):
    def __init__(self, valor, adicional=0.0):
        super().__init__(valor)
        self.__adicional = adicional

    @property
    def valor(self):
        return super().valor + self.__adicional


if __name__ == '__main__':
    print("Ingresso 1: ")
    ing = Ingresso(50.00)
    ing.imprimirValor()

    print("Ingresso VIP:")
    ing2 = IngressoVIP(50.00, 10.00)
    ing2.imprimirValor()

