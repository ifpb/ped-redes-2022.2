from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calculaArea(self):
        """calcula área de uma forma geométrica

        Returns:
            float|int: resultado do cálculo da área
        """
        pass

class FormaComBaseEAltura(FormaGeometrica):
    def __init__(self, base, altura) -> None:
        super().__init__()
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, base):
        assert type(base) == int or type(base) == float, "Base deve ser um número"
        self.__base = base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        assert type(altura) == int or type(altura) == float, "Altura deve ser um número"
        self.__altura = altura

class Retangulo(FormaComBaseEAltura):
    def __init__(self, base, altura) -> None:
        super().__init__(base, altura)

    def calculaArea(self):
        return self.base * self.altura

class Triangulo(FormaComBaseEAltura):
    def __init__(self, base, altura) -> None:
        super().__init__(base, altura)

    def calculaArea(self):
        return (self.base * self.altura) / 2

class Trapezio(FormaComBaseEAltura):
    def __init__(self, base, altura, baseMaior) -> None:
        super().__init__(base, altura)
        self.baseMaior = baseMaior

    @property
    def baseMaior(self):
        return self.__baseMaior
    
    @baseMaior.setter
    def baseMaior(self, baseMaior):
        assert type(baseMaior) == int or type(baseMaior) == float, "Base maior deve ser um número"
        assert baseMaior > self.base, "A base maior precisa ser maior do que a base menor"
        self.__baseMaior = baseMaior
    
    def calculaArea(self):
        return ((self.baseMaior + self.base) * self.altura) / 2

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, raio):
        assert type(raio) == int or type(raio) == float, "Raio deve ser um número"
        self.__raio = raio

    def calculaArea(self):
        return math.pi * math.pow(self.raio, 2)


try:
    c = Circulo(10)
    ti = Triangulo(30, 50)
    r = Retangulo(10, 20)
    ta = Trapezio(10, 20, 30)

    for f in [c, ti, r, ta]:
        print(f"Aréa do {f.__class__.__name__} = {f.calculaArea()}")

except AssertionError as e:
    print(e)