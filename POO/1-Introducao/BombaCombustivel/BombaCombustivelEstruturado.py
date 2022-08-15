
# funções da bomba de combustível (tarefas que pode desempenhar)
def mostraVisor( oVisor ):
    print(f'Preço por litro: [R$ {oVisor[0]:5.2f}] Litros: [{oVisor[1]:4.2f}] Total a Pagar: [R$ {oVisor[2]:6.2f}]   ')

def abastecePorLitro( oVisor ):
    pass

# 'Zera' a bomba pra iniciar o abastecimento
def preparaBomba( oVisor ):
    oVisor[2]=0.0
    print('.:.:.:.:..:.:.:.:..:.:.:.: BOMBA ZERADA :..:.:.:.:..:.:.:.:..:.:.:.:.')
    mostraVisor(oVisor)
    print('.:.:.:.:..:.:.:.:..:.:.:.:..:.:.:.:..:.:.:.:..:.:.:.:.:.:.:..:.:.:.:.')
    print()

def ajustarPreço( oVisor, novoValor):
    oVisor[0] = novoPreco


def iniciaAbastecimento(oVisor, valor):
    preçoPorLitro = oVisor[0]
    qtLitros = 0  # quantidade de litros já abastecido
    valorParcial = 0 # o valor que o usuário já está pagando de acordo com a quantidade de litros abastecida

    print('.:.:.:.:..:.:.:.:: INICIANDO ABASTECIMENTO :..:.:.:.:..:.:.:.:..:.:.:.')

    while valorParcial <= valor:
        qtLitros += 1
        valorParcial += preçoPorLitro
        oVisor[1] = qtLitros
        oVisor[2] = valorParcial

        mostraVisor(oVisor)

        if (valor - valorParcial) < preçoPorLitro:
            break
        

    print('.:.:.:.:..:.:.:.:.:.FIM DO ABASTECIMENTO:.:.:.:.:.:.:.:.:.:.:.:.:.:.:')
    oVisor[1] = (valor / preçoPorLitro)
    oVisor[2] = valor
    mostraVisor(oVisor)
    print('.:.:.:.:..:.:.:.:..:.:.:.:..:.:.:.:..:.:.:.:..:.:.:.:.:.:.:..:.:.:.:.')
   

# main: programa principal

# definindo o tipo abstrato de dados (TAD)
#                 preço por litro | litros | valor a pagar
ALCOOL   = 1 # constante que sinaliza o combustivel alcool
GASOLINA = 2 # constante que sinaliza o combustivel gasolina
visorAlcool   = [ 4.53, 0.0, 0.0]
visorGasolina = [ 5.55, 0.0, 0.0]


# comecando o programa
while(True):

    print('Alcool')
    mostraVisor(visorAlcool)
    print('Gasolina')
    mostraVisor(visorGasolina)
    print()

    print('(c) Configurar bomba')
    print('(i) iniciar abastecimentos')
    print('(q) desligar bomba')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    opcao = input('Digite a letra referente à opção desejada: ')
    opcao = opcao.lower()

    while opcao not in 'ciq':
        opcao = input('Digite a letra referente à opção desejada: ')
        opcao = opcao.lower()
        

    if opcao == 'c':
        tipo = int(input('Escolha o combustível que deseja ajustar o preço: (1) Alcool (2) Gasolina: '))   
            
        visor = visorAlcool if tipo == ALCOOL else visorGasolina
        
        novoPreco = float(input(f'Preço Atual: [R$ {visor[0]:5.2f}] Novo Preço: R$ '))

        ajustarPreço(visor,novoPreco)

        input('Preço do combustivel reajustado com sucesso! Pressione ENTER para continuar')
        print()

    elif  opcao == 'i':
        while(True):
        
            print('\nIniciar abastecimento')
            print('----------------------')
            print('Digite 0 (zero) para voltar ao menu principal')
            tipo = int(input('Tipo de Combustível (1) Alcool  (2) Gasolina: '))

            if (tipo == 0):
                break

            visor = visorAlcool if tipo == ALCOOL else visorGasolina
        
            valor = float(input('Valor para abastecimento: R$ '))
            print()

            preparaBomba(visor)
            print()
            iniciaAbastecimento(visor,valor)
        
    else:
        # Saida do programa
        break

print('Fim do Programa')
    


