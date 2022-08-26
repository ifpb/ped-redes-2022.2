from Calculadora import Calculadora

calculadora = Calculadora()
operacao = None
while True:
    print("+--------------+",
             f"|{calculadora.registrador: >13} |",
              "+--------------+",
              "(+) somar",
              "(-) subtrair",
              "(/) dividir",
              "(*) multiplicar",
              "(r) resetar",
              "(d) desfazer",
              "(exit) sair",
              "---------------",
              sep='\n')

    operacao = input("Operação: ")

    try:
        if operacao == '+':
            valor = float(input("Valor: "))
            calculadora.adicionar(valor)
            continue

        elif operacao == '-':
            valor = float(input("Valor: "))
            calculadora.subtrair(valor)
            continue

        elif operacao == '/':
            valor = float(input("Valor: "))
            calculadora.dividir(valor)
            continue

        elif operacao == '*':
            valor = float(input("Valor: "))
            calculadora.multiplicar(valor)
            continue

        elif operacao == 'r':
            calculadora.resetar()
            continue

        elif operacao == 'd':
            calculadora.desfazer()
            continue

        elif operacao == 'exit':
            break

        else:
            print('Operação inválida. Veja as opções disponíveis no menu.')

    except ValueError:
         print("Valor Inválido")
         continue

