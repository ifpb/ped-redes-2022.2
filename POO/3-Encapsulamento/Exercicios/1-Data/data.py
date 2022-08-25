class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"

if __name__ == '__main__':
    data = Data(20, 5, 2012)
    print(data)

    data2 = Data()
    print(data2)

    data3 = Data(12, 6)
    print(data3)

    data4 = Data(12)
    print(data4)