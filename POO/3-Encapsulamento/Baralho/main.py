from Baralho import Baralho
from Carta import Carta

print(Baralho.tipo_baralho())
baralho = Baralho()
outroBaralho = Baralho()

c1 = Carta('As','Ouro',5)
print(c1.naipe)
print(c1.face)
print(c1.valor)
print(c1)
c1.face = '2'
print(c1)
input(...)


print('\nExibindo o Baralho')
print(baralho)
print(f'O Baralho tem carta? = {baralho.tem_carta()}')
input('.....')

print(f'Número de cartas no baralho = {len(baralho)}')
print(f'Carta puxada do Baralho = {baralho.puxar_carta()}')
print(f'Número de cartas no baralho = {len(baralho)}')

input('.....')
# Baralho original
print('\nExibindo o Baralho depois do shuffle()')
baralho.embaralhar()
print(baralho)
# Baralho misturado

#
#while baralho.temCarta():
#    print(f'Carta puxada do Baralho = {baralho.puxarCarta()}')
#    print(f'Número de cartas no baralho = {len(baralho)}')

#if not baralho.temCarta():
#    print('Fim! Não há mais cartas no baralho')

#outroBaralho.juntarBaralho(baralho)
#print(f'Número de cartas do baralho que recebeu as cartas = {len(baralho)}')
#print(f'Número de cartas do baralho que doou as cartas = {len(outroBaralho)}')

input('....')

for i in range(40):
    carta = baralho.puxar_carta()

print('Baralho sem 40 cartas...')
print(baralho)
print(f'Ultima carta: {carta}')


input('....')

if baralho.repor_carta(carta):
    print(f'carta {carta} foi adicionada ao baralho')

if not baralho.repor_carta(carta):
    print(f'carta {carta} NÃO foi adicionada ao baralho')

print('Fim')

#print(f'Número de cartas do baralho = {len(outroBaralho)}')

print(Baralho.tipo_baralho())
print(Baralho.tipo_baralho())

print(baralho)


