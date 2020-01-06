
class Correntista:
    """
    Responsável por gerenciar os dados do correntista
    """
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo
        self.__historico = []

    def nome(self):
        return self.__nome

    def saldo(self):
        return format(self.__saldo, '.2f')

    def depositar(self, valor):
        """
        Depósito de valores

        Para o depósito, o valor deve ser:
        * um número integer ou float
        * o valor não deve ser negativo
        """
        self.__validar_deposito(valor)
        self.__saldo += valor
        self.__inserir_historico_deposito(valor)

    def __validar_deposito(self, valor):
        if not self.__number(valor):
            raise Exception('DEPÓSITO - ERRO: Informe um valor para o depósito')

        if self.__valor_negativo(valor):
            raise Exception('DEPÓSITO - ERRO: Valores negativos não são permitidos')

    def __inserir_historico_deposito(self, valor):
        historico = "Deposito de R${deposito} - Saldo atual R${saldo_atual}".format(
            deposito=format(valor, '.2f'),
            saldo_atual=format(self.__saldo, '.2f')
        )
        self.__salva_historico(historico)

    def sacar(self, valor):
        """
        Saque de valores

        Para o saque, o valor deve ser:
        * um número integer ou float
        * o valor não deve ser negativo
        * se o saldo for insulficiente uma exceção será retornada
        """
        self.__validar_saque(valor)

        self.__saldo -= valor
        self.__inserir_historico_saque(valor)

    def __validar_saque(self, valor):
        if not self.__number(valor):
            raise Exception('SAQUE - ERRO: Informe um valor para o saque')

        if self.__valor_negativo(valor):
            raise Exception('SAQUE - ERRO: Valores negativos não são permitidos')

        if (self.__saldo - valor < 0):
            raise Exception('SAQUE - ERRO: Seu saldo é insulficiente')

    def __inserir_historico_saque(self, valor):
        historico = "Saque de R${deposito} - Saldo atual R${saldo_atual}".format(
            deposito=format(valor, '.2f'),
            saldo_atual=format(self.__saldo, '.2f')
        )
        self.__salva_historico(historico)

    def __salva_historico(self, historico):
        self.__historico.append(historico)

    def __number(self, valor):
        if type(valor) is float:
            return True

        if type(valor) is int:
            return True

        return False

    def __valor_negativo(self, valor):
        if valor <= 0:
            return True
        return False

    def __str__(self):
        return "Correntista: {correntista}\nSaldo: R${saldo}".format(
            correntista=self.__nome,
            saldo=format(self.__saldo, '.2f')
        )

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index > len(self.__historico) - 1:
            raise StopIteration
        historico = self.__historico[self.__index]
        self.__index += 1
        return historico


if __name__ == '__main__':
    correntista = Correntista("Leo", 500.0)
    print(correntista)

    print(correntista.nome())
    print(correntista.saldo())
    correntista.depositar(25.50)
    correntista.sacar(50)
    correntista.sacar(40)
    correntista.sacar(80)
    correntista.sacar(300)
    correntista.sacar(50)

    for hist in correntista:
        print(hist)
