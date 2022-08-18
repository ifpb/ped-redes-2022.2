from datetime import date, datetime

class VideoGame:

    ultimo_numero_serie = 0

    def __init__(self, data_fabricacao=date.today(), marca="", modelo="", hd=100, garantia=2):
        self.data_fabricacao = data_fabricacao
        self.marca = marca
        self.modelo = modelo
        self.hd = hd
        self.anos_garantia = garantia
        self.numero_serie = self.get_prox_numero_serie()
        self.__jogos_instalados = []

    def get_prox_numero_serie(self):
        self.__class__.ultimo_numero_serie += 1
        return VideoGame.ultimo_numero_serie
    
    def instalar_jogo(self, nome):
        self.__jogos_instalados.append(nome)

    def remover_jogo(self, nome):
        self.__jogos_instalados.remove(nome)

    def get_jogos_instalados(self):
        return self.__jogos_instalados

    def __str__(self):
        return f'Série: {self.numero_serie}, Modelo: {self.modelo}, Marca: {self.marca},\
 Data de Fabricação: {self.data_fabricacao.day}/{self.data_fabricacao.month}/{self.data_fabricacao.year}\
 HD: {self.hd}, Anos de Garantia: {self.anos_garantia}'
