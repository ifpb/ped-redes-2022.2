from enum import Enum


class SalarioMinimoException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class TurnoInvalidoException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class SalarioInvalidoException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Turno(Enum):
    MANHA = 'dia'
    TARDE = 'dia'
    NOITE = 'noite'
    MADRUGADA = 'noite'

class Funcionario:

    __SALARIO_MINIMO = 1212.00

    def __init__(self, nome, salario) -> None:
        self.nome = nome
        self.salario = salario

    def adicionaAumento(self, valor):
        self.salario += valor

    def ganhoAnual(self):
        return self.salario * 13

    def exibeDados(self):
        return f"Nome: {self.nome}, Salário: {self.salario}"

    def __str__(self):
        return self.exibeDados()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):

        if type(salario).__name__ != 'float':
            raise SalarioInvalidoException(self.nome, salario)

        if salario < Funcionario.__SALARIO_MINIMO:
            raise SalarioMinimoException(self.nome, salario)
        
        self.__salario = salario

class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula) -> None:
        super().__init__(nome, salario)
        self.matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    def exibeDados(self):
        return super().exibeDados() + f", Matrícula: {self.matricula}"

class AssistenteTecnico(Assistente):
    def __init__(self, nome, salario, matricula, bonusSalarial) -> None:
        super().__init__(nome, salario, matricula)
        self.bonusSalarial = bonusSalarial

    @property
    def bonusSalarial(self):
        return self.__bonusSalarial

    @bonusSalarial.setter
    def bonusSalarial(self, bonusSalarial):
        self.__bonusSalarial = bonusSalarial

    def ganhoAnual(self):
        return super().ganhoAnual() + (self.bonusSalarial * 12)

class AssistenteAdministrativo(Assistente):

    TURNOS_VALIDOS = ['dia', 'noite']

    def __init__(self, nome, salario, matricula, turno: Turno) -> None:
        super().__init__(nome, salario, matricula)
        self.turno = turno.value

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
        turno = turno.lower()
        if turno not in AssistenteAdministrativo.TURNOS_VALIDOS:
            raise TurnoInvalidoException(turno)

        self.__turno = turno

    def ganhoAnual(self):
        adicionalNoturno = 150 * 12
        return super().ganhoAnual() + (adicionalNoturno if self.turno == 'noite' else 0.0)

if __name__ == '__main__':
    try:
        f = Funcionario("José da Silva", 1400.00)
        print(f.exibeDados())
        print(f"Ganho Anual = R$ {f.ganhoAnual():.2f}")

        a = Assistente("Maria Joaquina", 1950.00, "123456")
        print(a.exibeDados())

        tecnico = AssistenteTecnico("Joaquim da Silva", 1950.00, "654321", 100.00)
        print(tecnico.exibeDados())
        print(f"Ganho Anual = R$ {tecnico.ganhoAnual():.2f}")

        administrativo = AssistenteAdministrativo("Josefa da Costa", 1950.00, "123123", Turno.NOITE)
        print(administrativo.exibeDados())
        print(f"Ganho Anual = R$ {administrativo.ganhoAnual():.2f}")

        administrativo2 = AssistenteAdministrativo("Zenilda", 1950.00, "111222", Turno.MADRUGADA)
        print(administrativo2.exibeDados())
        print(f"Ganho Anual = R$ {administrativo2.ganhoAnual():.2f}")
    except SalarioMinimoException as es:
        print(f"Salário de R$ {es.args[1]:.2f} de {es.args[0]} deve ser maior ou igual a R$ 1212.00")
    except TurnoInvalidoException as ti:
        print(f"Turno de nome {ti.args[0]} inválido. Use {AssistenteAdministrativo.TURNOS_VALIDOS}")
    except SalarioInvalidoException as sl:
        print(f"Salário de {sl.args[0]} ({sl.args[1]}) deve ser fornecido como decimal (exemplo: 1212.00)")
    else:
        print("Deu tudo certo!")
    finally:
        print("Encerrando execução do programa")