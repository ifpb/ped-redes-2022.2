from Carta import Carta
import random

class Baralho:
    __TIPO = 'Tradicional'
    def __init__(self):
        self.__deck = []
        self.__constroi_baralho()
    
    def __constroi_baralho(self):
        face = ['2','3','4','5','6','7','8','9','10','Valete','Dama', 'Rei', 'As'] 
        valor= [2, 3, 4, 5, 6,7,8,9,10,11,12,13,14] 
        naipe = ['Ouro','Espada','Paus','Copas']

        for i in range(len(naipe)):
            for j in range(len(face)):
                self.__deck.append(Carta(face[j],naipe[i],valor[i]))
    
    def __str__(self):
        s = ''
        for i in range(len(self.__deck)):
            s += self.__deck[i].__str__() + "\n"
        return s

    
    def tem_carta(self): # retorna True se o baralho possui cartas a serem puxadas
        if len(self.__deck) > 0:
            return True
        else:
            return False

    def puxar_carta(self)->Carta:
        return self.__deck.pop()

    def __len__(self):
        return len(self.__deck)

    def embaralhar(self):
        random.shuffle(self.__deck)
        

    def juntar_baralho(self, outroBaralho:'Baralho'):
        # O baralho 'outroBaralho' deve ficar vazio no final
        while outroBaralho.tem_carta():
            carta = outroBaralho.puxar_carta()
            self.__deck.append(carta)

    def repor_carta(self, carta: 'Carta')-> bool:
        # recebe um objeto Carta como argumento e adiciona ao baralho
        # Porém, não vai aceitar uma carta que já esteja no deck
        # retorna True se a carta foi adicionada. False, caso contrário
        if not carta in self.__deck:
            self.__deck.append(carta)
            return True
        else:
            return False

    @classmethod
    def tipo_baralho(cls):
        return Baralho.__TIPO



    






