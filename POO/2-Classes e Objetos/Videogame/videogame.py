from datetime import date, datetime
from utils import DateUtils
class MarcaInvalida(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class HdInvalido(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class VideoGame:

    __ULTIMO_NUMERO_SERIE = 0

    def __init__(self, data_fabricacao=None, marca="", modelo="", hd=100, garantia=2):
        if not data_fabricacao:
            data_fabricacao = datetime.today()
            self.data_fabricacao = f"{data_fabricacao.day}/{data_fabricacao.month}/{data_fabricacao.year}"
        else:
            self.data_fabricacao = data_fabricacao
        self.marca = marca
        self.modelo = modelo
        self.hd = hd
        self.anos_garantia = garantia
        self.__numero_serie = self.get_prox_numero_serie()
        self.jogos_instalados = []

    @classmethod
    def get_ultimo_num_serie(cls):
        return cls.__ULTIMO_NUMERO_SERIE
        
    @property
    def data_fabricacao(self):
        return f"{self.__data_fabricacao.day}/{self.__data_fabricacao.month}/{self.__data_fabricacao.year}"

    @data_fabricacao.setter
    def data_fabricacao(self, d):
        self.__data_fabricacao = DateUtils.converter_string_p_data(d)

    @property
    def numero_serie(self):
        return self.__numero_serie

    @property
    def anos_garantia(self):
        return self.__anos_garantia

    @anos_garantia.setter
    def anos_garantia(self, a):
        self.__anos_garantia = a

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
    
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, m):
        if m != "" and m != "Playstation" and m != "XBOX" and m != "Nintendo":
            raise MarcaInvalida("Marca não suportada: ", m)
        self.__marca = m

    @property
    def hd(self):
        return self.__hd

    @hd.setter
    def hd(self, hd):
        if (hd < 32 or hd > 1024):
            raise HdInvalido("Tamanho de Hd não suportado")
        self.__hd = hd

    def get_prox_numero_serie(self):
        self.__class__.__ULTIMO_NUMERO_SERIE += 1
        return VideoGame.__ULTIMO_NUMERO_SERIE
    
    def instalar_jogo(self, nome):
        self.__jogos_instalados.append(nome)

    def remover_jogo(self, nome):
        self.__jogos_instalados.remove(nome)

    def get_jogos_instalados(self):
        return self.__jogos_instalados

    def __str__(self):
        return f'Série: {self.__numero_serie}, Modelo: {self.__modelo}, Marca: {self.__marca},\
 Data de Fabricação: {self.__data_fabricacao.day}/{self.__data_fabricacao.month}/{self.__data_fabricacao.year}\
 HD: {self.__hd}, Anos de Garantia: {self.__anos_garantia}'
