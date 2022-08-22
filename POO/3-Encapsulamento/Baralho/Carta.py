class Carta:
    def __init__(self, face, naipe, valor):
        self.__face = face
        self.__naipe = naipe
        self.__valor = valor

    @property
    def naipe(self):
        return self.__naipe

    @naipe.setter
    def naipe(self, naipe):
        self.__naipe = naipe

    @property
    def face(self):
        return self.__face

    @face.setter
    def face(self, face):
        self.__face = face

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    def __str__(self):
        return f'{self.__face} de {self.__naipe}'

    

