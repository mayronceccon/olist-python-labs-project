from models.historico import Historico
from models.conta import Conta
from models.pessoa import Pessoa
from iterators.correntista import Correntista as IteratorCorrentista


class Correntista:
    """
    Responsável por gerenciar os dados do correntista
    """
    def __init__(self, nome, saldo):
        self.__pessoa = Pessoa(nome)
        self.__conta = Conta(saldo)
        self.__historico = Historico()

    def nome(self):
        return self.__pessoa.nome()

    def saldo(self):
        return self.__conta.saldo()

    def depositar(self, valor):
        """
        Depósito de valores

        Para o depósito, o valor deve ser:
        * um número integer ou float
        * o valor não deve ser negativo
        """
        self.__conta.depositar(valor)
        self.__historico_depositar(valor)

    def __historico_depositar(self, valor):
        historico = 'Deposito de R${0} - Saldo atual R${1}'.format(
            format(valor, '.2f'),
            format(float(self.saldo()), '.2f')
        )
        self.__historico.inserir(historico)

    def sacar(self, valor):
        """
        Saque de valores

        Para o saque, o valor deve ser:
        * um número integer ou float
        * o valor não deve ser negativo
        * se o saldo for insulficiente uma exceção será retornada
        """
        self.__conta.sacar(valor)
        self.__historico_sacar(valor)

    def __historico_sacar(self, valor):
        historico = "Saque de R${0} - Saldo atual R${1}".format(
            format(valor, '.2f'),
            format(float(self.saldo()), '.2f')
        )
        self.__historico.inserir(historico)

    def __str__(self):
        return "Correntista: {0}\nSaldo: R${1}".format(
            self.nome(),
            format(float(self.saldo()), '.2f')
        )

    def __iter__(self):
        return IteratorCorrentista(self.__historico)
