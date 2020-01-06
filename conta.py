from deposito import Deposito
from saque import Saque


class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def saldo(self):
        return format(self.__saldo, '.2f')

    def depositar(self, valor):
        deposito = Deposito(self, valor)
        self.__saldo = deposito.saldo()

    def sacar(self, valor):
        saque = Saque(self, valor)
        self.__saldo = saque.saldo()
