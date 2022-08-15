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
        self.jogos_instalados = []

    def get_prox_numero_serie(self):
        VideoGame.ultimo_numero_serie += 1
        return VideoGame.ultimo_numero_serie
    
    def instalar_jogo(self, nome):
        self.jogos_instalados.append(nome)

    def get_jogos_instalados(self):
        return self.jogos_instalados

    def __str__(self):
        return f'Série: {self.numero_serie}, Modelo: {self.modelo}, Marca: {self.marca},\
 Data de Fabricação: {self.data_fabricacao.day}/{self.data_fabricacao.month}/{self.data_fabricacao.year}\
 HD: {self.hd}, Anos de Garantia: {self.anos_garantia}'


xbox = VideoGame(datetime.strptime("05/02/2022", "%d/%m/%Y"), "XBOX", "360")
xbox.instalar_jogo("FIFA 2022")
xbox.instalar_jogo("PES 2022")
print(xbox)
print(xbox.get_jogos_instalados())

ps4 = VideoGame()
ps4.marca = "Playstation"
ps4.modelo = "4 Slim"
print(ps4)