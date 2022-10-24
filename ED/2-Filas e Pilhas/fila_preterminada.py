from fila import Fila

class FilaCheiaException(Exception):
    pass

class FilaPredeterminada(Fila):
    def __init__(self, capacidade=10) -> None:
        super().__init__()
        self.count = 0
        self.capacidade = capacidade
    
    def add(self, valor):
        if self.count < self.capacidade:
            super().add(valor)
            self.count += 1
        else:
            raise FilaCheiaException()

    def remove(self):
        super().remove()
        self.count -= 1

if __name__ == '__main__':
    fila_pre = FilaPredeterminada(4)
    fila_pre.add(5)
    fila_pre.add(10)
    fila_pre.add(15)
    print(fila_pre)
    try:
        fila_pre.add(20)
        fila_pre.add(25)
        fila_pre.add(35)
        fila_pre.add(55)
    except FilaCheiaException:
        print("Fila cheia")
    finally:
        print(fila_pre)