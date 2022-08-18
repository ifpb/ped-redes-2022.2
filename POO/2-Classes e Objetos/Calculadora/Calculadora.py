import sys

class SomaMuitoAlta(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Calculadora:
    # ----------- Construtor ------------ #
    def __init__(self, registrador: float = 0.0):
        self.__registrador = registrador
        self.__historico = self.__registrador

    # ------------ Destrutor ------------ #
    def __del__(self):
        print(f'Objeto com endereço de memória {hex(id(self))} deletado.',
              file=sys.stderr)

    # ------------- Getters ------------- #
    @property
    def registrador(self):
        return self.__registrador

    # ---------- Magic Methods ---------- #
    def __str__(self):
        return f"Total: {self.__registrador}"

    # ------ Funções da Calculadora ----- #
    def adicionar(self, valor: float):
        if valor > 1000:
            raise SomaMuitoAlta("Soma alta demais")
        self.__definir_historico()
        self.__registrador += valor

    def subtrair(self, valor: float):
        self.__definir_historico()
        self.__registrador -= valor

    def dividir(self, valor: float):
        self.__definir_historico()
        try:
          self.__registrador /= valor
        except ZeroDivisionError:
          self.__registrador = 0.0

    def multiplicar(self, valor: float):
        self.__definir_historico()
        self.__registrador *= valor

    def exibir(self):
        print(self.__registrador)

    def resetar(self):
        self.__definir_historico()
        self.__registrador = 0.0

    def desfazer(self):
        self.__registrador, self.__historico = self.__historico, self.__registrador

    # ------- Métodos Auxiliares -------- #
    def __definir_historico(self):
        self.__historico = self.__registrador





