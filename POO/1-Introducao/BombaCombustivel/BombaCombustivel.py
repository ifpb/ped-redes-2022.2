class BombaCombustivel():

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.setTipoCombustivel(tipoCombustivel)
        self.setValorLitro(valorLitro)
        self.setQuantidadeCombustivel(quantidadeCombustivel)

    def setTipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def getTipoCombustivel(self):
        return self.tipoCombustivel 
        
    def setValorLitro(self, valorLitro):
        self.valorLitro = float(valorLitro)

    def setQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        totalLitros = valor / self.valorLitro
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(
                self.quantidadeCombustivel - totalLitros)

    def abastecerPorLitro(self, totalLitros):
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(
                self.quantidadeCombustivel - totalLitros)


    def mudarCombustivel(bomba, tipoCombustivel):
        bomba.setTipoCombustivel(tipoCombustivel)
        print(f'Bomba utilizando {bomba.getTipoCombustivel()}')

    
# Teste da classe
bomba1 = BombaCombustivel('Gasolina Aditivada', 6.90, 10000)
bomba2 = BombaCombustivel('Alcool', 4.70, 5000)
bomba3 = BombaCombustivel('Diesel', 5.90, 20000)

while True:

    
    print("----------------------------POSTO TEXACO---------------------------")
    print("Bomba 1: ",bomba1.tipoCombustivel)
    print("Bomba 2: " ,bomba2.tipoCombustivel)
    print("-------------------------------------------------------------------")
    print("PREÇO GASOLINA",bomba1.valorLitro)
    print("PREÇO ALCOOL",bomba2.valorLitro)

    print('''
----------------------------
1- ALTERAR PREÇO
2- COLOCAR COMBUSTIVEL
3- ZERAR BOMBA
4- MUDAR COMBUSTIVEL DA BOMBA
5- SAIR
''')
    
    x = float(input("DIGITE A OPÇÃO DESEJADA: "))
    if x == 1:
        alterar = float(input("(1) ALTERAR PREÇO GASOLINA (2) ALTERAR PREÇO DO ALCOOL: "))

        if alterar == 1:
            n=float(input('Novo Preço: '))
            bomba1.setValorLitro(n)
            print("PREÇO DA GASOLINA ALTERADO PARA:",bomba1.valorLitro)


        if alterar == 2:
            n=float(input('Novo Preço: '))
            bomba2.setValorLitro(n)
            print("PREÇO DO ALCOOL ALTERADO PARA:",bomba2.valorLitro)


    if x == 2:

        colocar = float(input("(1) GASOLINA (2) ALCOOL: "))

        if colocar == 1:
            z = float(input("DIGITE VALOR DESEJADO: "))
            gasolina = bomba1.valorLitro
            print("VOCÊ ABASTECEU",z/gasolina,"L DE GASOLINA")


        if colocar == 2:
            r = float(input("DIGITE O VALOR DESEJADO: "))
            alcool = bomba2.valorLitro
            print("VOCÊ ABASTECEU,",r/alcool,"L DE ALCOOL")


    if x == 3:
        e=float(input("(1) ZERAR BOMBA DE GASOLINA (2) ZERAR BOMBA DE ALCOOL: "))

        if e == 1 :
            bomba1.quantidadeCombustivel = 0

        if e ==2:
            bomba2.quantidadeCombustivel = 0
            
    if x == 4:
        print("BOMBA 1:")
        comb=input("Combustivel: ")

        mudarCombustivel(bomba1,comb)

    if x == 5:
        break

