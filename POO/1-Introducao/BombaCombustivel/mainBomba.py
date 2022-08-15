from BombaCombustivel import Bomba

b1 = Bomba()
b2 = Bomba()
b3 = Bomba()

b1.selecionarCombustivel(Bomba.GASOLINA)
b2.selecionarCombustivel(Bomba.ALCOOL)

print(b1)
b1.reajustarPreçoCombustivel(Bomba.GASOLINA, -6.58)
print(b1)

b1.setPreçoGasolina(6.28)
print(b1)

print(b1.preçoGasolina)
b1.preçoGasolina = 4.20
print(b1)