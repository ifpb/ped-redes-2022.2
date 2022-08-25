class Pais:
    def __init__(self, nome, capital, dimensao):
        self.nome = nome
        self.capital = capital
        self.dimensao = dimensao
        self.__paises_fronteira = []

    def adicionar_pais_fronteira(self, pais):
        if pais not in self.__paises_fronteira:
            self.__paises_fronteira.append(pais)

    @property
    def paises_fronteira(self):
        return self.__paises_fronteira

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def capital(self):
        return self.__capital
    
    @capital.setter
    def capital(self, capital):
        self.__capital = capital

    @property
    def dimensao(self):
        return self.__dimensao
    
    @dimensao.setter
    def dimensao(self, dimensao):
        self.__dimensao = dimensao

    def __str__(self):
        return f"Nome = {self.nome},\
 Capital = {self.capital},\
 Dimensão = {self.dimensao},\
 Países que fazem fronteira = {', '.join(self.paises_fronteira)}"

if __name__ == '__main__':
    pais = Pais("Brasil", "Brasília", 8516000)
    pais.adicionar_pais_fronteira("Argentina")
    pais.adicionar_pais_fronteira("Paraguai")
    pais.adicionar_pais_fronteira("Uruguai")
    pais.adicionar_pais_fronteira("Bolívia")
    pais.adicionar_pais_fronteira("Peru")
    pais.adicionar_pais_fronteira("Colombia")
    pais.adicionar_pais_fronteira("Guiana Francesa")
    pais.adicionar_pais_fronteira("Suriname")
    pais.adicionar_pais_fronteira("Guiana")
    pais.adicionar_pais_fronteira("Venezuela")
    print(pais)