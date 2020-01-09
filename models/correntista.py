from datetime import datetime
from models.historico import Historico
from models.historico_relatorio import HistoricoRelatorio
from models.conta import Conta
from models.pessoa import Pessoa
from iterators.correntista import Correntista as IteratorCorrentista


class Correntista:
    """
    Responsável por gerenciar os dados do correntista
    """
    def __init__(self, nome, saldo):
        self.__historico = HistoricoRelatorio()
        self.__pessoa = Pessoa(nome)
        self.__conta = Conta(saldo)

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
        historico = self.__historico_cadastro(
            mensagem="Depósito",
            valor=valor,
            tipo_operacao=Historico.DEPOSITO
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
        historico = self.__historico_cadastro(
            mensagem="Saque",
            valor=valor,
            tipo_operacao=Historico.SAQUE
        )
        self.__historico.inserir(historico)

    def __historico_cadastro(self, mensagem=None, valor=0, tipo_operacao="C"):
        historico = Historico()
        historico.mensagem = mensagem
        historico.valor = float(valor)
        historico.saldo = float(self.saldo())
        historico.tipo_operacao = tipo_operacao
        historico.data = datetime.now()
        return historico

    def __str__(self):
        return "Correntista: {0}\nSaldo: R${1}".format(
            self.nome(),
            format(float(self.saldo()), '.2f')
        )

    def __iter__(self):
        return IteratorCorrentista(self.__historico)
