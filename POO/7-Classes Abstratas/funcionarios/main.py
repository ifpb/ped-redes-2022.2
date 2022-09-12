from funcionarios import Gerente, Diretor, Presidente, GrauInstrucao

try:
    g = Gerente("Steve Jobs", 1500, GrauInstrucao.ENSINO_MEDIO)
    d = Diretor("Bill Gates", 3500, GrauInstrucao.MESTRE)
    p = Presidente("Linus Torvalds", 2000, GrauInstrucao.DOUTOR)

    for f in [g,d,p]:
        print(f)

except Exception as fe:
    print(fe)